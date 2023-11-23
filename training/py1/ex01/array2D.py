def slice_me(family: list, start: int, end: int) -> list:
    '''2D array slicer'''

    if not isinstance(family, list):
        raise ValueError("Family is not a list")
    sub_size = len(family[0]) if family else 0
    if not all(len(sublist) == sub_size for sublist in family):
        raise ValueError("Irregularly shaped list")

    print(f"My shape is: ({len(family)}, {sub_size})")

    trunc = family[start:end]

    sub_size = len(trunc[0]) if trunc else 0
    print(f"My new shape is: ({len(trunc)}, {sub_size})")

    return trunc
