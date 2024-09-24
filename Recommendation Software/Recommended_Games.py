from Game_dict import game_genres
import os
import time

def genre_list(dict):
    sortedkeys = sorted(dict.keys(), key = lambda x:x.lower())
    for i in sortedkeys:
        values = dict[i]
        print(i.title())



def greeting():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⠶⠶⠶⠶⠶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⣿⠟⠋⣉⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⣉⠙⠻⣿⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣦⣄⣉⡀⠉⠛⠛⠛⠛⠛⠛⠉⢀⣉⣠⣴⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠼⠿⠷⠤⠤⠤⠾⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠷⠤⠤⠤⠾⠿⠧⠀⠀⠀
⠀⠀⢰⡶⠶⠶⠶⠶⣶⡶⠶⠶⠶⠶⢶⣶⠶⠶⠶⠶⢶⣶⠶⠶⠶⠶⢶⡆⠀⠀
⠀⠀⢸⡇⣶⣶⣶⠀⣿⡇⢰⣶⣶⠀⢸⣿⠀⣶⣶⡆⢸⣿⠀⣶⣶⣶⢸⡇⠀⠀
⠀⠀⢸⣇⣈⣹⣯⣀⣿⣇⣈⣉⣉⣀⣼⣿⣀⣉⣉⣁⣸⣿⣀⣉⣉⣁⣸⡇⠀⠀
⠀⠀⠈⠉⠉⠉⠉⠿⣭⣉⣉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣉⣉⣉⣉⣉⡉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠙⠛⣷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠶⠾⠟⠛⠛⠛⠛⠻⠷⠶⠶⣦⣤⣤⣴⠟⠀⠀
⠀⠀⠀⠀⠀⢠⣶⡶⢶⣶⣶⣶⣶⠶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣯⡄⢨⣿⣿⣿⣍⢙⣽⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    print("Thank you for choosing Game Recommendations from Erza!")
    print("Lets get started on a grabbing some game ideas for you, and to be clear MOST games can be found on https://store.steampowered.com/.")
    print("But there could be console only, or even out dated and hard to find game recomendations.")
    print("We look for the 'Best' but our values still might differ from others opinions.")
    print("Here we go!!!")
    input("\n\nPlease Press Enter to Continue....")
    
def search_tool(dict):
    print("\n\nWhat style of game are you looking for?\n")
    genre_list(dict)
    search = input("\nPlease make a selection from the list. -> ")
    while search.lower() not in dict:
        os.system('cls')
        genre_list(dict)
        search = input("Please check the list and enter your selection: - > ")
    if search.lower() in dict:
        counter = 1
        while counter <= 5:
            for i in dict[search.lower()]:
                if i.rating == counter:
                    print("\n" + str(i.rating))
                    print("Title: " + i.name)
                    print("Price: $" + str(i.price))
                    counter += 1
    again = input("Would you like to search again? Enter y/n: -> ")
    while again.lower() != "y" and again.lower() != "n":
        again = input("Please enter y/n: -> ")
    if again == "y":
        os.system("cls")
        search_tool(dict)
    else:
        return
    
def good_bye():
    print("\n\nThank you for using our search, enjoy your selections!\n\n")
    print("""  __                            _ _ 
 / _|                          | | |
| |_ __ _ _ __ _____      _____| | |
|  _/ _` | '__/ _ \\ \\ /\\ / / _ \\ | |
| || (_| | | |  __/\\ V  V /  __/ | |
|_| \\__,_|_|  \\___| \\_/\\_/ \\___|_|_|""")
    
def recommend():
    greeting()
    search_tool(game_genres)
    good_bye()

recommend()