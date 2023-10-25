import random

def split(name):
    P = 6200082418925520492022105720662335761613 # some random large number
    secret = int(input(f"Enter {name}'s health secret (it must be of type int): "))
    print("\n")
    n = random.randint(0,P)
    m = random.randint(0,P)
    split_share = secret//3
    remainder = secret % 3
    shares = []
    shares.append(split_share + n + remainder)
    shares.append(split_share + m)
    shares.append(split_share - m - n)
    #print(f"secret share 1 = {s1}, secret 2 = {s2}, secret 3 = {s3}. The sum is {s1+s2+s3}")
    return shares
