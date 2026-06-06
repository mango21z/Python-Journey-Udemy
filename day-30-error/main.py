#FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdg"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("the file has been closed")
#     raise TypeError("thisi is the code i made up")


height = float(input("height:"))
weight = float(input("wight:"))

if height>3:
    raise ValueError("human hight should be more than 3m")
bmi = weight/height**2



