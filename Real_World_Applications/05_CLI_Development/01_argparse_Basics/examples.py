"""Examples for argparse Basics."""

import argparse
import sys
from pathlib import Path


# ============================================================================
# Example 1: Basic Argument Parser
# ============================================================================

def basic_example():
    """Simple argument parser with positional and optional args."""
    print("=== Basic Parser ===\n")
    
    parser = argparse.ArgumentParser(
        description='Process a file with optional settings'
    )
    
    # Positional argument (required)
    parser.add_argument('filename', help='Input file to process')
    
    # Optional flag (boolean)
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')
    
    # Optional argument with value
    parser.add_argument('--output', '-o', default='output.txt',
                       help='Output file (default: %(default)s)')
    
    # Parse test args
    test_args = ['input.txt', '--verbose', '--output', 'result.txt']
    args = parser.parse_args(test_args)
    
    print(f"Filename: {args.filename}")
    print(f"Verbose: {args.verbose}")
    print(f"Output: {args.output}")


# ============================================================================
# Example 2: Type Conversion
# ============================================================================

def type_conversion_example():
    """Use type conversion for arguments."""
    print("\n=== Type Conversion ===\n")
    
    parser = argparse.ArgumentParser()
    
    # Integer argument
    parser.add_argument('--count', type=int, default=10,
                       help='Number of items (default: %(default)s)')
    
    # Float argument
    parser.add_argument('--ratio', type=float, default=0.5,
                       help='Ratio value (default: %(default)s)')
    
    # Path argument
    parser.add_argument('--config', type=Path,
                       help='Configuration file path')
    
    test_args = ['--count', '25', '--ratio', '0.75', '--config', 'config.ini']
    args = parser.parse_args(test_args)
    
    print(f"Count: {args.count} (type: {type(args.count).__name__})")
    print(f"Ratio: {args.ratio} (type: {type(args.ratio).__name__})")
    print(f"Config: {args.config} (type: {type(args.config).__name__})")


# ============================================================================
# Example 3: Custom Validation
# ============================================================================

def validation_example():
    """Custom type validation."""
    print("\n=== Custom Validation ===\n")
    
    def port_number(value):
        """Validate port number."""
        port = int(value)
        if not 1 <= port <= 65535:
            raise argparse.ArgumentTypeError(
                f"{port} is not a valid port (1-65535)"
            )
        return port
    
    def positive_int(value):
        """Validate positive integer."""
        num = int(value)
        if num <= 0:
            raise argparse.ArgumentTypeError(f"{num} must be positive")
        return num
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=port_number, default=8080,
                       help='Server port')
    parser.add_argument('--workers', type=positive_int, default=4,
                       help='Number of workers')
    
    # Valid args
    args = parser.parse_args(['--port', '3000', '--workers', '8'])
    print(f"Port: {args.port}")
    print(f"Workers: {args.workers}")
    
    # Invalid args would raise error:
    # args = parser.parse_args(['--port', '99999'])  # Error!


# ============================================================================
# Example 4: Actions
# ============================================================================

def actions_example():
    """Different argument actions."""
    print("\n=== Argument Actions ===\n")
    
    parser = argparse.ArgumentParser()
    
    # store_true (flag)
    parser.add_argument('--verbose', action='store_true')
    
    # store_false
    parser.add_argument('--no-cache', action='store_true')
    
    # store_const
    parser.add_argument('--debug', action='store_const', const=True, default=False)
    
    # append (collect multiple values)
    parser.add_argument('--include', action='append', default=[])
    
    # count (count occurrences)
    parser.add_argument('-v', action='count', default=0,
                       help='Verbosity level (-v, -vv, -vvv)')
    
    test_args = ['--verbose', '--include', 'dir1', '--include', 'dir2', '-vvv']
    args = parser.parse_args(test_args)
    
    print(f"Verbose: {args.verbose}")
    print(f"No cache: {args.no_cache}")
    print(f"Include dirs: {args.include}")
    print(f"Verbosity level: {args.v}")


# ============================================================================
# Example 5: Choices
# ============================================================================

def choices_example():
    """Restrict argument values with choices."""
    print("\n=== Choices ===\n")
    
    parser = argparse.ArgumentParser()
    
    # String choices
    parser.add_argument('--format', choices=['json', 'xml', 'yaml', 'csv'],
                       default='json',
                       help='Output format')
    
    # Integer choices (range)
    parser.add_argument('--threads', type=int, choices=range(1, 9),
                       default=4,
                       help='Number of threads (1-8)')
    
    # Enum-like choices
    parser.add_argument('--log-level',
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       default='INFO')
    
    args = parser.parse_args(['--format', 'xml', '--threads', '4', '--log-level', 'DEBUG'])
    
    print(f"Format: {args.format}")
    print(f"Threads: {args.threads}")
    print(f"Log level: {args.log_level}")


# ============================================================================
# Example 6: Required Optional Arguments
# ============================================================================

def required_example():
    """Make optional arguments required."""
    print("\n=== Required Arguments ===\n")
    
    parser = argparse.ArgumentParser()
    
    # Optional syntax but required
    parser.add_argument('--api-key', required=True,
                       help='API key (required)')
    
    parser.add_argument('--endpoint', required=True,
                       help='API endpoint URL')
    
    parser.add_argument('--timeout', type=int, default=30,
                       help='Timeout in seconds')
    
    test_args = ['--api-key', 'abc123', '--endpoint', 'https://api.example.com']
    args = parser.parse_args(test_args)
    
    print(f"API Key: {args.api_key}")
    print(f"Endpoint: {args.endpoint}")
    print(f"Timeout: {args.timeout}")


# ============================================================================
# Example 7: Mutually Exclusive Groups
# ============================================================================

def mutually_exclusive_example():
    """Create mutually exclusive argument groups."""
    print("\n=== Mutually Exclusive ===\n")
    
    parser = argparse.ArgumentParser()
    
    # Can't use both --json and --xml
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--json', action='store_true', help='JSON output')
    group.add_argument('--xml', action='store_true', help='XML output')
    
    # Can't use both --quiet and --verbose
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument('--quiet', action='store_true')
    verbosity.add_argument('--verbose', action='store_true')
    
    # Valid: only one from each group
    args = parser.parse_args(['--json', '--quiet'])
    print(f"JSON: {args.json}, XML: {args.xml}")
    print(f"Quiet: {args.quiet}, Verbose: {args.verbose}")
    
    # Invalid would raise error:
    # args = parser.parse_args(['--json', '--xml'])  # Error!


# ============================================================================
# Example 8: Subcommands
# ============================================================================

def subcommands_example():
    """Implement subcommands like git."""
    print("\n=== Subcommands ===\n")
    
    parser = argparse.ArgumentParser(prog='myapp')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # 'start' subcommand
    start_parser = subparsers.add_parser('start', help='Start the service')
    start_parser.add_argument('--port', type=int, default=8000)
    start_parser.add_argument('--workers', type=int, default=4)
    
    # 'stop' subcommand
    stop_parser = subparsers.add_parser('stop', help='Stop the service')
    stop_parser.add_argument('--force', action='store_true')
    
    # 'status' subcommand
    status_parser = subparsers.add_parser('status', help='Check status')
    status_parser.add_argument('--verbose', action='store_true')
    
    # Test 'start' command
    args = parser.parse_args(['start', '--port', '3000', '--workers', '8'])
    
    if args.command == 'start':
        print(f"Starting service on port {args.port} with {args.workers} workers")
    elif args.command == 'stop':
        print(f"Stopping service (force: {args.force})")
    elif args.command == 'status':
        print(f"Checking status (verbose: {args.verbose})")


# ============================================================================
# Example 9: Argument Groups
# ============================================================================

def argument_groups_example():
    """Organize arguments into groups for better help."""
    print("\n=== Argument Groups ===\n")
    
    parser = argparse.ArgumentParser()
    
    # Input group
    input_group = parser.add_argument_group('input options',
                                           'Options for input sources')
    input_group.add_argument('--file', help='Input file')
    input_group.add_argument('--stdin', action='store_true', help='Read from stdin')
    input_group.add_argument('--url', help='Input URL')
    
    # Output group
    output_group = parser.add_argument_group('output options',
                                            'Options for output format')
    output_group.add_argument('--output', help='Output file')
    output_group.add_argument('--format', choices=['json', 'xml'])
    output_group.add_argument('--pretty', action='store_true')
    
    # Processing group
    process_group = parser.add_argument_group('processing options')
    process_group.add_argument('--threads', type=int, default=1)
    process_group.add_argument('--timeout', type=int, default=30)
    
    args = parser.parse_args(['--file', 'input.txt', '--format', 'json', '--pretty'])
    
    print(f"Input file: {args.file}")
    print(f"Format: {args.format}")
    print(f"Pretty: {args.pretty}")


# ============================================================================
# Example 10: Real-World Application
# ============================================================================

def real_world_example():
    """Complete CLI application example."""
    print("\n=== Real-World Application ===\n")
    
    parser = argparse.ArgumentParser(
        prog='data-processor',
        description='Process and transform data files',
        epilog='Example: %(prog)s input.csv --output result.json --format json'
    )
    
    # Positional arguments
    parser.add_argument('input_file', type=Path,
                       help='Input data file')
    
    # Output options
    parser.add_argument('--output', '-o', type=Path, default=Path('output.json'),
                       help='Output file (default: %(default)s)')
    parser.add_argument('--format', '-f', choices=['json', 'csv', 'xml'],
                       default='json',
                       help='Output format (default: %(default)s)')
    
    # Processing options
    parser.add_argument('--filter', action='append', default=[],
                       help='Filter criteria (can specify multiple)')
    parser.add_argument('--sort-by', help='Sort by field')
    parser.add_argument('--limit', type=int, help='Limit number of results')
    
    # Verbosity
    parser.add_argument('--verbose', '-v', action='count', default=0,
                       help='Increase verbosity')
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Suppress output')
    
    # Version
    parser.add_argument('--version', action='version', version='%(prog)s 2.0.0')
    
    # Dry run
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without doing it')
    
    test_args = [
        'data.csv',
        '--output', 'result.json',
        '--format', 'json',
        '--filter', 'age>18',
        '--filter', 'active=true',
        '--sort-by', 'name',
        '--limit', '100',
        '-vv'
    ]
    
    args = parser.parse_args(test_args)
    
    print(f"Input: {args.input_file}")
    print(f"Output: {args.output}")
    print(f"Format: {args.format}")
    print(f"Filters: {args.filter}")
    print(f"Sort by: {args.sort_by}")
    print(f"Limit: {args.limit}")
    print(f"Verbosity: {args.verbose}")
    print(f"Dry run: {args.dry_run}")


# ============================================================================
# Run all examples
# ============================================================================

if __name__ == '__main__':
    basic_example()
    type_conversion_example()
    validation_example()
    actions_example()
    choices_example()
    required_example()
    mutually_exclusive_example()
    subcommands_example()
    argument_groups_example()
    real_world_example()
    
    print("\n" + "="*60)
    print("All examples completed!")
    print("="*60)


