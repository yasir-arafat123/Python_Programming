# IO Streams (io module)

## Overview

The `io` module provides Python's main facilities for dealing with various types of I/O streams. Most importantly, it offers **in-memory** file-like objects (`StringIO`, `BytesIO`) that behave like files but exist only in RAM - perfect for testing, data processing, and avoiding disk access.

## Core Things to Learn

### 1. StringIO - In-Memory Text Streams

```python
from io import StringIO

# Create a text stream in memory
output = StringIO()
output.write("Hello, ")
output.write("World!\n")
output.write("Line 2\n")

# Read the contents
contents = output.getvalue()  # "Hello, World!\nLine 2\n"

# Reset position to read like a file
output.seek(0)
line1 = output.readline()  # "Hello, World!\n"

output.close()
```

**Use cases:**
- Testing file I/O without creating files
- Capturing print output
- Building strings efficiently
- Mock file objects for unit tests

### 2. BytesIO - In-Memory Binary Streams

```python
from io import BytesIO

# Create a binary stream
buffer = BytesIO()
buffer.write(b"Binary data")
buffer.write(b"\x00\x01\x02")

# Read as bytes
data = buffer.getvalue()  # b'Binary data\x00\x01\x02'

# Use with binary formats
buffer.seek(0)
# ... pass to libraries expecting file-like objects ...

buffer.close()
```

**Use cases:**
- Image/audio processing in memory
- Binary protocol handling
- Testing binary file operations
- Network data buffering

### 3. Context Managers (Auto-Close)

```python
from io import StringIO, BytesIO

# Automatically closed when done
with StringIO() as output:
    output.write("Temporary content")
    result = output.getvalue()
# output is automatically closed here

with BytesIO() as buffer:
    buffer.write(b"Binary data")
    data = buffer.getvalue()
```

### 4. TextIOWrapper - Text Encoding/Decoding

```python
from io import BytesIO, TextIOWrapper

# Wrap binary stream with text encoding
binary_stream = BytesIO(b"Hello, World!")
text_stream = TextIOWrapper(binary_stream, encoding='utf-8')

content = text_stream.read()  # "Hello, World!"
text_stream.close()
```

## Common Use Cases

### 1. Testing File Operations

```python
from io import StringIO
import csv

# Test CSV writing without creating files
output = StringIO()
writer = csv.writer(output)
writer.writerow(['Name', 'Age'])
writer.writerow(['Alice', 30])

csv_content = output.getvalue()
assert 'Alice,30' in csv_content
```

### 2. Capturing Print Output

```python
from io import StringIO
import sys

# Capture stdout
old_stdout = sys.stdout
sys.stdout = captured_output = StringIO()

print("This goes to memory")
print("Not to terminal")

sys.stdout = old_stdout  # Restore stdout

output = captured_output.getvalue()
print(f"Captured: {output}")
```

### 3. Mock Files for Testing

```python
from io import StringIO

def process_file(file_obj):
    """Function that expects a file object."""
    return file_obj.read().upper()

# Test without creating actual files
mock_file = StringIO("hello world")
result = process_file(mock_file)
assert result == "HELLO WORLD"
```

### 4. Image Processing

```python
from io import BytesIO
from PIL import Image  # Pillow library
import requests

# Download image to memory (no disk I/O)
response = requests.get('https://example.com/image.jpg')
image_data = BytesIO(response.content)
image = Image.open(image_data)

# Process and save to memory
output = BytesIO()
image.save(output, format='PNG')
png_data = output.getvalue()
```

### 5. Building Complex Strings

```python
from io import StringIO

# More efficient than string concatenation for many writes
output = StringIO()
for i in range(1000):
    output.write(f"Line {i}\n")

result = output.getvalue()
```

## Python Libraries

| Class | Purpose | Data Type |
|-------|---------|-----------|
| `StringIO` | In-memory text stream | Text (str) |
| `BytesIO` | In-memory binary stream | Binary (bytes) |
| `TextIOWrapper` | Text encoding/decoding wrapper | Text over binary |
| `BufferedReader` | Buffered binary input | Binary |
| `BufferedWriter` | Buffered binary output | Binary |

## Best Practices

### 1. Use Context Managers
```python
# ❌ BAD: Manual close (might forget)
output = StringIO()
output.write("data")
result = output.getvalue()
output.close()

# ✅ GOOD: Automatic cleanup
with StringIO() as output:
    output.write("data")
    result = output.getvalue()
```

### 2. Choose Correct Type
```python
# ❌ BAD: Type mismatch
buffer = StringIO()
buffer.write(b"bytes")  # TypeError!

# ✅ GOOD: Match types
text_buffer = StringIO()
text_buffer.write("text")

binary_buffer = BytesIO()
binary_buffer.write(b"bytes")
```

### 3. Reset Position When Reading
```python
output = StringIO()
output.write("Hello")

# ❌ BAD: Position at end, reads nothing
content = output.read()  # ""

# ✅ GOOD: Seek to start
output.seek(0)
content = output.read()  # "Hello"
```

### 4. Use getvalue() for Full Content
```python
output = StringIO()
output.write("Hello\n")
output.write("World\n")

# ✅ BEST: Get all content at once
content = output.getvalue()  # "Hello\nWorld\n"

# ⚠️ ALTERNATIVE: Seek and read (more steps)
output.seek(0)
content = output.read()
```

## Common Patterns

### CSV in Memory
```python
from io import StringIO
import csv

def create_csv_in_memory(data):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerows(data)
    return output.getvalue()

csv_data = create_csv_in_memory([
    ['Name', 'Score'],
    ['Alice', 95],
    ['Bob', 87]
])
```

### JSON to Binary
```python
from io import BytesIO
import json

def json_to_bytes(data):
    buffer = BytesIO()
    json_str = json.dumps(data)
    buffer.write(json_str.encode('utf-8'))
    return buffer.getvalue()
```

### Redirect Standard Streams
```python
from io import StringIO
import sys
from contextlib import contextmanager

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield new_out, new_err
    finally:
        sys.stdout, sys.stderr = old_out, old_err

# Usage
with captured_output() as (out, err):
    print("stdout message")
    print("stderr message", file=sys.stderr)

print(f"Captured stdout: {out.getvalue()}")
print(f"Captured stderr: {err.getvalue()}")
```

## StringIO vs String Concatenation

**When to use StringIO:**
- Many small writes (hundreds/thousands)
- Building large strings incrementally
- Need file-like interface

**Performance comparison:**
```python
# StringIO: O(n) - efficient
output = StringIO()
for i in range(10000):
    output.write(f"line {i}\n")
result = output.getvalue()

# String concatenation: O(n²) - inefficient
result = ""
for i in range(10000):
    result += f"line {i}\n"  # Creates new string each time!

# Modern alternative: join (also O(n))
lines = [f"line {i}\n" for i in range(10000)]
result = "".join(lines)
```

## io Module Classes Hierarchy

```
IOBase (abstract)
├── RawIOBase (abstract) - Raw binary I/O
│   ├── FileIO
│   └── BytesIO
├── BufferedIOBase (abstract) - Buffered binary I/O
│   ├── BufferedReader
│   ├── BufferedWriter
│   └── BufferedRandom
└── TextIOBase (abstract) - Text I/O
    ├── TextIOWrapper
    └── StringIO
```

## Performance Tips

1. **Use getvalue() once** - It copies data, call it when finished
2. **Reuse buffers** - Reset with `seek(0)` and `truncate()` instead of creating new ones
3. **For large data** - Consider `tempfile.SpooledTemporaryFile` (starts in memory, moves to disk if too large)

## Visualize It

- [Python IO module guide](https://realpython.com/python-io/)
- [StringIO vs file operations](https://www.geeksforgeeks.org/stringio-module-in-python/)

## References

- [Python io docs](https://docs.python.org/3/library/io.html)
- [io module tutorial](https://pymotw.com/3/io/)
- Python roadmap — https://roadmap.sh/python

## Related Topics

- `I.8/2_Paths_pathlib_os` - File system operations
- `I.8/9_Temporary_Files` - Temporary file alternatives
- `J.9_Quality/8_Mocking` - Mocking file operations in tests
- `I.8/6_Pickle_Serialization` - Binary serialization
- `P.15_Performance` - Performance optimization techniques
