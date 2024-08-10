def email(name):
    return (name +"@gmail.com")

Name=input("Enter yout FullName:")
Name=Name.lower()
Name=Name.replace(" ","")


print("Your Email is="+email(Name))