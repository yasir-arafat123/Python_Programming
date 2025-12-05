# 01 argparse Basics

## Overview

`argparse` is Python's built-in module for parsing command-line arguments. It provides a robust, user-friendly way to build CLI tools with automatic help generation, type conversion, and error handling.

## Core Things to Learn

### 1. Basic Argument Parser

```python
import argparse

parser = argparse.ArgumentParser(description='Process some data')

# Positional argument (required)
parser.add_argument('filename', help='Input file to process')

# Optional argument with flag
parser.add_argument('--verbose', '-v', action='store_true',
                   help='Enable verbose output')

# Optional argument with value
parser.add_argument('--output', '-o', default='output.txt',
                   help='Output file (default: output.txt)')

args = parser.parse_args()
print(f"Processing {args.filename}")
```

### 2. Argument Types

```python
parser.add_argument('count', type=int, help='Number of items')
parser.add_argument('--ratio', type=float, default=0.5)
parser.add_argument('--config', type=Path, help='Config file path')

# Custom type validation
def port_number(value):
    port = int(value)
    if not 1 <= port <= 65535:
        raise argparse.ArgumentTypeError(f"{port} is not a valid port")
    return port

parser.add_argument('--port', type=port_number, default=8080)
```

### 3. Actions

```python
# store (default) - Store the value
parser.add_argument('--name', action='store')

# store_true/store_false - Boolean flags
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--no-cache', action='store_true')

# store_const - Store constant value
parser.add_argument('--debug', action='store_const', const=10)

# append - Collect multiple values
parser.add_argument('--include', action='append')
# Usage: --include dir1 --include dir2

# count - Count occurrences
parser.add_argument('-v', action='count', default=0)
# Usage: -vvv (verbosity = 3)
```

### 4. Choices and Constraints

```python
# Restrict to specific values
parser.add_argument('--format', choices=['json', 'xml', 'yaml'])

# Number range
parser.add_argument('--threads', type=int, choices=range(1, 9))

# Required optional argument
parser.add_argument('--api-key', required=True)

# Mutually exclusive arguments
group = parser.add_mutually_exclusive_group()
group.add_argument('--json', action='store_true')
group.add_argument('--xml', action='store_true')
```

### 5. Subcommands (like git)

```python
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command', help='Available commands')

# git commit subcommand
commit_parser = subparsers.add_parser('commit', help='Commit changes')
commit_parser.add_argument('-m', '--message', required=True)
commit_parser.add_argument('--amend', action='store_true')

# git push subcommand
push_parser = subparsers.add_parser('push', help='Push changes')
push_parser.add_argument('remote', default='origin')
push_parser.add_argument('branch', default='main')

args = parser.parse_args()
if args.command == 'commit':
    print(f"Committing: {args.message}")
elif args.command == 'push':
    print(f"Pushing to {args.remote}/{args.branch}")
```

## Common Use Cases

1. **Script configuration** (input/output files, processing options)
2. **CLI tools** (database migrations, build tools, deployment scripts)
3. **Data processing pipelines** (ETL scripts, batch processors)
4. **Server management** (start/stop services, configuration)
5. **Development tools** (code generators, test runners)

## Best Practices

### 1. Provide Good Help Messages
```python
parser = argparse.ArgumentParser(
    description='Download and process website data',
    epilog='Example: %(prog)s https://example.com --format json'
)

parser.add_argument('url', help='Website URL to scrape')
parser.add_argument('--format', choices=['json', 'csv', 'xml'],
                   default='json',
                   help='Output format (default: %(default)s)')
```

### 2. Use Argument Groups for Organization
```python
# Input options
input_group = parser.add_argument_group('input options')
input_group.add_argument('--file', help='Input file')
input_group.add_argument('--stdin', action='store_true')

# Output options
output_group = parser.add_argument_group('output options')
output_group.add_argument('--output', help='Output file')
output_group.add_argument('--format', choices=['json', 'xml'])
```

### 3. Set Defaults and Validate
```python
parser.add_argument('--timeout', type=int, default=30,
                   help='Request timeout in seconds (default: %(default)s)')

args = parser.parse_args()

# Additional validation
if args.timeout < 1:
    parser.error("Timeout must be at least 1 second")
```

### 4. Support Version Flag
```python
parser.add_argument('--version', action='version', version='%(prog)s 2.0')
```

## Common Patterns

### Configuration File + CLI Override
```python
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--config', type=Path, default='config.json')
parser.add_argument('--host', help='Override config host')
parser.add_argument('--port', type=int, help='Override config port')

args = parser.parse_args()

# Load config file
config = json.loads(args.config.read_text())

# Override with CLI args
if args.host:
    config['host'] = args.host
if args.port:
    config['port'] = args.port
```

### Verbose Levels
```python
parser.add_argument('-v', '--verbose', action='count', default=0,
                   help='Increase verbosity (-v, -vv, -vvv)')

args = parser.parse_args()

# Configure logging based on verbosity
if args.verbose == 0:
    log_level = logging.WARNING
elif args.verbose == 1:
    log_level = logging.INFO
else:
    log_level = logging.DEBUG
```

### Dry Run Mode
```python
parser.add_argument('--dry-run', action='store_true',
                   help='Show what would be done without doing it')

args = parser.parse_args()

if args.dry_run:
    print(f"Would process {args.file}")
else:
    process_file(args.file)
```

## Alternatives

- **click** - Decorator-based, more Pythonic
- **typer** - Based on type hints, modern approach
- **docopt** - Define CLI via docstring
- **fire** - Automatically generate CLI from functions

## References

- [argparse docs](https://docs.python.org/3/library/argparse.html)
- [argparse tutorial](https://docs.python.org/3/howto/argparse.html)
- Python roadmap — https://roadmap.sh/python

## Related Topics

- `I.8/11_Config_Files` - Configuration file parsing
- `Real_World_Applications/05_CLI_Development/02_click_vs_typer` - Modern alternatives
- `Real_World_Applications/05_CLI_Development/03_Command_Structure_subcommands` - Complex CLI design
- `N.13_Logging_Obs` - Logging based on CLI flags

