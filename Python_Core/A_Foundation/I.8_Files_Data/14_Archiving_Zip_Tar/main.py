import zipfile
from pathlib import Path
def main():
    # Create a zip
    with zipfile.ZipFile('archive.zip', 'w') as zf:
        zf.writestr('file1.txt', 'Content of file 1')
        zf.writestr('file2.txt', 'Content of file 2')
    # Read a zip
    with zipfile.ZipFile('archive.zip', 'r') as zf:
        print("Contents:", zf.namelist())
        content = zf.read('file1.txt').decode()
        print("File 1:", content)
    # Cleanup
    Path('archive.zip').unlink()
if __name__ == "__main__":
    main()
