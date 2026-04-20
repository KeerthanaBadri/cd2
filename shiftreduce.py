# -------- INPUT --------
n = int(input("No. of productions: "))
prod = []
for _ in range(n):
    l, r = input().split("->")
    prod.append((l.strip(), r.strip()))
start_symbol = prod[0][0]
stack = ""
inp = input("Input string: ")
i = 0
# -------- DISPLAY --------
print("\nSTACK\t\tINPUT\t\tACTION")
print(f"$\t\t{inp}$")
def show(action, remaining):
    print(f"${stack:<10}\t{remaining + '$':<10}\t{action}")
# -------- REDUCE --------
def reduce_stack(remaining):
    global stack
    changed = True
    while changed:
        changed = False
        for l, r in prod:
            if stack.endswith(r):
                stack = stack[:-len(r)] + l
                show(f"Reduce {l}->{r}", remaining)
                changed = True
                break  # restart after one reduction
# -------- SHIFT REDUCE --------
while i < len(inp):
    stack += inp[i]
    show("SHIFT", inp[i+1:])
    reduce_stack(inp[i+1:])
    i += 1
# Final reductions
reduce_stack("")
# -------- ACCEPT / REJECT --------
if stack == start_symbol:
    print("\nACCEPT")
else:
    print("\nREJECT")
