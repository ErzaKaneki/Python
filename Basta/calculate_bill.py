def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)
    
table_7_total = [534.50, 20, 5]

calculate_price_per_person(*table_7_total)