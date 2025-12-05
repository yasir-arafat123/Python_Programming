"""Examples for Config Files - configparser module."""

import configparser
import os
from pathlib import Path
from io import StringIO


# ============================================================================
# Example 1: Basic INI File Operations
# ============================================================================

def basic_config_example():
    """Read and write INI configuration files."""
    print("=== Basic Config Operations ===\n")
    
    # Create config
    config = configparser.ConfigParser()
    
    # Add sections and options
    config['DEFAULT'] = {
        'ServerAliveInterval': '45',
        'Compression': 'yes',
        'CompressionLevel': '9'
    }
    
    config['forge.example'] = {}
    config['forge.example']['User'] = 'hg'
    
    config['topsecret.server.example'] = {}
    topsecret = config['topsecret.server.example']
    topsecret['Port'] = '50022'
    topsecret['ForwardX11'] = 'no'
    
    # Write to file
    with open('example.ini', 'w') as configfile:
        config.write(configfile)
    
    print("Config written to example.ini")
    
    # Read from file
    config_read = configparser.ConfigParser()
    config_read.read('example.ini')
    
    print(f"Sections: {config_read.sections()}")
    print(f"forge.example user: {config_read['forge.example']['User']}")
    print(f"topsecret port: {config_read['topsecret.server.example']['Port']}")
    
    # Clean up
    os.remove('example.ini')


# ============================================================================
# Example 2: Type Conversion
# ============================================================================

def type_conversion_example():
    """Use getint(), getfloat(), getboolean() for type conversion."""
    print("\n=== Type Conversion ===\n")
    
    config = configparser.ConfigParser()
    config.read_string("""
    [database]
    host = localhost
    port = 5432
    max_connections = 100
    timeout = 30.5
    ssl_enabled = yes
    auto_reconnect = no
    """)
    
    db = config['database']
    
    # String (default)
    host = db.get('host')
    print(f"Host: {host} (type: {type(host).__name__})")
    
    # Integer
    port = db.getint('port')
    print(f"Port: {port} (type: {type(port).__name__})")
    
    # Float
    timeout = db.getfloat('timeout')
    print(f"Timeout: {timeout} (type: {type(timeout).__name__})")
    
    # Boolean (yes/no, true/false, on/off, 1/0)
    ssl = db.getboolean('ssl_enabled')
    reconnect = db.getboolean('auto_reconnect')
    print(f"SSL: {ssl} (type: {type(ssl).__name__})")
    print(f"Auto-reconnect: {reconnect}")


# ============================================================================
# Example 3: Default Values and Fallback
# ============================================================================

def fallback_example():
    """Handle missing options with fallback values."""
    print("\n=== Fallback Values ===\n")
    
    config = configparser.ConfigParser()
    config.read_string("""
    [app]
    name = MyApp
    debug = false
    """)
    
    app = config['app']
    
    # Option exists
    name = app.get('name', fallback='DefaultApp')
    print(f"App name: {name}")
    
    # Option missing - use fallback
    version = app.get('version', fallback='1.0.0')
    print(f"Version: {version}")
    
    # Type conversion with fallback
    max_users = app.getint('max_users', fallback=100)
    print(f"Max users: {max_users}")
    
    # Boolean with fallback
    debug = app.getboolean('debug', fallback=True)
    print(f"Debug mode: {debug}")


# ============================================================================
# Example 4: Interpolation (Variable Substitution)
# ============================================================================

def interpolation_example():
    """Use variable interpolation in config values."""
    print("\n=== Variable Interpolation ===\n")
    
    # Basic interpolation
    config = configparser.ConfigParser()
    config.read_string("""
    [paths]
    home = /home/user
    data = %(home)s/data
    logs = %(home)s/logs
    cache = %(data)s/cache
    """)
    
    paths = config['paths']
    print(f"Home: {paths['home']}")
    print(f"Data: {paths['data']}")
    print(f"Logs: {paths['logs']}")
    print(f"Cache: {paths['cache']}")
    
    # Extended interpolation (allows ${section:option})
    config_ext = configparser.ConfigParser(
        interpolation=configparser.ExtendedInterpolation()
    )
    config_ext.read_string("""
    [paths]
    home = /home/user
    
    [database]
    data_dir = ${paths:home}/db
    backup_dir = ${paths:home}/backups
    """)
    
    print(f"\nDatabase dir: {config_ext['database']['data_dir']}")
    print(f"Backup dir: {config_ext['database']['backup_dir']}")


# ============================================================================
# Example 5: Multi-line Values
# ============================================================================

def multiline_example():
    """Handle multi-line configuration values."""
    print("\n=== Multi-line Values ===\n")
    
    config = configparser.ConfigParser()
    config.read_string("""
    [app]
    description = This is a long description
        that spans multiple lines
        and preserves indentation
    
    allowed_hosts = 
        localhost
        example.com
        api.example.com
    
    sql_query = 
        SELECT * FROM users
        WHERE active = true
        ORDER BY created_at DESC
    """)
    
    app = config['app']
    print("Description:")
    print(app['description'])
    
    print("\nAllowed hosts:")
    hosts = [h.strip() for h in app['allowed_hosts'].split('\n') if h.strip()]
    for host in hosts:
        print(f"  - {host}")


# ============================================================================
# Example 6: Real-World Application Config
# ============================================================================

def application_config_example():
    """Complete application configuration example."""
    print("\n=== Application Config ===\n")
    
    # Create comprehensive config
    config = configparser.ConfigParser()
    
    # Application settings
    config['app'] = {
        'name': 'DataProcessor',
        'version': '2.1.0',
        'debug': 'false',
        'log_level': 'INFO'
    }
    
    # Database configuration
    config['database'] = {
        'host': 'localhost',
        'port': '5432',
        'name': 'mydb',
        'user': 'dbuser',
        'pool_size': '10',
        'timeout': '30.0'
    }
    
    # API settings
    config['api'] = {
        'base_url': 'https://api.example.com',
        'timeout': '15',
        'retries': '3',
        'rate_limit': '100'
    }
    
    # Feature flags
    config['features'] = {
        'enable_caching': 'yes',
        'enable_analytics': 'yes',
        'enable_beta_features': 'no'
    }
    
    # Write config
    with open('app_config.ini', 'w') as f:
        config.write(f)
    
    # Read and use config
    app_config = configparser.ConfigParser()
    app_config.read('app_config.ini')
    
    # Extract values
    app_name = app_config['app']['name']
    db_host = app_config['database']['host']
    db_port = app_config['database'].getint('port')
    caching = app_config['features'].getboolean('enable_caching')
    
    print(f"App: {app_name}")
    print(f"Database: {db_host}:{db_port}")
    print(f"Caching enabled: {caching}")
    
    # Clean up
    os.remove('app_config.ini')


# ============================================================================
# Example 7: Environment Variables Override
# ============================================================================

def env_override_example():
    """Combine config file with environment variable overrides."""
    print("\n=== Config with Env Override ===\n")
    
    config = configparser.ConfigParser()
    config.read_string("""
    [database]
    host = localhost
    port = 5432
    user = defaultuser
    """)
    
    # Override with environment variables
    db_host = os.getenv('DB_HOST', config['database']['host'])
    db_port = int(os.getenv('DB_PORT', config['database']['port']))
    db_user = os.getenv('DB_USER', config['database']['user'])
    
    print(f"Database connection:")
    print(f"  Host: {db_host}")
    print(f"  Port: {db_port}")
    print(f"  User: {db_user}")
    
    # Set env var to test override
    os.environ['DB_HOST'] = 'production.example.com'
    db_host_override = os.getenv('DB_HOST', config['database']['host'])
    print(f"\nWith DB_HOST env var: {db_host_override}")
    
    # Clean up
    del os.environ['DB_HOST']


# ============================================================================
# Example 8: Configuration Validation
# ============================================================================

def validation_example():
    """Validate configuration values on load."""
    print("\n=== Config Validation ===\n")
    
    def validate_config(config):
        """Validate required config options."""
        errors = []
        
        # Check required sections
        required_sections = ['app', 'database']
        for section in required_sections:
            if not config.has_section(section):
                errors.append(f"Missing required section: {section}")
        
        # Check required options
        if config.has_section('app'):
            if not config.has_option('app', 'name'):
                errors.append("Missing app.name")
        
        if config.has_section('database'):
            # Validate port range
            try:
                port = config.getint('database', 'port')
                if not 1 <= port <= 65535:
                    errors.append(f"Invalid port: {port}")
            except ValueError as e:
                errors.append(f"Invalid port value: {e}")
        
        return errors
    
    # Valid config
    valid_config = configparser.ConfigParser()
    valid_config.read_string("""
    [app]
    name = MyApp
    
    [database]
    host = localhost
    port = 5432
    """)
    
    errors = validate_config(valid_config)
    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("✓ Configuration is valid")
    
    # Invalid config
    invalid_config = configparser.ConfigParser()
    invalid_config.read_string("""
    [app]
    version = 1.0
    
    [database]
    host = localhost
    port = 99999
    """)
    
    errors = validate_config(invalid_config)
    print("\nInvalid config errors:")
    for error in errors:
        print(f"  - {error}")


# ============================================================================
# Run all examples
# ============================================================================

if __name__ == '__main__':
    basic_config_example()
    type_conversion_example()
    fallback_example()
    interpolation_example()
    multiline_example()
    application_config_example()
    env_override_example()
    validation_example()
    
    print("\n" + "="*60)
    print("All examples completed!")
    print("="*60)
