def all_thing_is_obj(object: any) -> int:
    #my code
    if (type(object) == type("Brian")):
        print(f'Brian is in the kitchen : {type(object)}')
    elif (type(object) == type(10)):
        print("Type not found")
    else: 
        print(f'{type(object).__name__.capitalize()} : {type(object)}')
    return 42