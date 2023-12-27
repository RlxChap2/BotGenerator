import os
import zipfile
import requests
from colorama import Fore, Style

def download_extract_repo(repo_url):
    response = requests.get(repo_url)
    if response.status_code == 200:
        with open('temp.zip', 'wb') as f:
            f.write(response.content)
        
        with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
            zip_ref.extractall('.')
        
        os.remove('temp.zip')
        print(Fore.GREEN + "Project downloaded and extracted successfully!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Failed to download the project." + Style.RESET_ALL)

def main():
    print(Fore.BLUE + "Choose a bot project:" + Style.RESET_ALL)
    print(Fore.BLUE + "1. BotGenerator" + Style.RESET_ALL)
    print(Fore.BLUE + "2. Tutorial" + Style.RESET_ALL)
    print(Fore.BLUE + "3. Ticket" + Style.RESET_ALL)
    print(Fore.BLUE + "4. Suggestions" + Style.RESET_ALL)
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print(Fore.YELLOW + "Downloading BotGenerator..." + Style.RESET_ALL)
        download_extract_repo('https://github.com/RlxChap2/BotGenerator/archive/refs/heads/main.zip')
    elif choice == '2':
        print(Fore.YELLOW + "Downloading Tutorial..." + Style.RESET_ALL)
        download_extract_repo('https://github.com/RlxChap2/Tutorial/archive/refs/heads/main.zip')
    elif choice == '3':
        print(Fore.YELLOW + "Downloading Ticket..." + Style.RESET_ALL)
        download_extract_repo('https://github.com/RlxChap2/Tutorial/archive/refs/heads/main.zip')
    elif choice == '4':
        print(Fore.YELLOW + "Downloading Suggestions..." + Style.RESET_ALL)
        download_extract_repo('https://github.com/RlxChap2/Tutorial/archive/refs/heads/main.zip')
    else:
        print(Fore.RED + "Invalid choice." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
