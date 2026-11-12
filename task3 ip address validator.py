def validate_ip(ip_address):
    # Remove unnecessary spaces
    ip_address = ip_address.strip()
    
    # Check if the IP address contains exactly 3 periods/dots
    if ip_address.count('.') != 3:
        return False
    
    # Split the IP address into its numbers
    numbers = ip_address.split('.')
    
    # Check if we have exactly 4 numbers
    if len(numbers) != 4:
        return False
    
    # Check each number
    for number in numbers:
        # Check if the number is a valid integer
        if not number.isdigit():
            return False
        
        # Convert the number to an integer
        num = int(number)
        
        # Check if the number is within the valid range
        if num < 0 or num > 255:
            return False
    
    # If all checks pass, the IP address is valid
    return True

def main():
    ip_address = input("Enter an IP address: ")
    #Validate the IP address and print the result
    if validate_ip(ip_address):
        print(f"{ip_address} is a valid IP address.")
    else:
        print(f"{ip_address} is not a valid IP address.")

if __name__ == "__main__":
    main()