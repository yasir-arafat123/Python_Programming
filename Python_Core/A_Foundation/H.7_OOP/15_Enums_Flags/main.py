from enum import Enum, auto, Flag, IntEnum
class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    COMPLETED = auto()
    FAILED = auto()
class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
    ALL = READ | WRITE | EXECUTE
def check_status(s: Status):
    if s == Status.COMPLETED:
        print("Job done!")
    elif s == Status.FAILED:
        print("Job failed.")
    else:
        print("Still working...")
def main():
    # Basic Enum
    current = Status.RUNNING
    print(f"Current: {current} (name={current.name}, value={current.value})")
    check_status(current)
    # Flags
    user_perms = Permission.READ | Permission.WRITE
    print(f"User perms: {user_perms}")
    if Permission.WRITE in user_perms:
        print("User can write")
    if Permission.EXECUTE not in user_perms:
        print("User cannot execute")
if __name__ == "__main__":
    main()
