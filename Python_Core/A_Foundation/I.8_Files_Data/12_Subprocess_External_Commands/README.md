# Subprocess & External Commands
Purpose: Run external programs and scripts from within Python.
## Key Concepts
- \subprocess.run()\ (modern standard)
- Capturing output (\capture_output=True\, \	ext=True\)
- Checking return codes
- Handling errors (\check=True\)
- Piping input/output (\stdin\, \stdout\, \stderr\)
- \shlex.split()\ for safe command parsing
- Avoiding \os.system\ (legacy/unsafe)
## Security Warning
- Be careful with shell injection when using \shell=True\.
- Prefer passing arguments as a list.
