import re

user_id_pattern = r'^[A-Z][A-Za-z0-9\-¬_@]{0,7}$'
password_pattern = r'^(?=.*\d)(?!.*\d.*\d)[A-Za-z0-9\-¬_@]+$'

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if re.fullmatch(user_id_pattern, userid):
    print("Valid User ID")
else:
    print("Invalid User ID")

if re.fullmatch(password_pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")
