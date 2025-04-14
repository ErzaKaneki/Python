from calculate_bill import calculate_price_per_person

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

assign_table(7, 'Nevin', True)
assign_food_items(7, food='Pizza', drinks='Coke, Dr. Pepper')
print(tables)
calculate_price_per_person(28.00, 15, 2) # should have tied this into the actual menu and prices