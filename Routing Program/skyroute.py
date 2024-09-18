from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices
import sys

landmark_string = ""
for letter, landmark in landmark_choices.items():
    landmark_string += " ({0}) - [{1}]".format(letter, landmark)

vc_metro_string = ""
for station in vc_metro.keys():
    vc_metro_string += "[{0}]\n".format(station)

stations_under_construction = []
emp_pass = "sky"

def emp_login():
    login_attempt = 3
    print("Employee or Skyroute")
    e_or_s = input("If you are an employee please enter 'y', if not enter any other key: -> ")
    if e_or_s.lower() == 'y':
        enter_pass = input("Please enter the Employee password: -> ")
        while enter_pass != emp_pass:
            login_attempt -= 1
            if login_attempt <= 0:
                print("No more attempts can be made, goodbye.")
                sys.exit()
            else:    
                enter_pass = input("That was incorrect, you have {1} attempt(s) left, enter Employee password: -> ")   
        if enter_pass == emp_pass:
            station_out_of_service()
    else: 
        return

def station_out_of_service():
            station_option = input("Would you like to add a Station to the Under Construction List or remove one? Enter add or remove: -> ")
            while station_option.lower() != "add" and station_option.lower() != "remove":
                station_option = input("That was not 'add' or 'remove' Try again please.  Enter 'add' or 'remove' -> ")
            if station_option == "add":
                print(vc_metro_string)
                station_entered = input("Please enter the Station under construction: -> ")
                if station_entered in vc_metro and station_entered not in stations_under_construction:
                    stations_under_construction.append(station_entered)
                    print(stations_under_construction)
                    print(station_entered + " has been added")
                    again = input("Do you have another station to add or remove? Enter y/n: -> ")
                    while again.lower() != "y" and again != "n":
                        again = input("Please enter 'y' or 'n' to continue on: -> ")
                    if again.lower() == "y":
                        station_out_of_service()
                    else:
                        print("Thank you for your entries.")
                elif station_entered in stations_under_construction:
                    print("That station is already on the list. Thank you for double checking!")
                else:
                    print("That was not a valid station.")
                    station_out_of_service()
            elif station_option == "remove":
                print(stations_under_construction)
                to_remove = input("Please enter the station to remove: -> ")
                if to_remove in vc_metro and to_remove in stations_under_construction:
                    stations_under_construction.pop(stations_under_construction.index(to_remove))
                    print(stations_under_construction)
                    print(to_remove + " has been removed.")
                    again = input("Do you have another station to add or remove? Enter y/n: -> ")
                    while again.lower() != "y" and again != "n":
                        again = input("Please enter 'y' or 'n' to continue on: -> ")
                    if again.lower() == "y":
                        station_out_of_service()
                    else:
                        print("Thank you for your entries.")
                elif to_remove not in stations_under_construction:
                    print("That station must have been removed already it is not on the list. Thank you for checking!")
                else:
                    print("That is not a valid station.")
                    station_out_of_service()
            return

            
                    

def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def skyroute():
    greet()
    new_route()
    goodbye()

def set_start_and_end(start_point = None, end_point = None):
    if start_point != None:
                change_point = input("What would you like to change? You can enter 'o' for 'orgin', 'd' for 'destination', or 'b' for 'both': -> ")
                if change_point.upper() == "B":
                    start_point = get_start()
                    end_point = get_end()
                    if start_point == end_point:
                        print("Well thats not very fun, you choose a path going nowhere, lets go places.  Try again...")
                        set_start_and_end(start_point, end_point)
                elif change_point.upper() == "O":
                    start_point = get_start()
                elif change_point.upper() == "D":
                    end_point = get_end()
                else:
                    print("Oops, that isn't 'o', 'd', or 'b'...")
                    set_start_and_end(start_point, end_point)
                       
    else:
        start_point = get_start()
        end_point = get_end()

    return start_point, end_point


def get_start():
    start_point_letter = input("Where are you coming from?  Type in the corresponding letter: -> ")
    if start_point_letter.lower() in landmark_choices:
        start_point = landmark_choices[start_point_letter.lower()]
        return start_point
    else:
        print("Sorry that's not a landmark we have data on.  Let's try this again...")
        return get_start()

def get_end():
    end_point_letter = input("Where are you heading?  Type the corresponding letter: -> ")
    if end_point_letter.lower() in landmark_choices:
        end_point = landmark_choices[end_point_letter.lower()]
        return end_point
    else:
        print("Sorry that's not a landmark we have data on.  Let's try this again...")
        return get_end()

def new_route(start_point = None, end_point = None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    
    if shortest_route:
        shortest_route_string = "\n".join(shortest_route)
        print("The shortest metro route form {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    else:
        print("Unfortunately, there is currently no path tetween {0} and {1} due to maintenance.".format(start_point, end_point))
    
    again = input("Would you like to see another route? Enter y/n: -> ")
    
    while again.lower() != "y" and again.lower() != "n":
        again = input("Please make sure to enter 'y' or 'n': -> ")
    if again.lower() == "y":
        show_landmarks()
        new_route(start_point, end_point)
    elif again.lower() == "n":
        pass

def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: -> ")
    if see_landmarks.lower() == "y":
         print(landmark_string)
    elif see_landmarks.lower() == "n":
        pass
    else:
        print("Seem that letter want not 'y' or 'n' lets try that again...")
        show_landmarks()

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    for ss in start_stations:
        for es in end_stations:
            metro_system = get_active_stations() if stations_under_construction  else vc_metro
            if len(stations_under_construction) > 0:
                possible_route = dfs(metro_system, ss, es)
                if possible_route is None:
                    return None            
            route = bfs(metro_system, ss, es)
            if route is not None:
                routes.append(route)
            else:
                print("There are no routes available, please try different selections.")
                skyroute()
    shortest_route = min(routes, key = len)
    return shortest_route

def goodbye():
    print("Thanks for using SkyRoute!")

def get_active_stations():
    updated_metro = vc_metro
    for suc in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():
            if current_station != suc:
                updated_metro[current_station] -= set(stations_under_construction)
            else:
                updated_metro[current_station] = set([])
    return updated_metro

emp_login()
skyroute()
