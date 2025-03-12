"""
This module provides examples of exceptions.


Author: opendroid
Email: openweb@outlook.com
License: MIT
"""


def file_handling_exceptions(filename):
    """Reads a file with a int in a line. Raises exceptions. Note that how the
        file close() is getting handled."""
    print("file_handling_exceptions: ===>")
    try:
        f = open(filename, "r")
        line = f.readline()
        value = int(line.strip())
    except OSError as err:
        print(f"file_handling_exceptions: OS Error: {err}")
    except ValueError as err:
        print(f"file_handling_exceptions: Value error: {err}")
        f.close()
    else:  # If no exception is raised
        print(f"file_handling_exceptions: int read: {value}")
        f.close()
    finally:  # Executed all the time
        print(f"file_handling_exceptions: finally.")
    return


def file_handling_exceptions_with(filename):
    """with clause calls close on stream when done."""
    print("file_handling_exceptions_with: ===>")
    try:
        with open(filename, "r") as f:  # File is closed when with is done.
            try:
                line = f.readline()
                value = int(line.strip())
            except ValueError as err:
                print(f"file_handling_exceptions_with: Value error: {err}")
            else:  # If no exception is raised
                print(f"file_handling_exceptions_with: int read: {value}")
            finally:  # Executed all the time
                print("file_handling_exceptions_with: finally.")
    except OSError as err:
        print(f"file_handling_exceptions_with: OS Error: {err}")
    return


if __name__ == "__main__":
    file_handling_exceptions("./data/do_not_exist.txt")
    file_handling_exceptions("./data/string.txt")
    file_handling_exceptions("./data/int.txt")
    file_handling_exceptions_with("./data/do_not_exist.txt")
    file_handling_exceptions_with("./data/string.txt")
    file_handling_exceptions_with("./data/int.txt")
