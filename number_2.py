from pprint import pprint


def get_names(path):
    _names = []
    with open(path, 'r') as file:
        for line in file:
            for name in line.split(','):
                name = name.replace('"', '')
                _names.append(name)
    return _names


def get_result(all_names):
    result = 0
    subtruction_constant = ord('A') - 1

    for i, name in enumerate(all_names):
        total = 0
        for letter in name:
            total += (ord(letter) - subtruction_constant)
        result += (total * (i + 1))
    return result


file_name = 'names.txt'

names = get_names(file_name)
names = sorted(names)

print(get_result(names))
