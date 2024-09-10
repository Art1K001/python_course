from admin import Admin

my_admin = Admin("Denys", "penys", 22, "masturbation", "panda kung fu")
my_admin.describe_user()
my_admin.greet_user()
print("Now you are admin so you can do:")
my_admin.privileges.show_privileges()