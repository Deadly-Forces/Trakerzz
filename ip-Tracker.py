import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

ascii_banner = pyfiglet.figlet_format("IpTracker")
print(Fore.CYAN + ascii_banner)

# Main Script
import os
import requests
import socket 
from urllib.parse import urlparse

print(Fore.GREEN + "Welcome to IpTracker!")
print(Fore.YELLOW + "Type 'Show' to see the list of commands.")

def track():
    cmd = input(Fore.BLUE + "IpTracker >" + Style.RESET_ALL).strip().lower()
    if cmd == "help":
        print(Fore.YELLOW + "Available commands:")
        print(Fore.CYAN + "1. Show - Display this list of commands")
        print(Fore.CYAN + "2. IpTracker <IP/Domain> - Track the IP address or domain")
        print(Fore.CYAN + "3. Exit - Exit the program")
        track()
    elif cmd == "show":
        print(Fore.YELLOW + "Available commands:")
        print(Fore.CYAN + "1. IpTracker")
        print(Fore.CYAN + "2. help")
        print(Fore.CYAN + "3. Exit")
        track()
    elif cmd == "exit":
        print(Fore.RED + "Exiting the program.... \nGoodbye!")
        exit()
    elif cmd == "iptracker":
        print(Fore.MAGENTA + "Starting the tracker...")
        ip_or_url = input(Fore.BLUE + "Enter IP address or URL:" + Style.RESET_ALL)
        import socket
        from urllib.parse import urlparse

        def resolve_ip(input_str):
            if input_str.startswith("http://") or input_str.startswith("https://"):
                parsed_url = urlparse(input_str)
                hostname = parsed_url.hostname
            else:
                hostname = input_str
            try:
                ip_addr = socket.gethostbyname(hostname)
                return ip_addr
            except Exception as e:
                print(Fore.RED + f"Unable to resolve IP: {e}")
                return None

        ip = resolve_ip(ip_or_url)
        if not ip:
            print(Fore.RED + "Invalid IP or URL!")
            return

        def get_location(ip_address):
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

            location_data = {
                "Ip Address": ip_address,
                "city": response.get("city"),
                "region": response.get("region"),
                "country": response.get("country_name"),
                "Ip Address Type": response.get("version"),
                "Region Code": response.get("region_code"),
                "Postal Code": response.get("postal"),
                "Latitude": response.get(str("latitude")),
                "Longitude": response.get(str("longitude")),
                "TimeZone": response.get("timezone"),
                "Country code": response.get("country_calling_code"),
                "Country Area": response.get("country_area"),
                "Population": response.get("country_population"),
                "ASN": response.get("asn"),
                "Organization": response.get("org")
            }
            latitude = response.get("latitude")
            longitude = response.get("longitude")
            url = "https://google.com/maps/place/" + str(latitude) + "," + str(longitude) + "/@" + str(latitude) + "," + str(longitude) + ",16z"

            return location_data, url

        location_data, url = get_location(ip)
        print(Fore.GREEN + "Location Data:")
        for key, value in location_data.items():
            print(Fore.YELLOW + f"{key}: " + Fore.CYAN + f"{value}")
        print(Fore.MAGENTA + "You can view the location on Google Maps: " + Fore.BLUE + url)
        track()

track()
