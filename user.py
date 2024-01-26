user_info = {}

user_info["Name"] = input("What is the user's name? ")
user_info["Age"] = input("What is the user's age? ")
user_info["Birth_country"] = input("What is the user's country of birth? ")
user_info["Known_for"] = input("What is the user known for? ")

print("\nUser Information:")
for key, value in user_info.items():
    print(f"{key}: {value}")