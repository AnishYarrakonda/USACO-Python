# function that performs a greedy assignment of 1's and 0's
def greedy(bit):
    b_string = [0]                          # extra zero to prevent out of bounds indexing

    parity = 0                              # track the parity of the window
    for _ in range(K-1):                    # until one num before the end of the first window
        b_string.append(bit)                # start off by adding 0's or 1's based on min or max
        parity += bit                       # update parity accordingly

    for i, num in enumerate(B):             # iterate through the b_string

        parity -= b_string[i]               # remove the value that we slid past on the left endpoint of the window

        # use XOR to add a 1 if parity must be flipped or 0 if parity is the same
        # case 1:  (1, 1) or (0, 0) -> no change in parity so add a 0
        # case 2:  (0, 1) or (1, 0) -> there is a change in parity so add a 1
        b_string.append((parity & 1) ^ num)

        parity += b_string[-1]              # update parity with the new value that entered the window

    return b_string.count(1)                # return the number of 1's

T = int(input())                            # number of subcases

for _ in range(T):                          # loop through each subcase
    # read in input
    N, K = map(int, input().split())
    B = list(map(int, list(input())))

    print(greedy(0), greedy(1))             # print results from function for min and max number of 1's