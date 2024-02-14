from load_image import ft_load

print(ft_load("../doc/landscape.jpg"))

try:
    print(ft_load("../doc/notfound.jpg"))
except Exception as e:
    print(f"caught the oopsi: {e}")
