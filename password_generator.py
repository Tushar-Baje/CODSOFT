import random

def create_pass(length):
    random_string=""
    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$@&#"
    for i in range(length):
        random_string+=random.choice(chars)
    print(f"Here's your password:{random_string}")
    

print("***Password Generator***")
print("\n")
while True:
    ans=input("Do you want to generate a password Yes or No ")
    ans=ans.lower()
    if ans == 'yes':
        length=input("Enter the desired length of the password you require ")
        length=int(length)
        create_pass(length)
    else:
        print("Thank You!")
        break

