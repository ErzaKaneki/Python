from menu_data import brunch_items, early_bird_items

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
        
brunch = Menu("Brunch", brunch_items, 1100, 1600)
early_bird_dinners = Menu("Early Bird", early_bird_items, 1500, 1800)
