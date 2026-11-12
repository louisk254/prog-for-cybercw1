#imports the security_tools.py file
import security_tools
#asks user for a password and an IP address
password = input("Enter a password: ")
ip_address = input("Enter an IP address: ")
#validates the password using the functions from security_tools.py
if not security_tools.password_validation(password):
    print("The provided password is not strong.")
    generated_password = security_tools.generate_strong_random_password()
    print(f"Here is a suggested strong password: {generated_password}")
else:
    print("The provided password is strong.")
#validates the IP address using the functions from security_tools.py
if not security_tools.ip_address_validation(ip_address):
    print("The provided IP address is not valid.")
else:
    print("The provided IP address is valid.")
