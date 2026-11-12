
def create_sec_incident_record(username, ip_address, event_type, risk_level):
    # Create a dictionary with the provided information
    sec_incident_record = {
        "username": username,
        "ip_address": ip_address,
        "event_type": event_type,
        "risk_level": risk_level
    }
    return sec_incident_record

# Function to display the username and IP address from the security incident record
def display_username_ip(sec_incident_record):
    print(f"Username: {sec_incident_record['username']}")
    print(f"IP Address: {sec_incident_record['ip_address']}")

# Function to add a new field called status to the security incident record
def add_status_field(sec_incident_record, status):
    sec_incident_record["status"] = status
    print(f"Status field added with value: {status}")

# Function to update the risk level in the security incident record
def update_risk_level(sec_incident_record, new_risk_level):
    sec_incident_record["risk_level"] = new_risk_level
    print(f"Risk level updated to: {new_risk_level}")

# Function to remove a field from the security incident record
def remove_field(sec_incident_record, field):
    if field in sec_incident_record:
        del sec_incident_record[field]
        print(f"Field '{field}' removed from the security incident record.")
    else:
        print(f"Field '{field}' not found in the security incident record.")

# Function to display all remaining keys and values in the security incident record
def display_all_fields(sec_incident_record):    
    print("Remaining fields in the security incident record:")
    for key, value in sec_incident_record.items():
        print(f"{key}: {value}")

# Function to display the total number of key-value pairs in the security incident record
def display_total_fields(sec_incident_record):
    print(f"Total number of fields in the security incident record: {len(sec_incident_record)}")

def main():
    # Create a security incident record
    record = create_sec_incident_record("user123", "192.168.1.100", "Unauthorized Access", "High")
    
    # Display the username and IP address
    display_username_ip(record)
    
    # Add a new field called status
    add_status_field(record, "Open")
    
    # Update the risk level
    update_risk_level(record, "Critical")
    
    # Remove a field from the dictionary
    remove_field(record, "event_type")
    
    # Display all remaining keys and values
    display_all_fields(record)
    
    # Display the total number of key-value pairs
    display_total_fields(record)

if __name__ == "__main__":
    main()