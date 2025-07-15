from validator_collection import validators

my_email = input("What's your email address? ")

try:
    validators.email(my_email)
    print("Valid")
except ValueError:
    print("Invalid")
