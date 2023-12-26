ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "Switzerland!")
ft_set.remove("tutu!")
ft_set.update({"Lausanne!"})
ft_dict["Hello"] = "42Lausanne!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)