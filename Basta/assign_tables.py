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

print(tables)

def assign_table(table_number, name, vip_status=False):
    if table_number in tables:
        tables[table_number]['name'] = name]
        tables[table_number]['vip_status'] = vip_status
        tables[table_number]['order'] = ''

