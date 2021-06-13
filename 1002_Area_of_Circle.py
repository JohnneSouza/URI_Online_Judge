pi = 3.14159
radius = float(input())


def area(pi_value, radius_value):
    return pi_value * (radius_value ** 2)


result = round(area(pi, radius), 4)

print(f'A={result:.4f}')
