n = int(input("Enter number of TAC instructions: "))
tac = []

print("Enter TAC instructions (e.g., t1 = b * c):")
for _ in range(n):
    tac.append(input().strip())

print("\nGenerated Assembly Code:")

reg = 1

for line in tac:
    parts = line.split()
    result = parts[0]
    arg1 = parts[2]
    op = parts[3]
    arg2 = parts[4]
    print(f"MOV R{reg}, {arg1}")
    if op == '+':
        print(f"ADD R{reg}, {arg2}")
    elif op == '-':
        print(f"SUB R{reg}, {arg2}")
    elif op == '*':
        print(f"MUL R{reg}, {arg2}")
    elif op == '/':
        print(f"DIV R{reg}, {arg2}")

    print(f"MOV {result}, R{reg}")
    reg += 1
