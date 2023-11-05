def count_in_list(lst: list, word: any):
    return len([i for i in lst if i == word])


print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
