import ft_package

print(ft_package)
print(ft_package.__name__)
print(ft_package.__doc__)

# print(ft_package.count_in_list(["this", "that", "what"]))

from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
