while True:
    user_input = input("What's your name? ")

    if user_input == "":
        print("OK")
        break

    print(f"Hello, {user_input}")

    with open("guest_book.txt", "a") as file_object:
        file_object.write(f"{user_input}\n")