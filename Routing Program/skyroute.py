from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

landmark_string = ""
for letter, landmark in landmark_choices.items():
    landmark_string += "{0} - {1}".format(letter, landmark)

def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def skyroute():
    greet()

def set_start_and_end(start_point, end_point):
    if get_start != None:
                change_point = input("What would you like to change? You can enter 'O' for 'orgin', 'D' for 'destination', or 'b' for 'both': -> ")
                if change_point.upper() == "B":
                    start_point = get_start()
                    end_point = get_end()
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
     set_start_and_end(start_point, end_point)

def get_route(start_point, end_point):
     start_stations = vc_landmarks[start_point]
     end_stations = vc_landmarks[end_point]
     routes = []
     