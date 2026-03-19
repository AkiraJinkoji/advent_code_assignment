"""
Day 3: Lobby
"""
def read_input(path):
    banks = [] 
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            banks.append([int(ch) for ch in line])
    return banks

def compute_output_joltage_part1(banks):
    joltage_tot = 0
    for b in banks:
        max_digit = b[0]
        max_joltage = 0
        for i in range(1,len(b)-1):
            digit = b[i]
            cand_joltage = max_digit*10 + digit 
            max_joltage = max(max_joltage, cand_joltage)
            max_digit = max(max_digit, digit)
        
        # for the last digit
        cand_joltage = max_digit*10 + b[-1]
        max_joltage = max(max_joltage, cand_joltage)

        joltage_tot += max_joltage
    
    return joltage_tot

def compute_output_joltage_part2(banks):
    joltage_tot = 0
    l = 12 # length of the final number
    for b in banks:
        to_turnon = []
        nbr_candidate = len(b)
        for x in b:    
            while nbr_candidate > l and to_turnon and to_turnon[-1] < x:
                to_turnon.pop()
                nbr_candidate-=1
            to_turnon.append(x)
        
        joltage = sum(to_turnon[k] * 10**(l-1-k) for k in range(l))
        joltage_tot += joltage
    
    return joltage_tot

if __name__ == "__main__":
    file_path = "challenge3/test_input.txt"
    banks = read_input(file_path)
    joltage1 = compute_output_joltage_part1(banks)
    joltage2 = compute_output_joltage_part2(banks)
    print(f"joltage part 1 is: {joltage1}")
    print(f"joltage part 2 is: {joltage2}")
