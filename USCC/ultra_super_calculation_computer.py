class UltraSuperCalculator:
    def __init__(self, name):
        self.name = name
        self.number_registers = [0] * 32
        self.history_registers = [0] * 32
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ""
        self.update_display(f"{self.name}'s Calculator")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

# Erza = UltraSuperCalculator("Erza")  Testing update_display()

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
            self.number_registers[self.numbers_index] = int(value_to_store, 2)
            print(f"{int(value_to_store, 2)} was stored in register address {self.number_registers[self.numbers_index]}")
            self.numbers_index +=1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[self.numbers_index], 2)
        return int_value
    
    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0
            self.history_registers[self.history_index] = int(result_to_store, 2)
            self.history_index += 1
            self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = sum(num1, num2)
        return calculated_value
    
    def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 * num2
        return calculated_value
    
    def subtract(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 - num2
        return calculated_value
    
    def divide(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = 0
        if num2 != 0:
            calculated_value = int(num1 / num2)
        else:
            print(f"Division by 0 error: {num1} / {num2}.")
        return calculated_value
    
    def get_last_calculation(self):
        self.temp_history_index -= 1
        last_value = "Last recorded result = " + int(self.history_registers[self.temp_history_index], 2)
        self.update_display(last_value)

    def binary_reader(self, instruction):
        if len(instruction) != 32:
            print("Invalid Instruction, goodbye.")
            return
        
        opcode = instruction[0, 5]
        source_one = instruction[6, 10]
        source_two = [11, 15]
        store = instruction[16, 25]
        function_code = instruction[26, 31]

        if opcode == '000001':
            self.store_value_to_register(store)
            return
        elif opcode == '100001':
            self.get_last_calculation()
            return
        elif opcode != '000000':
            self.update_display("Invalid OPCODE")
            return
        
        result = 0

        if function_code == '100000':
            self.update_display(self.add(source_one, source_two))
            return
        elif function_code == '100010':
            self.update_display(self.subtract(source_one, source_two))
            return
        elif function_code == '011000':
            self.update_display(self.multiply(source_one, source_two))
            return
        elif function_code == '011010':
            self.update_display(self.divide(source_one, source_two))
            return
        elif function_code != '000000':
            self.update_display("Invalid OPCODE")
            return

# erza = UltraSuperCalculator("Erza")
# erza.binary_reader("1234567812345678123456781234567") Testing if reader is working
# erza.binary_reader("12345678123456781234567812345678")

        