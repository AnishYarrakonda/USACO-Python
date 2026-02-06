def max_area(rects):
    total_area = 0
    for wi, hi in rects:
        total_area += wi * hi
    return total_area

def min_area(rects):
    # First, get rid of any rectangle that is dominated by some other
    #   rectangle. We just build up a new list instead of popping from
    #   within the existing list, which can be expensive.
    pruned_rects = []
    # We sort the existing list (by increasing wi, with hi as a tiebreaker)
    #   first, to ensure that if a rectangle A is dominated by another
    #   rectangle B, then B appears later in the list.
    rects.sort()
    for i in range(len(rects)):
        save = True
        for j in range(i+1, len(rects)):
            # We already know the order of the widths, so we just need to
            #   compare the heights.
            if (rects[i][1] <= rects[j][1]):
                # this rectangle is dominated; we can ignore it
                save = False
                break
        if save:
            pruned_rects.append(rects[i])
    # Now use the "chunking" method as explained in the analysis.
    total_area = 0
    prev_width = 0
    for wi, hi in pruned_rects:
        total_area += (wi - prev_width) * hi
        prev_width = wi
    return total_area

t = int(input())
for _ in range(t):
    n, a = map(int, input().split())
    rects = [list(map(int, input().split())) for _ in range(n)]
    # Find the max area first because that function is nondestructive
    #  (does not alter the list of rectangles)
    mx = max_area(rects)
    mn = min_area(rects)
    print("YES" if (mn <= a <= mx) else "NO")