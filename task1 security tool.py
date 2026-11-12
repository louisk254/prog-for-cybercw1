#importing the sys module to use sys.exit() for exiting the program
import sys
#defining the correct username and password for authentication
username = "Admin"
password = "Cyber123"

def menu():
    #displaying the main menu and prompting the user to choose a function
    print("Main Menu:")
    function_choice = input("Choose a function (1: Security Event Counter, 2: Brute Force Simulation, 3: Login Authentication, 4: Exit): ")
    while function_choice not in ("1", "2", "3", "4"):
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        function_choice = input("Choose a function (1: Security Event Counter, 2: Brute Force Simulation, 3: Login Authentication, 4: Exit): ")
#calling the appropriate function based on the user's choice
    if function_choice == "1":
        security_event_counter()
    elif function_choice == "2":
        brute_force_simulation()
    elif function_choice == "3":
        login_authentication()
    elif function_choice == "4":
        exit_program()

def security_event_counter():
    attempts = 0
#while loop to allow the user to attempt login up to 10 times
    while attempts < 10:
        input_username = input("Enter username: ")
        input_password = input("Enter password: ")
#checking if the entered username and password match the predefined ones
        if input_username == username and input_password == password:
            print("Authentication successful.")
            print("Number of failed attempts:", attempts)
            sec_end_choice = input("would you like to retry or exit to main menu? (retry/exit): ")
            if sec_end_choice.lower() == "retry":
                security_event_counter()
            elif sec_end_choice.lower() == "exit":
                menu()
            return
#if the username and password do not match, increment the attempts counter and provide feedback to the user
        attempts += 1
        if attempts == 6:
            print("alert attempts more than 50%")
        print("Incorrect username or password. Please try again.")
#if the user reaches the maximum number of attempts, provide an option to retry or exit to the main menu
        if attempts == 10:
            print("maximum attempts reached.")
            sec_end_choice = input("would you like to retry or exit to main menu? (retry/exit): ")
            if sec_end_choice.lower() == "retry":
                security_event_counter()
            elif sec_end_choice.lower() == "exit":
                menu()

def brute_force_simulation():
    attempts = 0
#while loop to allow the user to attempt login up to 10 times
    while attempts < 10:
        input_username = input("Enter username: ")
        input_password = input("Enter password: ")
#checking if the entered username and password match the predefined ones
        if input_username == username and input_password == password:
            print("Authentication successful.")
            print("Number of failed attempts:", attempts)
            sec_end_choice = input("would you like to retry or exit to main menu? (retry/exit): ")
            if sec_end_choice.lower() == "retry":
                brute_force_simulation()
            elif sec_end_choice.lower() == "exit":
                menu()
            return
#if the username and password do not match, increment the attempts counter and provide feedback to the user
        attempts += 1
        print("Incorrect username or password. Please try again.")
        if attempts == 10:
            print("maximum attempts reached.")
            sec_end_choice = input("would you like to retry or exit to main menu? (retry/exit): ")
            if sec_end_choice.lower() == "retry":
                brute_force_simulation()
            elif sec_end_choice.lower() == "exit":
                menu()

def login_authentication():
    log_ins = 0
#while loop to allow the user to attempt login up to 3 times
    while log_ins < 3:
        input_username = input("Enter username: ")
        input_password = input("Enter password: ")
#checking if the entered username and password match the predefined ones
        if input_username == username and input_password == password:
            print("Authentication successful.")
            sec_end_choice = input("would you like to retry or exit to main menu? (retry/exit): ")
            if sec_end_choice.lower() == "retry":
                login_authentication()
            elif sec_end_choice.lower() == "exit":
                menu()
            return
#if the username and password do not match, increment the log_ins counter and provide feedback to the user
        log_ins += 1
        print("Incorrect username or password. Please try again.")
    print("Too many failed attempts. Account is frozen for 24 hours.")
    sec_end_choice = input("would you like to retry or exit to main menu? (retry/exit): ")
    if sec_end_choice.lower() == "retry":
        brute_force_simulation()
    elif sec_end_choice.lower() == "exit":
        menu()

def exit_program():
    #prompt the user for confirmation before exiting the program
    should_exit = input("are you sure you want to exit? (yes/no): ")
    if should_exit.lower() == "yes":
        print("Exiting the program.")
        sys.exit()
    else:
        print("Returning to the main menu.")
        menu()

def main():
    #prompt the user for username and password for authentication
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    #while loop to keep prompting the user until the correct username and password are entered
    while input_username != username or input_password != password:
        print("Incorrect username or password. Please try again.")
        input_username = input("Enter username: ")
        input_password = input("Enter password: ")
    if input_username == username and input_password == password:
        print("Authentication successful.")
        print("Welcome to security tool.")
        menu()

            


if __name__ == "__main__":
    main()