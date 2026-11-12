import random
import string


def password_validation(password):
    #Validates the given password based on specific criteria.
    # Check for minimum length
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Check for at least one special character
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if not any(char in special_characters for char in password):
        return False
    
    return True

def ip_address_validation(ip_address):
    #Validates the given IP address based on specific criteria.
    # Split the IP address into its components
    parts = ip_address.split('.')

    #checkif there is exactly 3 periods/dots
    if ip_address.count('.') != 3:
        return False
    
    # Check if there are exactly 4 parts
    if len(parts) != 4:
        return False
    
    for part in parts:
        # Check if each part is a digit
        if not part.isdigit():
            return False
        
        # Convert part to integer and check if it's in the valid range
        num = int(part)
        if num < 0 or num > 255:
            return False
    
    return True

def generate_strong_random_password(length=12):
    #Generates a strong random password of the specified length.
    if length < 10:
        raise ValueError("Password length should be at least 10 characters.")
    
    if length > 16:
        raise ValueError("Password length should not exceed 16 characters.")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    
    # Ensure the password has at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password length with random choices from all sets
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password list to ensure randomness and convert to string
    random.shuffle(password)
    
    return ''.join(password)