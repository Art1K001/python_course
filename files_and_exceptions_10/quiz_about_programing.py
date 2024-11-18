while True:
    user_input = input("What you like in programing? ")

    if user_input == "":
        print("Thank's for you answer")
        break

    with open("quiz_about_programing.txt", "a") as file_object:
        file_object.write(f"{user_input}\n")