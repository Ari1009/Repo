#!/usr/bin/env python3

from colorama import Fore
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

print(Fore.CYAN)
print("""
██████╗░███████╗██████╗░░█████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗
██████╔╝█████╗░░██████╔╝██║░░██║
██╔══██╗██╔══╝░░██╔═══╝░██║░░██║
██║░░██║███████╗██║░░░░░╚█████╔╝
╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░""")
print("Search any Git-Repo from your LINUX terminal.")
print()
print("""If you type more then one word, add a '+' in between.
Example: 'Hello+World' = 'Hello World'. """)
print()

def menu():
    print(Fore.RED)
    search = str(input("Type Git To Search: "))
    url = urlopen(f'https://github.com/search?q={search}') 
    print()
    soup = BeautifulSoup(url.read(), 'lxml') 
    links = []

    for link in soup.find_all('a', class_="v-align-middle"): 
        
        links.append(link.get('href'))

    print("A list of the top ten Repos from your search:")
    print()
    print(*links, sep = '\n') # This line prints and seperates the repos into their own lines.
    print()
    print(Fore.CYAN)
    print("Options:\n\nExplore a 'Git README' press [1].\nSearch again? Press [2].\n\nPress [3] to exit.")
    print()
    choice = input()

    if choice == '1':
        print()
        print(Fore.RED)
        add = str(input("Add repo here: "))
        url1 = urlopen(f"https://raw.githubusercontent.com/{add}/master/README.md")# This line pulls up the README.md info. 
        soup = BeautifulSoup(url1.read(), 'lxml')
        link = soup.find_all('p') # This line is the html flag targeter for displaying only the README info into the terminal.
        print(link)
        print()
        print(Fore.CYAN)
        
        def menu1():
            print("Options:\n\nGit clone the repo press [1].\nNew search press [2].")
            print()
            choice2 = input()

            if choice2 == '1':
                print(Fore.RED)
                clone1 = os.system(f'git clone https://github.com{add}.git') # Clones git to your computer.
                exit()
            
            if choice2 == '2': # Back to search option.
                menu()

        menu1()

    if choice == '2': # Back to search option.
        menu()

    if choice == '3': # Will allow you to exit program.
        exit()
menu()
