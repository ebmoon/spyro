# y = x * x
# f1 = lambda x, y: (10 * x + 11 * y + 0) % 16 <= (2 * x + 3 * y + 7) % 16
# f2 = lambda x, y: (12 * x + 5 * y + 7) % 16 <= (2 * x + 8 * y + 15) % 16
# f3 = lambda x, y: (0 * x + 5 * y + 3) % 16 <= (8 * x + 2 * y + 4) % 16
# f4 = lambda x, y: (12 * x + 7 * y + 1) % 16 <= (12 * x + 3 * y + 8) % 16
# fs = [f1, f2, f3, f4]

# y = x * x * x
# f1 = lambda x, y: (6 * x + 10 * y + 1) % 16 <= (10 * x + 5 * y + 2) % 16
# f2 = lambda x, y: (0 * x + 4 * y + 1) % 16 <= (11 * x + 3 * y + 13) % 16
# f3 = lambda x, y: (10 * x + 14 * y + 9) % 16 <= (4 * x + 15 * y + 14) % 16
# f4 = lambda x, y: (4 * x + 5 * y + 1) % 16 <= (10 * x + 7 * y + 10) % 16
# f5 = lambda x, y: (12 * x + 12 * y + 9) % 16 <= (4 * x + 2 * y + 9) % 16
# fs = [f1, f2, f3, f4, f5]

# y = x / 2
# f1 = lambda x, y: (0 * x + 15 * y + 9) % 16 <= (11 * x + 10 * y + 15) % 16
# f2 = lambda x, y: (7 * x + 10 * y + 1) % 16 <= (1 * x + 15 * y + 8) % 16
# f3 = lambda x, y: (3 * x + 11 * y + 1) % 16 <= (14 * x + 4 * y + 14) % 16
# f4 = lambda x, y: (13 * x + 6 * y + 6) % 16 <= (2 * x + 13 * y + 6) % 16
# f5 = lambda x, y: (14 * x + 4 * y + 4) % 16 <= (10 * x + 13 * y + 8) % 16
# f6 = lambda x, y: (0 * x + 0 * y + 14) % 16 <= (1 * x + 14 * y + 14) % 16
# fs = [f1, f2, f3, f4, f5, f6]

# y <= x * x
# f1 = lambda x, y: (2 * x + 15 * y + 3) % 16 <= (0 * x + 15 * y + 15) % 16
# f2 = lambda x, y: (10 * x + 0 * y + 4) % 16 <= (0 * x + 15 * y + 15) % 16
# f3 = lambda x, y: (8 * x + 15 * y + 4) % 16 <= (8 * x + 0 * y + 4) % 16
# fs = [f1, f2, f3]

# y != 7
# f1 = lambda x, y: (0 * x + 0 * y + 1) % 16 <= (0 * x + 13 * y + 5) % 16
# fs = [f1]

# (x + y + 4 <= x + 15 * y + 7 % 16) && (2 * x + 14 * y + 3 <= x + 15 * y + 7);
# f1 = lambda x, y: (15 * x + 1 * y + 8) % 16 <= (1 * x + 15 * y + 11) % 16
# f2 = lambda x, y: (0 * x + 14 * y + 3) % 16 <= (15 * x + 15 * y + 11) % 16
# fs = [f1, f2]

# (x == 3 && y == 7) || (x == 9 && y == 10) || (x == 6 && y == 1) || (x == 0 && y == 15)
# f1 = lambda x, y: (2 * x + 9 * y + 11) % 16 <= (3 * x + 11 * y + 15) % 16
# f2 = lambda x, y: (6 * x + 15 * y + 5) % 16 <= (6 * x + 5 * y + 4) % 16
# f3 = lambda x, y: (11 * x + 11 * y + 5) % 16 <= (12 * x + 3 * y + 15) % 16
# f4 = lambda x, y: (6 * x + 9 * y + 3) % 16 <= (2 * x + 1 * y + 14) % 16
# f5 = lambda x, y: (6 * x + 3 * y + 12) % 16 <= (15 * x + 2 * y + 14) % 16
# fs = [f1, f2, f3, f4, f5]

# (x == 3 && y == 7)
# f1 = lambda x, y: (1 * x + 1 * y + 6) % 16 <= (0 * x + 0 * y + 0) % 16
# f2 = lambda x, y: (2 * x + 15 * y + 1) % 16 <= (2 * x + 15 * y + 0) % 16
# fs = [f1, f2]

# f1 = lambda x, y: (x + y + 4) % 16 <= (x + 15 * y + 7) % 16 
# fs = [f1]

f1 = lambda x, y: (2 * x + 14 * y + 3) % 16 <= (x + 15 * y + 7) % 16
fs = [f1]

# f1 = lambda x, y: (0 * x + 0 * y + 1) % 16 <= (7 * x + 9 * y + 1) % 16
# fs = [f1]

# f1 = lambda x, y: (((2 * x + 14 * y + 3) % 16 <= (x + 15 * y + 7) % 16) or ((x + y + 4) % 16 <= (x + 15 * y + 7) % 16)) 
# fs = [f1]

lines = []

for y in range(16):
    line = "-"
    for x in range(16):
        if all(f(x, y) for f in fs):
            line += " * "
        else:
            line += "   "
    line += "-"
    lines.append(line)

print(" " + " | " * 16 + " ")
for line in lines[::-1]:
    print(line)
print(" " + " | " * 16 + " ")
