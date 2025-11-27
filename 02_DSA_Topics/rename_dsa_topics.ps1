<#!
Rename DSA topic folders from pattern NN_NN_Name to N_Name and subfolders 01_X -> 1_X.
Also normalize README headings: '# 01_Foundations' -> '# Foundations'.
Dry-run supported with -DryRun switch.
#>
param(
  [switch]$DryRun
)

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "Root: $Root" -ForegroundColor Cyan

# Function: Simplify a top-level folder name like 01_01_Foundations -> 1_Foundations
function Get-NewTopLevelName([string]$name) {
  if ($name -match '^(\d{2})_(\d{2})_(.+)$') {
    $n1 = [int]$Matches[1]  # drop leading zero
    $rest = $Matches[3]
    return "$n1" + '_' + $rest
  }
  return $name
}

# Function: Simplify a subfolder name 01_XYZ -> 1_XYZ (only if starts with 0[1-9]_)
function Get-NewSubName([string]$name) {
  if ($name -match '^0([1-9])_(.+)$') { return "$($Matches[1])_" + $Matches[2] }
  return $name
}

$planned = @()

# Collect top-level renames
Get-ChildItem -Path $Root -Directory | ForEach-Object {
  $old = $_.Name
  $new = Get-NewTopLevelName -name $old
  if ($new -ne $old -and -not (Test-Path (Join-Path $Root $new))) {
    $planned += [pscustomobject]@{ Scope='Top'; Old=$old; New=$new; Path=$_.FullName }
  }
}

# Collect subfolder renames (after computing new top names to map path)
foreach ($p in Get-ChildItem -Path $Root -Directory) {
  $parentOld = $p.Name
  $parentNew = Get-NewTopLevelName -name $parentOld
  $parentPathActual = $p.FullName
  Get-ChildItem -Path $parentPathActual -Directory -ErrorAction SilentlyContinue | ForEach-Object {
    $oldSub = $_.Name
    $newSub = Get-NewSubName -name $oldSub
    if ($newSub -ne $oldSub -and -not (Test-Path (Join-Path $parentPathActual $newSub))) {
      $planned += [pscustomobject]@{ Scope='Sub'; Old=$oldSub; New=$newSub; Path=$_.FullName; ParentOld=$parentOld; ParentNew=$parentNew }
    }
  }
}

if ($planned.Count -eq 0) {
  Write-Host "No folder renames needed." -ForegroundColor Yellow
} else {
  Write-Host "Planned folder renames:" -ForegroundColor Cyan
  $planned | ForEach-Object {
    if ($_.Scope -eq 'Top') { Write-Host ("  TOP: {0} -> {1}" -f $_.Old, $_.New) }
    else { Write-Host ("  SUB: {0}/{1} -> {0}/{2}" -f $_.ParentOld, $_.Old, $_.New) }
  }
}

# Heading normalization plan (README.md in each top-level folder)
$headingPlanned = @()
Get-ChildItem -Path $Root -Directory | ForEach-Object {
  $folder = $_.FullName
  $readme = Join-Path $folder 'README.md'
  if (Test-Path $readme) {
    $content = Get-Content $readme -Raw
    if ($content -match '^#\s+0?\d{1,2}_(.+)$') {
      $newHeading = ($content -replace '^#\s+0?\d{1,2}_','# ') -replace '\r?\n','# ' + ($Matches[1]) + "`n"  # simplified but ensure first heading changed
      # Actually simpler: just replace pattern
      $updated = $content -replace '^#\s+0?\d{1,2}_','# '
      if ($updated -ne $content) {
        $headingPlanned += [pscustomobject]@{ File=$readme }
      }
    }
  }
}

if ($headingPlanned.Count -gt 0) {
  Write-Host "Planned heading normalizations:" -ForegroundColor Cyan
  $headingPlanned | ForEach-Object { Write-Host "  HDR: $($_.File)" }
}

if ($DryRun) {
  Write-Host "Dry run only. No changes applied." -ForegroundColor Green
  exit 0
}

# Apply folder renames: Top level first, then subfolders (re-scan after top-level rename)
$errors = 0

# Top-level renames
$topItems = $planned | Where-Object Scope -eq 'Top'
foreach ($t in $topItems) {
  try {
    Rename-Item -Path $t.Path -NewName $t.New -ErrorAction Stop
    Write-Host "Renamed TOP: $($t.Old) -> $($t.New)" -ForegroundColor Green
  } catch { Write-Warning "Failed TOP: $($t.Old): $($_.Exception.Message)"; $errors++ }
}

# Subfolder renames (need to account for new top-level names)
$subItems = $planned | Where-Object Scope -eq 'Sub'
foreach ($s in $subItems) {
  $parentAfter = Join-Path $Root $s.ParentNew
  $targetOld = if (Test-Path (Join-Path $parentAfter $s.Old)) { Join-Path $parentAfter $s.Old } else { $s.Path }
  if (-not (Test-Path $targetOld)) { Write-Warning "Skip missing sub: $($s.ParentNew)/$($s.Old)"; continue }
  try {
    Rename-Item -Path $targetOld -NewName $s.New -ErrorAction Stop
    Write-Host "Renamed SUB: $($s.ParentNew)/$($s.Old) -> $($s.ParentNew)/$($s.New)" -ForegroundColor Green
  } catch { Write-Warning "Failed SUB: $($s.ParentOld)/$($s.Old): $($_.Exception.Message)"; $errors++ }
}

# Apply heading normalization
foreach ($h in $headingPlanned) {
  try {
    (Get-Content $h.File -Raw) -replace '^#\s+0?\d{1,2}_','# ' | Set-Content $h.File -Encoding UTF8
    Write-Host "Updated Heading: $($h.File)" -ForegroundColor Cyan
  } catch { Write-Warning "Failed heading: $($h.File): $($_.Exception.Message)"; $errors++ }
}

Write-Host "Done. Folder renames: $($planned.Count) attempted. Heading updates: $($headingPlanned.Count). Errors: $errors" -ForegroundColor Cyan
exit $errors
