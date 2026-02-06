import itertools

def overlap(rect1, rect2):
    if rect1 == 0 or rect2 == 0:
        return 0
    # Make the rectangle with the leftmost LL corner be "rectangle 1"
    # Break ties by lowermost LL corner
    if (rect2[0] < rect1[0] or
        (rect2[0] == rect1[0] and rect2[1] < rect1[1])):
        rect1, rect2 = rect2, rect1
    a1, b1, c1, d1 = rect1
    a2, b2, c2, d2 = rect2
    if c1 <= a2:
        return 0
    left_x = max(a1, a2)
    right_x = min(c1, c2)
    if ((d2 <= b1) or (d1 <= b2)):
        return 0
    bottom_y = max(b1, b2)
    top_y = min(d1, d2)
    return (left_x, bottom_y, right_x, top_y)

def area(rect):
    if rect == 0:
        return 0
    a, b, c, d = rect
    return (c-a) * (d-b)

n = int(input())
rects = []
for _ in range(n):
    rects.append(list(map(int, input().split())))

answer = 0
# find all overlaps
for which_rects in itertools.product([True, False], repeat=n):
    overlap_so_far = [-10**7, -10**7, 10**7, 10**7]
    for i in range(n):
        if which_rects[i]:
            overlap_so_far = overlap(overlap_so_far, rects[i])
    num_rects = which_rects.count(True)
    if num_rects > 0:
        overlap_area = area(overlap_so_far)
        # Overlaps of an odd number of rectangles contribute to our total.
        # Overlaps of an even number of rectangles subtract from it.
        if num_rects % 2 == 0:
            overlap_area *= -1
        answer += overlap_area
print(answer)