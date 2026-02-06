n, s = map(int, input().split())
# Here's a nice built-in way to do it!
s_as_binary = format(s, 'b')
i = 1
while i <= len(s_as_binary) and s_as_binary[-i] == '0':
    i += 1
num_bits_after_rightmost_1 = i-1
print(n - num_bits_after_rightmost_1)