import io

lines = []
i = 0

while True:
    line = input()
    lines.append(line)
    if line.endswith('}'):
        break

print(lines)
one_line = ''
for line in lines:
    one_line += line


print(one_line)

