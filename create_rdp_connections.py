import csv
import os

def create_rdp(ip_address, username, rdp_file_name):
    # Adding domain name to username
    username_with_domain = f"{username}@test.com"

    rdp_content = f"""\
full address:s:{ip_address}
username:s:{username_with_domain}
screen mode id:i:2
authentication level:i:2
prompt for credentials:i:1
session bpp:i:16  # Setting color depth to 16-bit
"""

    # Creating RDP file
    with open(os.path.join("RDP_Connections", f"{rdp_file_name}.rdp"), "w") as rdp_file:
        rdp_file.write(rdp_content)

def main():
    csv_file = 'connections.csv'  # Change this to your CSV file path

    # Create folder for RDP files
    os.makedirs("RDP_Connections", exist_ok=True)

    # Reading CSV and creating RDP connections
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            ip_address = row['IP_Address']
            username = row['Username']
            rdp_file_name = row['RDP_File_Name']

            create_rdp(ip_address, username, rdp_file_name)
            print(f"RDP connection '{rdp_file_name}' created successfully!")

if __name__ == "__main__":
    main()
