import inspect
def my_func(a: int, b: str = "default"):
    """Docstring here."""
    return a
def main():
    # Inspect signature
    sig = inspect.signature(my_func)
    print(f"Signature: {sig}")
    print(f"Params: {list(sig.parameters.keys())}")
    # Get source
    print(f"Source:\n{inspect.getsource(my_func)}")
    # Check type
    print(f"Is function? {inspect.isfunction(my_func)}")
if __name__ == "__main__":
    main()
