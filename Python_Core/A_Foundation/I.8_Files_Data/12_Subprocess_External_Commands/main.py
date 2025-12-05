import subprocess
import sys
import shlex
def main():
    # Simple command
    print("--- Running 'echo' ---")
    # Windows uses cmd /c echo, Linux uses echo directly. 
    # Python's subprocess usually handles finding the executable if in PATH.
    # For cross-platform echo, we might just print, but let's try 'python --version'
    cmd = [sys.executable, "--version"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Return code: {result.returncode}")
    print(f"Stdout: {result.stdout.strip()}")
    # Checking for errors
    print("\n--- Running invalid command ---")
    try:
        subprocess.run(["python", "-c", "import sys; sys.exit(1)"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Caught expected error: {e}")
if __name__ == "__main__":
    main()
