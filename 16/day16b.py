from collections import namedtuple
import copy

Instruction = namedtuple('Instruction', 'opcode, inputA, inputB, output')
registers = [0, 0, 0, 0]

def addr(A, B, C):
  registers[C] = registers[A] + registers[B]
def addi(A, B, C):
  registers[C] = registers[A] + B

def mulr(A, B, C):
  registers[C] = registers[A] * registers[B]
def muli(A, B, C):
  registers[C] = registers[A] * B

def banr(A, B, C):
  registers[C] = registers[A] & registers[B]
def bani(A, B, C):
  registers[C] = registers[A] & B

def borr(A, B, C):
  registers[C] = registers[A] | registers[B]
def bori(A, B, C):
  registers[C] = registers[A] | B

def setr(A, B, C):
  registers[C] = registers[A]
def seti(A, B, C):
  registers[C] = A

def gtir(A, B, C):
  registers[C] = 1 if A > registers[B] else 0
def gtri(A, B, C):
  registers[C] = 1 if registers[A] > B else 0
def gtrr(A, B, C):
  registers[C] = 1 if registers[A] > registers[B] else 0

def eqir(A, B, C):
  registers[C] = 1 if A == registers[B] else 0
def eqri(A, B, C):
  registers[C] = 1 if registers[A] == B else 0
def eqrr(A, B, C):
  registers[C] = 1 if registers[A] == registers[B] else 0

opcodes = {'addr': addr, 'addi':addi, 'mulr':mulr, 'muli':muli, 'banr':banr, 'bani':bani, 'borr':borr, 'bori':bori, 'setr':setr, 'seti':seti, 'gtir':gtir, 'gtri':gtri, 'gtrr':gtrr, 'eqir':eqir, 'eqri':eqri, 'eqrr':eqrr}
func_to_opcode = {'addr':set(), 'addi':set(), 'mulr':set(), 'muli':set(), 'banr':set(), 'bani':set(), 'borr':set(), 'bori':set(), 'setr':set(), 'seti':set(), 'gtir':set(), 'gtri':set(), 'gtrr':set(), 'eqir':set(), 'eqri':set(), 'eqrr':set()}
opcodes_to_func = {}
instructions = []


with open('input.txt', 'r') as input_file:
  line_count = 1

  for line in input_file:
    line = line.strip()
    if line == '' and line_count == 1:

      while sum([sum(x) for x in func_to_opcode.values()]) > 0:
        for k,v in func_to_opcode.items():
          if len(v) == 1:
            val = v.pop()
            opcodes_to_func[val] = k

            for li in func_to_opcode.values():
              if val in li:
                li.remove(val)
            break
        
      line_count = 5

    if line_count == 4:
      line_count = 1
      continue

    if line_count == 1:
      registers_before = [int(x) for x in line[9:19].replace(',','').split(' ')]
    
    if line_count == 2:
      parts = [int(x) for x in line.split(' ')]
      opcode = parts[0]
      inputA = parts[1]
      inputB = parts[2]
      output = parts[3]


    if line_count == 3:
      registers_after = [int(x) for x in line[9:19].replace(',','').split(' ')]
    
      for op in opcodes.keys():
        registers = copy.deepcopy(registers_before)
        opcodes[op](inputA, inputB, output)

        equal = True
        for i in range(4):
          if registers[i] != registers_after[i]:
            equal = False
        if equal:
          func_to_opcode[op].add(opcode)
      
      
    if line_count > 6:
      parts = [int(x) for x in line.split(' ')]
      opcode = parts[0]
      inputA = parts[1]
      inputB = parts[2]
      output = parts[3]
      instructions.append(Instruction(opcode, inputA, inputB, output))

    line_count += 1

registers = [0, 0, 0, 0]
for instruction in instructions:
  opcodes[opcodes_to_func[instruction.opcode]](instruction.inputA, instruction.inputB, instruction.output)

print(registers[0])