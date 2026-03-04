rooms25 = {i: i for i in range(1, 96)}
rooms25.update({f'П{i}': i + 95 for i in range(1, 5)})
k = 99
for i in range(1, 13):
    rooms25.update({f'П{i + 2}-1': i + k})
    k += 1
    rooms25.update({f'П{i + 2}-2': i + k})

rooms29 = {i: i + 123 for i in range(1, 91)}
rooms29.update({f'Пм{i}': i + 213 for i in range(1, 18)})
rooms29.update({f'Пм{i}': i + 212 for i in range(19, 46)})
rooms29.update({'П3': 258})

if __name__ == '__main__':
    print(rooms25)