import signal
import time
import sys
def handler(signum, frame):
    print(f"\nReceived signal {signum}. Exiting gracefully...")
    # Perform cleanup here
    sys.exit(0)
def main():
    # Register handler for Ctrl+C
    signal.signal(signal.SIGINT, handler)
    print("Running... Press Ctrl+C to stop.")
    while True:
        time.sleep(1)
        print(".", end="", flush=True)
if __name__ == "__main__":
    main()
