my_dict = {"Ivan": "python",
           "Mary": "java",
           "Petro": "c++"
           }

for name, language in my_dict.items():
    print(f"{name} love {language.upper()}")


for number in range(1, 101):
    if number % 2 == 0:
        print(f"{number} - парне число")

    else:
        print(f"{number} - непарне число")