#!/usr/bin/env python3
import sys
import requests
import argparse
from colorama import init, Fore, Style

init(autoreset=True)

BANNER = f'''
{Fore.CYAN}   _  __________                 
  | |/_/ __/ __/______  ___  ___ 
 _>  <_\ \_\ \/ __/ _ \/ _ \/ -_)
/_/|_/___/___/\__/\___/ .__/\__/ 
                     /_/           
-------------------------------------
 {Fore.GREEN}[*] Developed by GH0STH4CKER
--------------------------------------
{Style.RESET_ALL}
'''

API_ENDPOINT = "https://check4xss.vercel.app/check_xss?url="

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.RequestException:
        return False

def extract_search_url(html):
    """
    Extract the Search URL from API HTML response.
    Looks for <p><strong>Search URL:</strong> ... </p>
    """
    marker = "<strong>Search URL:</strong>"
    start = html.find(marker)
    if start == -1:
        return None
    start += len(marker)
    end = html.find("</p>", start)
    if end == -1:
        return None
    snippet = html[start:end].strip()
    # Remove any HTML tags (basic)
    import re
    clean = re.sub('<.*?>', '', snippet)
    return clean

def main():
    print(BANNER)

    parser = argparse.ArgumentParser(description="XSScope - XSS Reflection Checker (API powered)")
    parser.add_argument('-u', '--url', required=True, help='Target URL to check for XSS reflection')
    args = parser.parse_args()
    
    target_url = args.url

    print(f"{Fore.YELLOW}[*] Checking internet connection...{Style.RESET_ALL}")
    if check_internet():
        print(f"{Fore.GREEN}[+] Internet connection is ON{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[+] Internet connection is OFF")
        print("Turn on WiFi/mobile data and rerun the tool.")
        sys.exit(1)

    print(f"{Fore.YELLOW}[*] Checking site accessibility: {target_url}{Style.RESET_ALL}")
    try:
        head_resp = requests.head(target_url, timeout=10, allow_redirects=True)
        if head_resp.status_code == 200:
            print(f"{Fore.GREEN}[+] Site is accessible{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[+] Site is not accessible: returned status code {head_resp.status_code}")
            sys.exit(1)
    except requests.RequestException as e:
        print(f"{Fore.RED}[+] Site is not accessible: {e}")
        sys.exit(1)

    print(f"{Fore.YELLOW}[*] Querying XSS check API for: {target_url}{Style.RESET_ALL}")

    try:
        api_url = API_ENDPOINT + target_url
        response = requests.get(api_url, timeout=15)
        response.raise_for_status()
        html = response.text

        search_url = extract_search_url(html)
        if search_url:
            print(f"{Fore.CYAN}[+] Search URL pattern found:\n    {search_url}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[!] Could not extract Search URL pattern from API response.{Style.RESET_ALL}")

        if "XSS payload was reflected" in html:
            print(f"{Fore.GREEN}[+] XSS payload was reflected in the response! Potential vulnerability detected.{Style.RESET_ALL}")
        elif "XSS payload was not reflected" in html:
            print(f"{Fore.RED}[-] XSS payload was NOT reflected. Target likely not vulnerable.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[!] Unexpected API response. Unable to determine XSS reflection status.{Style.RESET_ALL}")

    except requests.RequestException as e:
        print(f"{Fore.RED}[!] Error querying the API: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()
