# 0_Getting_Started

Status: Draft

Use this module when you are brand new to Python or need a clean workstation before diving into the rest of the curriculum.

## Objectives
- Install Python 3.x and add it to your PATH on Windows.
- Install VS Code with the Python extension.
- Configure PowerShell execution policy for local scripts.
- Create and activate a virtual environment.
- Run your first script (`hello_world.py`).

## 1. Install Python
1. Download the latest stable Python 3 installer from https://www.python.org/downloads/windows/
2. During installation, **check** "Add python.exe to PATH".
3. Open a new PowerShell window and verify:
```powershell
python --version
pip --version
```

## 2. Install VS Code + Extensions
1. Download VS Code from https://code.visualstudio.com/
2. Launch VS Code and install the **Python** extension (ms-python.python).
3. Optional but recommended: install **Pylance** (ms-python.vscode-pylance) for language intelligence.

## 3. Configure PowerShell (Windows)
Allow local scripts for the current user if you plan to run helper `.ps1` tools:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## 4. Create a Workspace Folder
```powershell
# choose a directory where you store code
New-Item -ItemType Directory -Path "$HOME\python-playground" -Force | Out-Null
Set-Location "$HOME\python-playground"
```

## 5. Create and Activate a Virtual Environment
```powershell
python -m venv .venv
. .venv\Scripts\Activate
```
You should see `(.venv)` prefixed in the prompt. To exit later, run `deactivate`.

## 6. Run Hello World
1. Copy `hello_world.py` from this folder into your workspace (or open it directly).
2. Run it:
```powershell
python hello_world.py
```
3. You should see `Hello from Python Programming curriculum!`.

## 7. Next Steps
- Keep the `.venv` active while following `01_Python_Core_Topics/1_Setup_Packaging/`.
- Read the root `README.md` "Quick Start Tracks" section to choose your path.
- Update the status line here when the setup instructions are verified on a fresh machine.
