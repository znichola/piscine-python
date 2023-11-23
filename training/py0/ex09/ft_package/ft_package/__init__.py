def count_in_list(lst: list, word: any):
    '''count the number of occurrences of a thing from a list'''
    return len([i for i in lst if i == word])


# print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
# print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0

# https://py-pkgs.org/03-how-to-package-a-python#a-brief-introduction``
