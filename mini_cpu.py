import time

registers = {"R1":0,"R2":0,"R3":0,"R4":0}
memory = []
for i in range(10):
    memory.append(0)

#store value into specific register
def mov(register,value):
    registers[register]=int(value)

#add value to value in specific register
def add(register,value_or_register):
    
    if value_or_register in registers:
        registers[register]+=registers[value_or_register]
        return
    value = int(value_or_register)
    registers[register]+=value


#store into memory, value located in specific register 
def store(register,memory_num):
    memory_num = int(memory_num)
    memory[memory_num]=registers[register]

#loads from memory at index into specific register
def load(register,address):
    registers[register]=memory[address]


program = [
    "MOV R1, 5",
    "ADD R1, 10",
    "STORE R1, 5",
    "MOV R2, 1",
    "ADD R2, R1"
]

def run_program(program):
    #implementing clock
    insruction_address_register = 0
    #first we separate each line into 3 parts ex: "MOV","R1","5"
    while insruction_address_register < len(program):
        instruction = program[insruction_address_register]
        two_parts = instruction.split(", ")
        instruction_register = two_parts[0]

        value = two_parts[1] #our value is a str

        instruction_split_register= instruction_register.split(" ")
        opcode = instruction_split_register[0] #instruction
        register = instruction_split_register[1] #register
        if opcode in ["MOV","ADD","STORE"]:
            if opcode == "MOV":
                mov(register,value)
            elif opcode == "ADD":
                add(register,value)
            elif opcode == "STORE":
                store(register,memory_num=value)
            print(registers)
            print(memory)
            print("-" * 30)
        insruction_address_register+=1
        time.sleep(1)
run_program(program)

