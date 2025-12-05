import random
import secrets
def main():
    # Basic randoms
    print(f"Float [0.0, 1.0): {random.random()}")
    print(f"Int [1, 10]: {random.randint(1, 10)}")
    print(f"Range [0, 100, 5]: {random.randrange(0, 100, 5)}")
    # Sequences
    colors = ['red', 'green', 'blue', 'yellow']
    print(f"Choice: {random.choice(colors)}")
    print(f"Sample (2 unique): {random.sample(colors, k=2)}")
    random.shuffle(colors)
    print(f"Shuffled: {colors}")
    # Weighted choices
    # 50% red, 10% others
    weights = [50, 10, 10, 10] 
    # Note: weights length must match population, this is just a demo
    # Secure randoms
    print(f"Secure token: {secrets.token_hex(16)}")
if __name__ == "__main__":
    main()
