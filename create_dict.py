import io

lines = []  #lista która będzie przechowywała linie

#czytanie inputu, przekazywanie każdej linijki do listy
while True:
    line = input()
    lines.append(line)
    if line.endswith('}'):
        break

print(lines)


one_line = '' #wartość złączająca wszystkie elementy listy
#złączenie wszystkich elementów listy w jeden ciąg (połączenie linków)
for line in lines:
    one_line += line


print(one_line)

persons = one_line.split(',')   #podział długiego stringa na listę, gdzie każdy element to jeden klucz i wartość starego słownika
print(persons)
dict = {}
for line in persons:
    key_and_value = line.split(':')
    key = key_and_value[0]
    elements_of_value = key_and_value[1:]
    value = ''
    for element in elements_of_value:
        value += element + ":"
    key = key[2:-1]         #usunięcie " '" i "'"
    value = value[2:-2]     #usunięcie " '" i " '"
    print(f'klucz: {key}, wartość: {value}')
    dict[key] = value

print(dict)
# dict =
# file = open('output.txt', 'w')
# file.write(one_line)
# file.close()