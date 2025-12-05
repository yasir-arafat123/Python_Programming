import shutil
import os
from pathlib import Path
def main():
    # Setup dummy data
    src = Path("test_src")
    src.mkdir(exist_ok=True)
    (src / "file.txt").write_text("Hello")
    dst = Path("test_dst")
    # Copy tree
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f"Copied tree to {dst}")
    # Disk usage
    total, used, free = shutil.disk_usage(".")
    print(f"Free space: {free // (2**30)} GB")
    # Cleanup
    shutil.rmtree(src)
    shutil.rmtree(dst)
if __name__ == "__main__":
    main()
