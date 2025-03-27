def args_with_list(places, *capitals):
    """Add capitals to places list. 'capitals are passed as a tuple'"""

    print(f"args_with_list: places:{type(places)}, id: {id(places)}")
    print(f"args_with_list: capitals:{type(capitals)}, id: {id(capitals)}")

    for capital in capitals:
        places.append(capital)
    return


def example_args_with_list():
    print("example1_args_with_list: ===>")
    places = []
    args_with_list(places, "Abuja", "Accra", "Bamako", "Cairo")
    print(f"example1_args_with_list: places: {places}")
    return


if __name__ == "__main__":
    example_args_with_list()
