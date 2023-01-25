def hanoi(n, source, target, spare):
    if n == 1:
        print("Move disk", n, "from", source, "to", target)
    else:
        hanoi(n - 1, source, spare, target)
        print("Move disk", n, "from", source, "to", target)
        hanoi(n - 1, spare, target, source)


hanoi(3, "A", "B", "C")
