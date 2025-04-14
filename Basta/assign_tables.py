tables = {
    1: {
        'name': 'Jiho',
        'vip_status': False,
        'order': 'Orange Juice, Apple Juice'
        },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}

def assign_food_items(table_number, **order_items):
    food = order_items.get("food")
    drinks = order_items.get("drinks")
    tables[table_number]['order']['food_items'] = food
    tables[table_number]['order']['drinks'] = drinks
    

def assign_table(table_number, name, vip_status=False):
    if table_number in tables:
        tables[table_number]['name'] = name
        tables[table_number]['vip_status'] = vip_status
        tables[table_number]['order'] = {}

# def assign_and_print_order(table_number, *order_items):
#     if table_number in tables:
#         tables[table_number]['order'] = order_items
#     for item in order_items:
#         print(item)
        
# assign_table(2, 'Arwa', True)
# assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')

assign_table(2, 'Douglas', True)    
    
assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')    

print(tables)