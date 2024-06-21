def mates(*args):
    """print list of names"""
    for idx, val in enumerate(args):
        print(f"[{idx}]: {val}")
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
    """Prints prices of {items} as dictionary."""
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
