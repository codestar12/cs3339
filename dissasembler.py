# program = {
# 	#
# 	"94" : {
# 		"instruction": "ADDI",
# 		'ARGS': ['R1', 'R0', 10],
# 		'valid': True
# 	}
# }
#
# ops = {
# 	"ADDI": lambda x: registers[x[0]] = registers[x[1]] + x[2]
# }
#
# registers = {
# 	'R0': 0
# 	'R1': 0
# }
#
# formatedOps = {
#         "ADDI": lambda x: "ADDI\t" + x[0] + ' ' +  x[1] + ' #' + str(x[3])
#         }
#
# while program[PC]["instruction"] != "BREAK":
#
# 	if program[PC]['valid']:
# 		ops[program[PC]["instruction"]](program[PC]['ARGS'])
#
# 	PC += 4


import argparse

parser = argparse.ArgumentParser(description="Simulates MIPS")
parser.add_argument("-i", "--input", help="string of file name of input")
parser.add_argument("-o", "--output", help="string of file names of output")

args = parser.parse_args()

with open(args.input) as f:
    content = f.readlines()
    content = [x.strip() for x in content]

sourceCode = {}

for i in range(len(content)):
    sourceCode[(96 + i * 4)] = content[i]


print(sourceCode)
