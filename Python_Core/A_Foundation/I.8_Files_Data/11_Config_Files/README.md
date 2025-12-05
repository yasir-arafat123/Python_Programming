# Config Files

## Overview

Configuration files are essential for managing application settings, preferences, and environment-specific parameters. Python provides several approaches for handling configuration data, from traditional INI files to modern TOML format.

## Core Things to Learn

### 1. configparser - INI File Format
- Reading and writing INI files (`.ini`, `.cfg`)
- Sections, options (keys), and values
- Default values and fallback mechanisms
- Type conversion: `getint()`, `getfloat()`, `getboolean()`
- Variable interpolation (substituting values)
- Case sensitivity handling

### 2. INI File Structure
```ini
[Section1]
key1 = value1
key2 = value2

[Section2]
# Comments start with # or ;
option1 = 123
option2 = true
```

### 3. Modern Alternatives

**TOML (recommended for new projects)**
```python
import tomli  # Python 3.11+: tomllib (built-in)
with open('config.toml', 'rb') as f:
    config = tomli.load(f)
```

**Environment Variables**
```python
import os
from pathlib import Path

# Best practice: use .env files with python-dotenv
DATABASE_URL = os.getenv('DATABASE_URL', 'default_value')
```

**JSON/YAML** (covered in other modules)
- JSON: Native Python support, no comments
- YAML: Requires `pyyaml`, more human-readable

## Python Libraries

| Library | Purpose | Built-in? |
|---------|---------|-----------|
| `configparser` | INI files | ✅ Yes |
| `tomllib` (3.11+) | TOML reading | ✅ Yes (Python 3.11+) |
| `tomli` / `toml` | TOML (older Python) | ❌ No (`pip install tomli`) |
| `python-dotenv` | `.env` files | ❌ No (`pip install python-dotenv`) |
| `json` | JSON files | ✅ Yes |
| `pyyaml` | YAML files | ❌ No |

## Common Use Cases

1. **Application settings** (database URLs, API keys, feature flags)
2. **User preferences** (theme, language, default paths)
3. **Environment-specific config** (dev, staging, production)
4. **Plugin configuration**
5. **Deployment settings** (ports, hostnames, timeouts)

## Best Practices

1. **Never commit secrets** - Use environment variables for sensitive data
2. **Provide defaults** - Use `config.get(section, option, fallback='default')`
3. **Validate early** - Check config on startup, fail fast with clear errors
4. **Document your config** - Add comments explaining each option
5. **Use appropriate format**:
   - INI: Simple key-value pairs, legacy compatibility
   - TOML: Modern Python projects (PEP 518, used by Poetry/Hatch)
   - YAML: Complex nested structures, DevOps tools
   - Environment variables: Secrets, containerized deployments

## Configuration Hierarchy (12-Factor App)

**Priority order** (highest to lowest):
1. Command-line arguments (`--config-path`)
2. Environment variables (`APP_DATABASE_URL`)
3. Config file (`.env`, `config.toml`)
4. Default values (hardcoded in code)

## Example Workflow

```python
# 1. Load config file
config = load_config('app.toml')

# 2. Override with environment variables
config['database_url'] = os.getenv('DATABASE_URL', config['database_url'])

# 3. Override with CLI args
if args.database_url:
    config['database_url'] = args.database_url

# 4. Validate
validate_config(config)
```

## References

- [configparser docs](https://docs.python.org/3/library/configparser.html)
- [TOML specification](https://toml.io/)
- [The Twelve-Factor App - Config](https://12factor.net/config)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- Python roadmap — https://roadmap.sh/python

## Related Topics

- `I.8/3_JSON` - JSON configuration files
- `I.8/7_XML_YAML` - YAML configuration
- `R.17_Security/04_Secrets_Management` - Handling sensitive data
- `Real_World_Applications/05_CLI_Development` - CLI argument parsing
- `Real_World_Applications/03_Deployment` - Environment configuration


