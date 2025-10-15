val = []  # Move outside the loop

for i in range(5):
    values = int(input(f"Enter value {i+1}: "))  # Fixed parentheses and added colon
    val.append(values)

total = int(sum(val))
total_float = float(sum(val))
total_string = ''.join(str(x) for x in val)
print(f'Integer:{total}')
print(f'Float:{total_float}')
print(f'String:{total_string}')
