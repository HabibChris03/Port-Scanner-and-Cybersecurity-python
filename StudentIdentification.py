val = []
values = input("Enter 9 digit number: ")

if len(values) == 9 and values.isdigit():
    num = list(values)  # Convert string to list of characters
    indexes = [3, 5]  # Positions to insert hyphens (0-based index)
    result = ""  # Initialize result string

    for i in range(len(num)):
        result += num[i]  # Add current digit
        if i in indexes:  # Check if we need to add hyphen after this position
            result += "-"

    print(result)
else:
    print("Please enter exactly 9 digits")