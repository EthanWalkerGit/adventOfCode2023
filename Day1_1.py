import numpy as np

file_path = "list.txt"
with open(file_path, "r") as file:
    input_list = [line.strip() for line in file]
total = 0

for cali in input_list:
    section = []

    for i, x in enumerate(cali):
        if x != " " and x.isdigit():
            if len(section) == 2:
                section = section[:1]
            section.append(int(x))
        elif x == " ":
            if len(section) == 1:
                section.append(section[0])  # If only one digit, duplicate it
            # Concatenate the digits to form a number and add to total
            total += int("".join(map(str, section)))

    # If only one digit is found at the end, duplicate it
    if len(section) == 1:
        section.append(section[0])

    # Concatenate the digits of the last section to form a number and add to total
    total += int("".join(map(str, section)))

    # Print current results
    print(f"Current total: {total}, Current section: {section}")
    section = []  # Reset the section

# Print the final total
print(f"Final total: {total}")
