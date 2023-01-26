def hanoi(n, source, target, spare):
    if n == 1:
        print("Move disk", n, "from", source, "to", target)
    else:
        hanoi(n - 1, source, spare, target)
        print("Move disk", n, "from", source, "to", target)
        hanoi(n - 1, spare, target, source)


hanoi(3, "A", "B", "C")


def moveTower(height, fromPole, toPole, withPole):
    # add code here
    # call moveDisk in your function call.
    if height == 1:
        moveDisk(fromPole, toPole)

    else:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)


disks = int(input("Enter the number of disks:\n"))
moveTower(disks, "A", "B", "C")