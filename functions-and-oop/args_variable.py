def mates(*args):
    """print list of names, arguments passed as tuple"""
    for idx, val in enumerate(args):
        print(f"[{idx}]: {val} or {args[idx]}")
    return


mates("KM", "AT", "NB")


def icons(members, *stars):
    """Add stars to members list."""
    for star in stars:
        members.append(star)
    return


holywood_stars = []
icons(
    holywood_stars,
    "Robert Downey Jr.",
    "Scarlett Johansson",
    "Samuel L. Jackson",
    "Zoe Saldaña",
    "Chris Pratt",
)
print(f"holywood stars: {holywood_stars}")


def prices(**items):
    """Keyword:Arguments passed as dictionary.
    Prints prices of {items} as dictionary."""
    for idx, item in enumerate(items):
        print(f"[{idx}] {item}: {items[item]}")
    return


# Print arguments as dictionary
prices(burger="$ 31.00", shake="$ 10.99", fries="$ 5.99")


def execute_sate(state: str, event: str, action: str):
    """prints arguments."""
    print(f"state: {state}, event: {event}, action: {action}")


state = {"state": "processing", "event": "deposit", "action": "add"}
execute_sate(**state)
print(f"annotations: {execute_sate.__annotations__}")


def combined_args(pos1, *args_tuple, pos2=5, **kwargs_dict):
    """Order matters. Tuple must be before tge keword argu ents"""
    print("Combined Arguments: ===>")
    print(f"pos1: {pos1}")
    print(f"tuple: {args_tuple}")
    print(f"pos2: {pos2}")
    print(f"dict: {kwargs_dict}")
    return


combined_args(10, 20, 30, 40, pos2=50, name="Joe", age=200, location="CA")
