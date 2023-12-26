from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

print("Testing error checking")
try:
    slice_me([[1, 3, 2], [1]], 0, 2)
except Exception as e:
    print("Caught:", e)

try:
    slice_me("not a list", 0, 2)
except Exception as e:
    print("Caught:", e)

try:
    slice_me(family, -9, 2)
except Exception as e:
    print("Caught:", e)
