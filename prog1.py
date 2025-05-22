print("Welcome to our Chatbot")
print("Our Chatbot will collect some information to grant you access.")

wrong_name = True

while wrong_name == True:
    name = str(input("Enter your name :"))
    if (len(name) >= 5 and len(name) < 30):
        wrong_name = False
    else:
        print("Name should be minimum 5 letters and maximum should be 30 letters")

wrong_age =  True

while wrong_age == True:
    age = int(input("Enter your age :"))
    if age >= 12 and age < 80:
        wrong_age = False
    else:
        print("Age should be minimum 12 years and maximum should be 80 years")

username = str(input("Enter Username :"))

mismatch = True

while mismatch == True:
    password = str(input("Enter Password :"))
    re_password = str(input("Please re-enter password for conformaition :"))
    if password == re_password:
        mismatch = False
    else:
        print("Password should be same")

print("ACCESS GRANTED")