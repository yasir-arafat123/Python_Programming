"""Examples for pip configuration files."""

# Example pip.conf snippet
# [global]
# index-url = https://pypi.org/simple
# trusted-host = pypi.org

# Using environment variable to change cache dir
# PIP_CACHE_DIR=/path/to/cache python -m pip install requests

# TODO: document secure ways to store credentials (avoid plaintext in pip.conf).