class TAC:
    def __init__(self):
        self.t = 0

    def temp(self):
        self.t += 1
        return f"t{self.t}"

    def prec(self, op):
        return 1 if op in "+-" else 2 if op in "*/" else 0

    def gen(self, expr):
        ops, vals, tac = [], [], []

        def apply():
            op = ops.pop()
            b, a = vals.pop(), vals.pop()
            t = self.temp()
            tac.append(f"{t} = {a} {op} {b}")
            vals.append(t)

        for ch in expr.replace(" ", ""):
            if ch.isalnum():
                vals.append(ch)
            elif ch == '(':
                ops.append(ch)
            elif ch == ')':
                while ops[-1] != '(':
                    apply()
                ops.pop()
            else:
                while ops and self.prec(ops[-1]) >= self.prec(ch):
                    apply()
                ops.append(ch)

        while ops:
            apply()

        return tac

expr = input("Enter an expression: ")
t = TAC()
res = t.gen(expr)

print("\nThree Address Code:")
for line in res:
    print(line)