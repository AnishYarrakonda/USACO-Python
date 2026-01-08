N = int(input().strip())
songs = list(map(int, input().strip().split()))

left, largest, window= 0, 0, set()
for right in range(N):
    while songs[right] in window:
        window.remove(songs[left])
        left += 1
    window.add(songs[right])
    largest = max(right - left + 1, largest)
print(largest)