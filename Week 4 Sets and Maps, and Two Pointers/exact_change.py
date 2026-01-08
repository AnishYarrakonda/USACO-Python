# 1-18 cow coins each up to 10**18 (don't have to be distinct)
# What are the total number of ways Bessie can pay with exact change (total number of sums)

N = int(input().strip())
cis = list(map(int, input().strip().split()))

unique_sums = set()
def nested_for_loop(idx=0, current_sum=0):
    for val in [0, 1]:          # Either add or don't add
        new_sum = current_sum   # define new_sum for each iteration
        if val:                 # If true:
            new_sum = current_sum + cis[idx] # then we add the value of the current coin to new_sum
        if idx == N-1:          # base case
            unique_sums.add(new_sum)    # add the final branch to the set
        else:                   # recursive call
            nested_for_loop(idx+1, new_sum) # call the function to split into 2 more branches

nested_for_loop()
print(len(unique_sums)-1)