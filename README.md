# RDP_Connection_Creator
Project Title: RDP Connection Creator

Description:
This Python script automates the creation of Remote Desktop Protocol (RDP) connections from IP addresses and usernames provided in a CSV file. It reads input from a CSV file containing IP addresses, usernames, and desired RDP file names, then generates corresponding RDP files with specified settings. Each RDP file prompts for credentials and has display settings set to "High Color (16 bit)" by default. Additionally, the script appends a domain name ("test.com") to all usernames. The generated RDP files are saved in a folder named "RDP_Connections".

Features:

Parses input data from a CSV file to create RDP connections.
Sets display settings to "High Color (16 bit)" and prompts for credentials in each RDP file.
Appends a domain name to all usernames for authentication.
Organizes generated RDP files into a dedicated folder.

Usage:

Prepare a CSV file with IP addresses, usernames, and desired RDP file names.
Run the script, which will read the CSV file and generate corresponding RDP files.
Find the generated RDP files inside the "RDP_Connections" folder.
Requirements:

Python 3.x
CSV file containing IP addresses, usernames, and RDP file names
Author:
[Sanka Soysa]
