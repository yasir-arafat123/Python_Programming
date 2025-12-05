# Shutil Module
Purpose: High-level file operations (copying, moving, deleting trees).
## Key Concepts
- \shutil.copy2()\ (preserves metadata) vs \shutil.copy()\
- \shutil.move()\
- \shutil.rmtree()\ (recursive delete - dangerous but useful)
- \shutil.disk_usage()\
- \shutil.which()\ (find executable path)
## Best Practices
- Use \pathlib\ for paths, but \shutil\ for the actual heavy lifting actions.
- Be careful with \mtree\.
