dict = {
    "Tushya":"12345678",
    "Tushya2":"87654321",
    "Tushya3":"qwertyui",
    "Tushya4":"iuytrewq",
    "Tushya5":"QWERTYUI",
    "Tushya6":"IUYTREWQ",
    "Tushya7":"password",
    "Tushya8":"PassWord",
    "Tushya9":"password123",
    "Tushya10":"PASSWORD"
}
inp = input("Enter your username: ")
if inp not in dict.keys():
    print("Username does not exist.")
elif inp in dict.keys():
    password = input("Enter your password: ")
    if dict[inp] != password:
        print("Wrong password.")
    elif dict[inp] == password:
        print("User logged in.")