# Python program that computes the approximate grade level needed to comprehend some text.

L = S = 0
W = 1

text = input("Text: ")

for char in text:
    if char.isalpha():
        L += 1
    if char.isspace():
        W += 1
    if char in [".", "!", "?"]:
        S += 1

print(f"{L} letter(s)")
print(f"{W} word(s)")
print(f"{S} sentence(s)")

L = ((L / W) * 100)
S = ((S / W) * 100)
index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    print("Before Grade 1")
elif index > 15:
    print("Grade 16+")
else:
    print(f"Grade {index}")
