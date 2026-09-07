def args_with_immutables(a, b, c):
    """Arguments are Passed Object-Reference.
    But the immutable objects reassignment created new object.
    The mutable eg. list, dict, set orginal are modified.
    """

    # Passed by reference
    print(f"in func arg a: {id(a)}: {a}")
    print(f"in func arg b: {id(b)}: {b}")
    print(f"in func arg c: {id(c)}: {c}")

    # Reassignment creates a new object
    c = a + b
    a = -10
    b = -20
    print(f"in func arg c, after reassignment: {id(c)}: {c}")
    print(f"in func arg a, after reassignment: {id(a)}: {a}")
    print(f"in func arg b, after reassignment: {id(b)}: {b}")
    return


def example_immutable_args():
    a, b, c = 10, 20, -100
    print(f"before the call, a: {id(a)}: {a}")
    print(f"before b: {id(b)}: {b}")
    print(f"before c: {id(c)}: {c}")
    args_with_immutables(a, b, c)
    print(f"after the call, a: {id(a)}: {a}")
    print(f"after the call, b: {id(b)}: {b}")
    print(f"after the call, c: {id(c)}: {c}")


if __name__ == "__main__":
    example_immutable_args()
