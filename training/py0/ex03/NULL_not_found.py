def NULL_not_found(object: any) -> int:
    
    if (type(object) == type(None)):
        print(f'Nothing:', end=' ')
    elif (type(object) == type(float("NaN"))):
        print('Cheese:', end=' ')
    elif (type(object) == type(0)):
        print('Zero:', end=' ')
    elif (type(object) == type("")):
        if (len(object) > 0):
            print("Type not found")
            return 2
        print('Empty:', end=' ')
    elif (type(object) == type(False)):
        print('Fake:', end=' ')
    else:
        print("Type not found")
        return 2
    print(f'{object} {type(object)}')
    return 0