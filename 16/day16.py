from collections import namedtuple
import copy

# Instruction = namedtuple('Instruction', 'opcode, inputA, inputB, output')
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
opcodes_numbers = {'addr':[], 'addi':[], 'mulr':[], 'muli':[], 'banr':[], 'bani':[], 'borr':[], 'bori':[], 'setr':[], 'seti':[], 'gtir':[], 'gtri':[], 'gtrr':[], 'eqir':[], 'eqri':[], 'eqrr':[]}
# instructions = []


with open('input.txt', 'r') as input_file:
  line_count = 1
  how_many_behave_like_3_opcodes = 0

  for line in input_file:
    line = line.strip()
    if line == '' and line_count == 1:
      break
    if line_count == 4:
      line_count = 1
      continue

    if line_count == 1:
      registers_before = [int(x) for x in line[9:19].replace(',','').split(' ')]
    
    if line_count == 2:
      parts = line.split(' ')
      opcode = parts[0]
      inputA = int(parts[1])
      inputB = int(parts[2])
      output = int(parts[3])


    if line_count == 3:
      registers_after = [int(x) for x in line[9:19].replace(',','').split(' ')]
    
      behave_like = 0
      for op in opcodes.keys():
        registers = copy.deepcopy(registers_before)
        opcodes[op](inputA, inputB, output)

        equal = True
        for i in range(4):
          if registers[i] != registers_after[i]:
            equal = False
        if equal:
          behave_like += 1
          if behave_like == 3:
            break
      
      if behave_like == 3:
        how_many_behave_like_3_opcodes += 1


    line_count += 1

print(how_many_behave_like_3_opcodes)