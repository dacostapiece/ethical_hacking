#you can pass the top-level domain for querying as args like
#python subdomain_enumeration.py example.com
#or call it without args
#python subdomain_enumeration.py
#code will request you to input it

import requests
import sys

# Check if the domain argument is provided
if len(sys.argv) < 2:
    # Prompt the user to input the domain if not provided
    top_level_domain = input("Please enter the top-level domain (e.g., example.com): ").strip()
else:
    # Extract the top-level domain from arguments
    top_level_domain = sys.argv[1]

# Read subdomains from file
try:
    with open("subdomains.txt") as file:
        sub_list = file.read()
except FileNotFoundError:
    print("Error: 'subdomains.txt' file not found. Please make sure the file exists in the same directory as this script.")
    sys.exit(1)

subdoms = sub_list.splitlines()

for sub in subdoms:
    # Form the full subdomain URL
    sub_domains = f"http://{sub}.{top_level_domain}"
    try:
        # Make a request to the subdomain
        requests.get(sub_domains)
    except requests.ConnectionError:
        # Skip if the connection fails
        pass
    else:
        print("Valid domain: ", sub_domains)
