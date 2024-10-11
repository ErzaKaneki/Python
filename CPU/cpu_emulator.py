import csv

class CPU:
    def __init__(self, instruction):
        self.instruction = instruction
        self.number_registers = [0] * 256
        self.history_registers = [0] * 256
        self.leter_registers = [0] * 265
        self.string_registers = [0] * 256
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ("")
        self.program_counter = 0
        
    def fetch(self):
        with open(self.instruction, "r") as file:
            csv_reader = csv.reader(file)
            
            for line in csv_reader:
                self.program_counter += 1
                self.control_unit(line)
                
            
    def control_unit(self, string):
        if string[:2] == "0b":
            pass
        elif len(string) == 8:
            pass
            
    
    def ALU_arithmetic(self, binary):
        pass
    
    def ALU_letters(self, binary):
        pass