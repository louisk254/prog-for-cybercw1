#import necessary modules
import random
import socket
from datetime import datetime

# Valid credentials
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"


def get_ip_address():
    #Get the IP address of this system, with a fallback if offline.
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except OSError:
        ip_address = "127.0.0.1"
    return ip_address


def create_event(username, event_type):
    #Build an event log entry as a dictionary.
    return {
        "event_id": random.randint(1000, 9999),
        "username": username,
        "ip_address": get_ip_address(),
        "event": event_type,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def print_event_log(events):
    #Print all recorded events in the required format.
    print("\nSECURITY EVENT LOG")
    print("==================")
    for e in events:
        print(f"Event ID: {e['event_id']}")
        print(f"Username: {e['username']}")
        print(f"IP Address: {e['ip_address']}")
        print(f"Event: {e['event']}")
        print(f"Timestamp: {e['timestamp']}")
        print()


def main():
    events = []
    logged_in = False
#while loop to prompt for username and password until correct credentials are provided.
    while not logged_in:
        username = input("Enter username: ")
        password = input("Enter password: ")
#Check if the provided credentials match the correct ones and log the event accordingly.
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            events.append(create_event(username, "Successful login"))
            logged_in = True
            print("Login successful!")
        else:
            events.append(create_event(username, "Failed login"))
            print("Invalid username or password. Try again.\n")

    print_event_log(events)


main()