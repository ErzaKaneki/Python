from Game_dict import game_genres

def genre_list(dict):
    sortedkeys = sorted(dict.keys(), key = lambda x:x.lower())
    for i in sortedkeys:
        values = dict[i]
        print(i)

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
    print("Lets get started on a grabbing some game ideas for you, and to be clear MOST games can be found on steam.")
    print("But there could be console only, or even out dated and hard to find game recomendations.")
    print("We look for the 'Best' but our values still might differ from others opinions.")
    print("Here we go!!!")
    
def search_tool(dict):
    print("What style of game are you looking for?")
    genre_list(game_genres)
    search = input("Please make a selection from the list. -> ")
    if search.lower() in dict:
        for i in dict[search.lower()]:
            print(i.name)
            print("Rating - " + str(i.rating))
            print("Price - $" + str(i.price))

search_tool(game_genres)