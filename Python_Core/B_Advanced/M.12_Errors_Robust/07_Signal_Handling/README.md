# Signal Handling
Purpose: Handling asynchronous events like Ctrl+C (SIGINT) or termination requests (SIGTERM).
## Key Concepts
- \signal\ module
- \signal.signal(signal.SIGINT, handler)\
- Graceful shutdown patterns
- Windows vs Unix differences (Windows has limited signals)
## Why it matters
- Ensuring cleanup (closing files/DBs) when a user cancels a script.
- Preventing data corruption during forced stops.
