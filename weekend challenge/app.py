# Prompt the user for input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email address: ")
phone_number = input("Enter your phone number: ")
location = input("Enter your location: ")

# Create a list of inputs
user_info = [first_name, last_name, email, phone_number, location]

# Print the list of inputs
print("User Information:")
for info in user_info:
    print(info)
