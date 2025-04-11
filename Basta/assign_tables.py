tables = {
    1: ['Jiho', False],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
}

def assign_table(table_number, name, vip_status=False):
    if table_number in tables:
        tables[table_number] = [name, vip_status]

assign_table(6, 'Yoni', False)

assign_table(name='Martha', table_number=3, vip_status=True)

assign_table(4, 'Karla')

print(tables)