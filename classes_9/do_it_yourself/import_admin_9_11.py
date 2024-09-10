from privileges_9_8 import Admin

admistrator = Admin("Oleh", "Dido", 87, "Hobby Horsing", "dildohod")
admistrator.describe_user()
admistrator.greet_user()
print("Admin's privigeles: ")
admistrator.privileges.show_privileges()