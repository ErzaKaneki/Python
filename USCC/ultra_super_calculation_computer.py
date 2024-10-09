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