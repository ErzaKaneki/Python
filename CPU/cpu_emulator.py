import csv

class CPU:
    def __init__(self):
        self.number_registers = [0] *256
        self.history_registers = [0] * 256
        self.letter_registers = [0] * 256
        self.numbers_index = 1
        self.letter_index = 0
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ("")
        
    def fetch(self, grab):
        with open(grab, "r") as file:  #reads file
            csv_reader = csv.reader(file, delimiter = ',')
            for line in csv_reader:
                self.program_counter += 1
                self.control_unit(line)
            
    def control_unit(self, string):  #decides where to send information
        for i in string[:1]: 
            if i[:2] == "0b":
                self.ALU_arithmetic(string)
            else:
                self.ALU_letters(string)

    def update_display(self, to_update):  #arithmetic output
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store): #arithmetic registers are short term storage.
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"{int(value_to_store, 2)} was stored in register address {self.numbers_index}.")
        self.numbers_index +=1

    def load_value_from_register(self, register_address): #arithmetic
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value
    
    def store_to_history_register(self, result_to_store): #arithmetic
        if self.history_index > 9:
            self.history_index = 0

        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2):  #arithmetic
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 + num2
        return calculated_value
    
    def multiply(self, address_num1, address_num2):   #arithmetic
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 * num2
        return calculated_value
    
    def subtract(self, address_num1, address_num2):   #arithmetic
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 - num2
        return calculated_value
    
    def divide(self, address_num1, address_num2):   #arithmetic
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = 0
        if num2 != 0:
            calculated_value = int(num1 / num2)
        else:
            print(f"Division by 0 error: {num1} / {num2}.")
        return calculated_value
    
    def get_last_calculation(self):   #arithmetic
        self.temp_history_index -= 1
        last_value = f"Last recorded result: {int(self.history_registers[self.temp_history_index], 2)}"
        self.update_display(last_value)
            
    def ALU_arithmetic(self, binary):   #arithmetic main
            binary_values = ''.join(binary)
            binary.pop()
            opcode = binary_values[:8]
            source_one = binary_values[8:13]
            source_two = binary_values[13:18]
            store = binary_values[18:28]
            function_code = binary_values[28:]

            if opcode == "0b000001":
                self.store_value_to_register(store)
                return
            elif opcode == '0b100001':
                self.get_last_calculation()
                return
            elif opcode != '0b000000':
                self.update_display("Invalid OPCODE")
                print(opcode)
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
       
    
    def ALU_letters(self, binary):  #non-arithmetic
        if self.letter_index > 265:
            self.letter_index = 1
        binary = ''.join(binary)
        define = self.binary_to_text(binary)
        self.letter_registers[self.letter_index] = define
        self.letter_index += 1
        self.execute_typed(define)
        
     
    @staticmethod        #called so to avoid calling .self
    def binary_to_text(binary_string):   #non-arithmetic
        binary_values = binary_string.split(' ')
        binary_values.pop()
        text = ''.join(chr(int(byte, 2))for byte in binary_values)
        return text

        
           
            
    def execute_typed(self, list):   #non-arithmetic
            output = list
            print(output)
            toot_toot = Memory_Bus()
            toot_toot.mem_output.append(output)

           
            
class Memory_Bus:  #long term storage
    def __init__(self):
        self.mem_output = []
        self.mem_output_counter = 0
        
erza = CPU()
erza.fetch("G:/Users/nevin/vsCode/Python/CPU/input_file.txt")
