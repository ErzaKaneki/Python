import csv

class CPU:
    def __init__(self, input):
        self.input = input
        self.number_registers = [0] * 256
        self.history_registers = [0] * 256
        self.leter_registers = [0] * 265
        self.string_registers = [0] * 256
        self.numbers_index = 1
        self.letter_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ("")
        self.program_counter = 0
        
    def fetch(self):
        with open(self.input, "r") as file:
            csv_reader = csv.reader(file)
            
            for line in csv_reader:
                self.program_counter += 1
                self.control_unit(line)
                
            
    def control_unit(self, string):
        if string[:2] == "0b":
           self.ALU_arithmetic(string)
        else:
            self.ALU_letters(string)
            
            
    
    def ALU_arithmetic(self, binary):
            if len(binary) != 34:
                print("Invalid code, goodbye.")
                return
        
            opcode = binary[:8]
            source_one = binary[8:13]
            source_two = binary[13:18]
            store = binary[18:28]
            function_code = binary[28:]

            if opcode == "0b000001":
                self.store_value_to_register(store)
                return
            elif opcode == '0b100001':
                self.get_last_calculation()
                return
            elif opcode != '0b000000':
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
       
    
    def ALU_letters(self, binary):
        if self.letter_index > 265:
            self.letter_index = 1
        while binary:
            binary_string = binary[:9]
            decoded = bytes.fromhex(binary_string).decode("ascii")
            self.leter_registers[self.letter_index] = decoded
            self.letter_index += 1
            
    def execute_typed(self, list):
        output = ", ".join(list)
        print(output)
        Memory_Bus.output[Memory_Bus.output_counter] = output
        Memory_Bus.output_counter += 1
            
            
class Memory_Bus:
    def __init__(self):
        self.output = [0] * 256
        self.output_counter = 0