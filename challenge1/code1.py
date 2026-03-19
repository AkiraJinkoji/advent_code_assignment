"""
Day 1: Secret Entrance
"""

def read_input(file_path: str):
    instructions = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            direction = line[0]
            dist = int(line[1:])
            instructions.append((direction, dist))
    
    return instructions

def compute_password_part1(instructions):
    dial = 50
    password = 0

    for rot in instructions:
        if rot[0] == 'R':
            sign = 1
        else:
            sign = -1
        dial = (dial + sign * rot[1]) %100

        if dial == 0:
            password += 1
    
    return password

def compute_password_part2(instructions):
    dial = 50
    password = 0

    for rot in instructions:
        if rot[0] == 'R':
            password += (dial + rot[1]) // 100 - dial //100
            dial += rot[1]
        else:
            password +=  (dial - 1) //100 -(dial - rot[1] - 1) // 100
            dial -= rot[1]
        # print(f"dial: {dial},  pw: {password}")
        dial = dial %100 # to keep the value low
    return password

if __name__ == "__main__":
    input_file_path = "challenge1\test_input.txt"
    instructions = read_input(input_file_path)
    pw1 = compute_password_part1(instructions)
    pw2 = compute_password_part2(instructions)
    print(f"The password for part 1 is: {pw1}")
    print(f"The password for part 2 is: {pw2}")