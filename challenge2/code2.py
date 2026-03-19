"""
Day 2: Gift Shop
"""

def read_input(file_path):
    ranges = []
    with open(file_path) as f:
        content = f.read().strip()

    for r in content.split(","):
        r = r.strip()
        if not r:
            continue

        rmin, rmax = r.split("-")
        ranges.append((int(rmin), int(rmax)))
    
    return ranges

def adjust_to_even_digits(num, min_or_max = "min"):
    digits = len(str(abs(num)))
    if digits%2 == 0:
        return num, digits
    
    if min_or_max == "min":
        return 10**(digits), digits+1
    else:
        return 10**(digits-1)-1, digits-1

    
def compute_sum_invalidID_part1(ranges):
    res = 0

    for (rmin, rmax) in ranges:
        # print(f"solving range {rmin}-{rmax}")

        # find the min and max with even nbr of digits, return them with their number of digits
        orig_min, orig_max = rmin, rmax
        adj_min, kmin = adjust_to_even_digits(rmin, "min")
        adj_max, kmax = adjust_to_even_digits(rmax, "max")
        # case1 :  the bounds have the same number of digits 
        if kmax == kmin:
            k_half = int(kmax/2)
            boundmin = int(adj_min // (10**(k_half))) 
            boundmax = int(adj_max // (10**(k_half)))
            candidates = [x*(10**(k_half)) + x for x in range(boundmin, boundmax+1)]

        # case2 :  the bounds don't have the same number of digits
        else:
            candidates = []
            for k_half in range(kmin//2, (kmax//2)+1):
                if k_half == int(kmin/2):
                    boundmin = int(adj_min // (10**(k_half)))
                    boundmax = int(10**(k_half))
                elif k_half == int(kmax/2):
                    boundmin = int(10**(k_half-1))
                    boundmax = int(adj_max // (10**(k_half)))
                else:
                    boundmin = int(10**(k_half-1))
                    boundmax = int(10**(k_half))
                   
                candidates += [x*(10**(k_half)) + x for x in range(boundmin, boundmax)]
        
        # eliminate candidates that are not in the range
        sum_range = 0
        for c in candidates:
            if orig_min <= c <= orig_max:
                sum_range += c
        
        res += int(sum_range)
    
    return res

def get_seq_formats(k): 
    """Return all (sequence_length, repetition_count) pairs for a k-digit pattern."""
    seq_format = [] 
    for i in range(1,k):
        if k % i == 0:
            seq_format.append((i, int(k/i)))
    
    return seq_format

def compute_sum_invalidID_part2(ranges):
    res = 0
    
    for (rmin, rmax) in ranges:
        # print(f"-------- range: {(rmin, rmax)} ------------")
        candidates = []
        kmin = len(str(abs(rmin)))
        kmax = len(str(abs(rmax)))

        if kmin == kmax:
            seq = get_seq_formats(kmin)
            # print(f"number of digit: {kmin}; sequences are (len, reqetitions): {seq} \n")
            for (sl, sn) in seq:
                boundmin = int(rmin // (10**(sl*(sn-1))) )
                boundmax = int(rmax // (10**(sl*(sn-1))))
                candidates += [sum(x*10**(sl*i) for i in range(sn)) 
                              for x in range(boundmin, boundmax+1)]

        else:
            for k in range(kmin, kmax+1):
                seq = get_seq_formats(k)
                # print(f"number of digit: {k}; sequences are (len, reqetitions): {seq} \n")
                if k == kmin:
                    for (sl, sn) in seq:
                        boundmin = int(rmin // (10**(sl*(sn-1))))
                        boundmax = int(10**(sl)-1)
                        candidates += [sum(x*10**(sl*i) for i in range(sn)) 
                              for x in range(boundmin, boundmax+1)]
                elif k == kmax:
                    for (sl, sn) in seq:
                        boundmin = int(10**(sl-1))
                        boundmax = int(rmax // (10**(sl*(sn-1))))
                        candidates += [sum(x*10**(sl*i) for i in range(sn)) 
                                for x in range(boundmin, boundmax+1)]
                else:
                    for (sl, sn) in seq:
                        boundmin = int(10**(sl-1))
                        boundmax = int(10**(sl)-1)
                        candidates += [sum(x*10**(sl*i) for i in range(sn)) 
                                for x in range(boundmin, boundmax+1)]
        
        # eliminate candidates that are not in the range
        candidates_set = set(candidates)
        # print(f"candidates are: {candidates_set}")
        sum_range = 0
        valid_cand = []
        for c in candidates_set:
            if rmin <= c <= rmax:
                valid_cand.append(c)
                sum_range += c
        # print(f"valid cadidate: {valid_cand} \n")
        res += int(sum_range)
    
    return res
        
if __name__ == "__main__":
    file_path = "challenge2/test_input.txt"
    ranges = read_input(file_path)
    res1 = compute_sum_invalidID_part1(ranges)
    res2 = compute_sum_invalidID_part2(ranges)
    print(f"The sum is: {res1}")
    print(f"The sum is: {res2}")