class UltraSuperCalculator:
    def __init__(self, name):
        self.name = name
        self.number_registers = [0] * 32
        self.history_registers = [0] * 32
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ("")
        self.update_display(f"{self.name}'s Calculator")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

# Erza = UltraSuperCalculator("Erza")  Testing update_display()

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"{int(value_to_store, 2)} was stored in register address {self.numbers_index}.")
        self.numbers_index +=1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value
    
    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0

        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 + num2
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
        last_value = f"Last recorded result: {int(self.history_registers[self.temp_history_index], 2)}"
        self.update_display(last_value)

    def binary_reader(self, instruction):
        if len(instruction) != 32:
            print("Invalid Instruction, goodbye.")
            return
        
        opcode = instruction[:6]
        source_one = instruction[6:11]
        source_two = instruction[11:16]
        store = instruction[16:26]
        function_code = instruction[26:]

        if opcode == "000001":
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
            result = self.add(source_one, source_two)
        elif function_code == '100010':
            result = self.subtract(source_one, source_two)
        elif function_code == '011000':
            result = self.multiply(source_one, source_two)
        elif function_code == '011010':
            result = self.divide(source_one, source_two)
        else:
            self.update_display("Invalid FUNCTION CODE")
            return
        
        self.store_to_history_register(result)
        self.update_display(f"The result is: {result}")

erza = UltraSuperCalculator("Erza")
# Adds 5 and 10 to number registers
erza.binary_reader("00000100000000000000000101000000")
erza.binary_reader("00000100000000000000001010000000")

# Adds/Subtracts/Multiplies/Divides 5 and 10 from registers
erza.binary_reader("00000000001000100000000000100000")
erza.binary_reader("00000000001000100000000000100010")
erza.binary_reader("00000000001000100000000000011000")
erza.binary_reader("00000000001000100000000000011010")

# Gets the last three calculations
erza.binary_reader("10000100000000000000000000000000")
erza.binary_reader("10000100000000000000000000000000")
erza.binary_reader("10000100000000000000000000000000")
