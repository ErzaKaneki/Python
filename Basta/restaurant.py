from menu_data import arepas_items, brunch_items, early_bird_items, dinner_items, kids_items
from datetime import datetime, time

class Menu:
    
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return f"{self.name} menu available from {self.start_time.strftime("%I%p").lstrip("0").lower()} to {self.end_time.strftime("%I%p").lstrip("0").lower()}."
    
    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return f"${total:.2f}"
        
brunch = Menu("Brunch", brunch_items, time(11, 0), time(16, 0)) # brunch from 11am to 4pm
early_bird_dinners = Menu("Early Bird", early_bird_items, time(15, 0), time(18, 0)) # early bird from 3pm to 6pm
dinner = Menu("Dinner", dinner_items, time(17, 0), time(23, 0)) # dinner form 11am to 9pm
kids = Menu("Kids", kids_items, time(11, 0), time(21, 0)) # kids available from 11am to 9pm
arepas_menu = Menu("Arepas", arepas_items, time(10, 0), time(20, 0)) # arapas available from 10am to 8pm

class Franchise:
    
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
        
    def __repr__(self):
        return f"Franchise located at {self.address}."
    
    def available_menus(self, time):
        return [menu for menu in self.menus if menu.start_time <= time <= menu.end_time]

flagship_store = Franchise("1232 West End Road",[brunch, early_bird_dinners, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird_dinners, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

class Business:
    
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises
        
BFwmH = Business("Basta Fazoolin' with My Heart", [flagship_store, new_installment])
TaA = Business("Take a' Arepa", [arepas_place])