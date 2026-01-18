IMPOSSIBLE = -1

def solve(program, kd, kl, kr, ku):
    hgood_count, hbad_count, vgood_count, vbad_count = 0, 0, 0, 0
    # We are going to reframe the problem such that the robot is currently
    #   to the right of (or on) the y-axis, and above (or on) the x-axis.
    # So left and up are our "good" directions 
    hgood_ok = kl
    hbad_ok = kr
    vgood_ok = kd
    vbad_ok = ku
    for c in program:
        if c == 'L':
            hgood_count += 1
        elif c == 'R':
            hbad_count += 1
        elif c == 'D':
            vgood_count += 1
        elif c == 'U':
            vbad_count += 1
    hdev = hbad_count - hgood_count
    # If the final location is left of the y-axis, exchange L and R so left
    #   is the new right.
    if hdev < 0:
        hdev *= -1
        hgood_ok, hbad_ok = hbad_ok, hgood_ok
        hgood_count, hbad_count = hbad_count, hgood_count
    vdev = vbad_count - vgood_count
    # If the final location is below the x-axis, exchange U and D so down
    #   is the new up.
    if vdev < 0:
        vdev *= -1
        vgood_ok, vbad_ok = vbad_ok, vgood_ok
        vgood_count, vbad_count = vbad_count, vgood_count
    # We also want the horizontal deviation to be no smaller than the
    #   vertical deviation.
    if hdev < vdev:
        hdev, vdev = vdev, hdev
        hgood_ok, hbad_ok, vgood_ok, vbad_ok = (
            vgood_ok, vbad_ok, hgood_ok, hbad_ok)
        hgood_count, hbad_count, vgood_count, vbad_count = (
            vgood_count, vbad_count, hgood_count, hbad_count)
    # OK, now we can get solving!
    if (hdev + vdev) % 2 == 1:
        return IMPOSSIBLE # As discussed in class
    if hdev == 0 and vdev == 0:
        return 0 # No need to change anything!
    if hgood_ok and vgood_ok: # L and D available
        # Same strategy as in class!
        return (hdev + vdev) // 2
    elif (not hgood_ok) and (not vgood_ok): # Neither L nor D available
        return IMPOSSIBLE
    elif hgood_ok: # L available, D unavailable
        return (hdev + vdev) // 2
    else: # L unavailable, D available
        if (hdev == vdev) or vbad_ok:
            return hdev
        else:
            return IMPOSSIBLE

t = int(input().strip())
for tt in range(t):
    n, kd, kl, kr, ku = map(int, input().split())
    program = input()
    print(solve(program, kd, kl, kr, ku))