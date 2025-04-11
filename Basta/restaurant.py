from menu_data import brunch_items, early_bird_items, dinner_items, kids_items

class Menu:
    
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}."
    
    def calculate_bill(self, purchased_items):
        total = 0
        for items in purchased_items:
            if items in self.items:
                total += self.items[items]
        return f"${total:.2f}"
        
brunch = Menu("Brunch", brunch_items, "11am", "4pm")
early_bird_dinners = Menu("Early Bird", early_bird_items, "3pm", "6pm")
dinner = Menu("Dinner", dinner_items, "11am", "9pm")
kids = Menu("Kids", kids_items, "11am", "9pm")

print(Menu.calculate_bill(brunch, ["pancakes", "home fries", "coffee"]))