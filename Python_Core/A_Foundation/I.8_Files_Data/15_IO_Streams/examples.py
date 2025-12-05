"""Examples for IO Streams (io module)."""

from io import StringIO, BytesIO, TextIOWrapper
import sys
import csv
import json


# ============================================================================
# Example 1: Basic StringIO Operations
# ============================================================================

def basic_stringio_example():
    """Basic StringIO usage for text streams."""
    print("=== Basic StringIO ===\n")
    
    # Create StringIO buffer
    output = StringIO()
    
    # Write text
    output.write("Hello, ")
    output.write("World!\n")
    output.write("Line 2\n")
    output.write("Line 3")
    
    # Get all content
    content = output.getvalue()
    print("Content:")
    print(content)
    
    # Reset position and read
    output.seek(0)
    first_line = output.readline()
    print(f"\nFirst line: {repr(first_line)}")
    
    # Read all remaining
    remaining = output.read()
    print(f"Remaining: {repr(remaining)}")
    
    output.close()


# ============================================================================
# Example 2: Basic BytesIO Operations
# ============================================================================

def basic_bytesio_example():
    """Basic BytesIO usage for binary streams."""
    print("\n=== Basic BytesIO ===\n")
    
    # Create BytesIO buffer
    buffer = BytesIO()
    
    # Write binary data
    buffer.write(b"Binary data ")
    buffer.write(b"\x00\x01\x02\x03")
    buffer.write(b" More data")
    
    # Get all content
    data = buffer.getvalue()
    print(f"Binary data: {data}")
    print(f"Length: {len(data)} bytes")
    
    # Reset and read
    buffer.seek(0)
    chunk = buffer.read(11)
    print(f"\nFirst chunk: {chunk}")
    
    buffer.close()


# ============================================================================
# Example 3: Context Manager Usage
# ============================================================================

def context_manager_example():
    """Use context managers for automatic cleanup."""
    print("\n=== Context Manager ===\n")
    
    # StringIO with context manager
    with StringIO() as output:
        output.write("Temporary content\n")
        output.write("Will be automatically closed")
        result = output.getvalue()
    # output is automatically closed here
    
    print("StringIO result:")
    print(result)
    
    # BytesIO with context manager
    with BytesIO() as buffer:
        buffer.write(b"Binary content")
        data = buffer.getvalue()
    
    print(f"\nBytesIO result: {data}")


# ============================================================================
# Example 4: Testing CSV Operations
# ============================================================================

def csv_testing_example():
    """Test CSV operations without creating files."""
    print("\n=== CSV in Memory ===\n")
    
    # Write CSV to memory
    output = StringIO()
    writer = csv.writer(output)
    
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'London'])
    writer.writerow(['Charlie', 35, 'Tokyo'])
    
    csv_content = output.getvalue()
    print("CSV content:")
    print(csv_content)
    
    # Read CSV from memory
    input_buffer = StringIO(csv_content)
    reader = csv.DictReader(input_buffer)
    
    print("Parsed data:")
    for row in reader:
        print(f"  {row['Name']}, {row['Age']}, {row['City']}")


# ============================================================================
# Example 5: Capturing Print Output
# ============================================================================

def capture_output_example():
    """Capture stdout to test print statements."""
    print("\n=== Capture stdout ===\n")
    
    # Save original stdout
    original_stdout = sys.stdout
    
    # Redirect stdout to StringIO
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # These prints go to memory
    print("This is captured")
    print("Line 2")
    print(f"Calculated: {2 + 2}")
    
    # Restore stdout
    sys.stdout = original_stdout
    
    # Get captured output
    output = captured_output.getvalue()
    print("Captured output:")
    print(output)
    print(f"Total length: {len(output)} characters")


# ============================================================================
# Example 6: Mock File Operations for Testing
# ============================================================================

def mock_file_example():
    """Mock file objects for testing."""
    print("\n=== Mock File Testing ===\n")
    
    def process_file(file_obj):
        """Function that expects a file object."""
        content = file_obj.read()
        return content.upper()
    
    def count_lines(file_obj):
        """Count lines in file."""
        lines = file_obj.readlines()
        return len(lines)
    
    # Test with StringIO (no actual file needed)
    mock_file = StringIO("hello world\ntest data\nline 3")
    
    # Test first function
    mock_file.seek(0)
    result = process_file(mock_file)
    print(f"Uppercase result: {repr(result)}")
    
    # Test second function
    mock_file.seek(0)
    line_count = count_lines(mock_file)
    print(f"Line count: {line_count}")


# ============================================================================
# Example 7: Building Strings Efficiently
# ============================================================================

def string_building_example():
    """Use StringIO for efficient string building."""
    print("\n=== Efficient String Building ===\n")
    
    import time
    
    # Method 1: String concatenation (slower)
    start = time.perf_counter()
    result = ""
    for i in range(1000):
        result += f"Line {i}\n"
    concat_time = time.perf_counter() - start
    
    # Method 2: StringIO (faster)
    start = time.perf_counter()
    output = StringIO()
    for i in range(1000):
        output.write(f"Line {i}\n")
    result = output.getvalue()
    stringio_time = time.perf_counter() - start
    
    print(f"String concatenation: {concat_time:.6f}s")
    print(f"StringIO: {stringio_time:.6f}s")
    print(f"Speedup: {concat_time/stringio_time:.2f}x")


# ============================================================================
# Example 8: JSON Operations in Memory
# ============================================================================

def json_memory_example():
    """Work with JSON in memory."""
    print("\n=== JSON in Memory ===\n")
    
    # Python object to JSON string in memory
    data = {
        'name': 'Alice',
        'age': 30,
        'skills': ['Python', 'SQL', 'Docker']
    }
    
    # Write JSON to StringIO
    json_buffer = StringIO()
    json.dump(data, json_buffer, indent=2)
    json_str = json_buffer.getvalue()
    
    print("JSON string:")
    print(json_str)
    
    # Read JSON from StringIO
    json_buffer.seek(0)
    loaded_data = json.load(json_buffer)
    print(f"\nLoaded data: {loaded_data}")


# ============================================================================
# Example 9: Binary Data Processing
# ============================================================================

def binary_processing_example():
    """Process binary data in memory."""
    print("\n=== Binary Data Processing ===\n")
    
    # Create binary data
    data = BytesIO()
    
    # Write header (magic number + version)
    data.write(b'MYFORMAT')
    data.write(b'\x01\x00')  # Version 1.0
    
    # Write record count
    record_count = 3
    data.write(record_count.to_bytes(4, byteorder='little'))
    
    # Write records
    for i in range(record_count):
        record = f"Record {i}".encode('utf-8')
        data.write(len(record).to_bytes(2, byteorder='little'))
        data.write(record)
    
    # Read back
    data.seek(0)
    
    # Read header
    magic = data.read(8)
    version = data.read(2)
    print(f"Magic: {magic}")
    print(f"Version: {version}")
    
    # Read record count
    count_bytes = data.read(4)
    count = int.from_bytes(count_bytes, byteorder='little')
    print(f"Record count: {count}")
    
    # Read records
    print("\nRecords:")
    for _ in range(count):
        length = int.from_bytes(data.read(2), byteorder='little')
        record = data.read(length).decode('utf-8')
        print(f"  {record}")


# ============================================================================
# Example 10: TextIOWrapper for Encoding
# ============================================================================

def text_wrapper_example():
    """Use TextIOWrapper for encoding/decoding."""
    print("\n=== TextIOWrapper ===\n")
    
    # Create binary stream with text wrapper
    binary_stream = BytesIO()
    text_stream = TextIOWrapper(binary_stream, encoding='utf-8', newline='')
    
    # Write text (automatically encoded)
    text_stream.write("Hello, 世界!\n")
    text_stream.write("Привет, мир!\n")
    text_stream.write("مرحبا بالعالم!\n")
    text_stream.flush()  # Important: flush to binary stream
    
    # Get binary data
    binary_data = binary_stream.getvalue()
    print(f"Binary data length: {len(binary_data)} bytes")
    print(f"Binary data: {binary_data[:50]}...")
    
    # Read back as text
    binary_stream.seek(0)
    text_stream_read = TextIOWrapper(binary_stream, encoding='utf-8')
    content = text_stream_read.read()
    
    print("\nDecoded text:")
    print(content)


# ============================================================================
# Example 11: Advanced: Redirect stderr
# ============================================================================

def redirect_stderr_example():
    """Capture both stdout and stderr."""
    print("\n=== Redirect stderr ===\n")
    
    import sys
    from contextlib import redirect_stdout, redirect_stderr
    
    # Capture stdout
    with StringIO() as stdout_buf:
        with redirect_stdout(stdout_buf):
            print("This goes to stdout")
            print("Another stdout line")
        
        captured_stdout = stdout_buf.getvalue()
    
    # Capture stderr
    with StringIO() as stderr_buf:
        with redirect_stderr(stderr_buf):
            print("Error message", file=sys.stderr)
            print("Warning", file=sys.stderr)
        
        captured_stderr = stderr_buf.getvalue()
    
    print("Captured stdout:")
    print(captured_stdout)
    
    print("Captured stderr:")
    print(captured_stderr)


# ============================================================================
# Example 12: Seek and Tell Operations
# ============================================================================

def seek_tell_example():
    """Understand seek and tell operations."""
    print("\n=== Seek and Tell ===\n")
    
    buffer = StringIO("ABCDEFGHIJKLMNOP")
    
    # Current position
    print(f"Initial position: {buffer.tell()}")
    
    # Read some data
    data = buffer.read(5)
    print(f"Read: {data}")
    print(f"Position after read: {buffer.tell()}")
    
    # Seek to beginning
    buffer.seek(0)
    print(f"After seek(0): {buffer.tell()}")
    
    # Seek to end
    buffer.seek(0, 2)  # 2 = SEEK_END
    print(f"At end: {buffer.tell()}")
    
    # Seek relative to current
    buffer.seek(0)
    buffer.read(5)
    buffer.seek(3, 1)  # 1 = SEEK_CUR (skip 3 chars)
    print(f"After relative seek: {buffer.tell()}")
    print(f"Read from position 8: {buffer.read(4)}")


# ============================================================================
# Run all examples
# ============================================================================

if __name__ == '__main__':
    basic_stringio_example()
    basic_bytesio_example()
    context_manager_example()
    csv_testing_example()
    capture_output_example()
    mock_file_example()
    string_building_example()
    json_memory_example()
    binary_processing_example()
    text_wrapper_example()
    redirect_stderr_example()
    seek_tell_example()
    
    print("\n" + "="*60)
    print("All examples completed!")
    print("="*60)
