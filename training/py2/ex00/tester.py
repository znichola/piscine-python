from load_csv import load

print("Valid File")
print(load("../doc/life_expectancy_years.csv"))
print("Valid Url")
url = "https://cdn.intra.42.fr/document/document/15948/population_total.csv"
print(load(url))

print("\nError tests")
print(load("not_found.csv"))
print(load("https://cdn.intra.42.fr/document/document/15948/not_found.csv"))
print(load(str))
