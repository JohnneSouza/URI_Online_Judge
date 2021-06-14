pi = 3.14159
sides_values_list = input().split()


def triangle(values):
    return f'TRIANGULO: {float(values[0]) * float((values[2])) / 2:.3f}'


def circle(values):
    return f'CIRCULO: {pi * float(values[2]) ** 2:.3f}'


def trapeze(values):
    return f'TRAPEZIO: {(float(values[0]) + float(values[1])) * float(values[2]) / 2:.3f}'


def square(values):
    return f'QUADRADO: {float(values[1]) ** 2:.3f}'


def rectangle(values):
    return f'RETANGULO: {float(values[0]) * float(values[1]):.3f}'


shapes = [triangle(sides_values_list),
          circle(sides_values_list),
          trapeze(sides_values_list),
          square(sides_values_list),
          rectangle(sides_values_list)]

for shape in shapes:
    print(shape)
