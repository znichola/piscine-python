from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))


print("Testing exception catching")
try:
    give_bmi(["foobar", 123], weight)
except Exception as e:
    print("Caught:", e)

try:
    give_bmi(height, ["foobar", 123])
except Exception as e:
    print("Caught:", e)

try:
    give_bmi([2, 123,  0.99, .9], weight)
except Exception as e:
    print("Caught:", e)
