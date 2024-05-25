"""
Código para converter instruções em BLDIM-Assembly para seus
correspondentes binários, e então para hexadecimal, uma vez
que as memórias disponíveis no Logisim aceitam somente 
instruções em hexadecimal.
"""

assembly = [
    "add $um 1 $zero $zero",
    "add $s0 0 $zero $zero",
    "add $s1 16 $zero $zero",
    "add $v0 32 $zero $zero",
    "add $t7 4 $zero $zero",
    "add $s2 0 $zero $zero",
    "beq $zero 33 $s2 $t7",
	"add $s3 0 $zero $zero",
	"beq $zero 31 $s3 $t7",
	"add $t0 0 $zero $zero",
    "add $s4 0 $zero $zero",
	"mul $t1 1 $t7 $s2",
	'mul $t2 1 $um $s3',
	'beq $zero 28 $s4 $t7',
	'mul $t3 1 $um $s4',
	'add $t3 0 $s0 $t3',
	'add $t3 0 $t3 $t1',
	'lw $t4 0 $t3 $zero',
	'mul $t3 1 $t7 $s4',
	'add $t3 0 $s1 $t3',
	'add $t3 0 $t3 $t2',
	'lw $t5 0 $t3 $zero',
	'mul $t4 1 $t4 $t5',
	'add $t0 0 $t0 $t4',
	'add $s4 1 $s4 $zero',
	'j $zero 13 $zero $zero',
	'add $t1 0 $v0 $t1',
	'add $t1 0 $t1 $t2',
	'sw $zero 0 $t1 $t0',
	'add $s3 1 $s3 $zero',
	'j $zero 8 $zero $zero',
    'add $s2 1 $s2 $zero',
    'j $zero 6 $zero $zero'
    ]

registers = {
    "$zero": '0000',
    "$um": '0001',
    "$t0": '0010',
    "$t1": '0011',
    "$t2": '0100',
    "$t3": '0101',
    "$t4": '0110',
    "$t5": '0111',
    "$t6": '1000',
    "$t7": '1001',
    "$s0": '1010',
    "$s1": '1011',
    "$s2": '1100',
    "$s3": '1101',
    "$s4": '1110',
    "$v0": '1111'
    }
    
functions = {
    "add": '000',
    "mul": '001',
    "sw": '010',
    "lw": '011',
    "beq": '100',
    "jr": '101',
    "jal": '110',
    "j": '111'
    }

Hex = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "a",
    "1011": "b",
    "1100": "c",
    "1101": "d",
    "1110": "e",
    "1111": "f"
}

for line in assembly:
    func, reg1, imdt, reg2, reg3 = line.split(" ")
    bin_line = []
    hex_line = []
    for k in functions.keys():
        if func == k:
            bin_line.append(functions[k])
            break
    for k in registers.keys():
        if reg1 == k:
            bin_line.append(registers[k])
            break
    q = int(imdt)
    imdt = []
    while q > 0:
        r = q % 2
        q = q // 2
        imdt.append(str(r))
    imdt.reverse()
    tam = len(imdt)
    for i in range(17-tam):
        imdt.insert(0, "0")
    imdt = "".join(imdt)
    bin_line.append(imdt)
    for k in registers.keys():
        if reg2 == k:
            bin_line.append(registers[k])
            break
    for k in registers.keys():
        if reg3 == k:
            bin_line.append(registers[k])
            break
    bin_line = "".join(bin_line)
    for i in range(0, 32, 4):
        for k in Hex.keys():
            if bin_line[i:i+4] == k:
                hex_line.append(Hex[k])
    hex_line = "".join(hex_line)
    print(hex_line)
