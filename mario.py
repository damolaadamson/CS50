# Python program to create two pyramids of blocks, the first right-aligned and the other left-aligned with a gap
# between them, similar to those seen in Nintendo’s Super Mario Brothers Mario, where Mario must ascend the
# right-aligned pyramid, hop over the gap, and descend the left-aligned pyramid.

while True:
    h = int(input("Height: "))
    if 0 < h < 9:
        break

for i in range(h):
    print(" " * (h - i - 1) + "#" * (i + 1) + "  " + "#" * (i + 1))
print(end = "")
