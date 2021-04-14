# A Python program that asks the user for a credit or debit card number then uses Luhn's Algorithm to determine if the
# number is valid and letting the user know if it is an American Express, Mastercard, or Visa card number.

def main():
    while True:
        card_number = int(input("Card Number: "))
        if card_number > 0:
            break

    card_length = len(str(card_number))
    if (checksum(card_number, card_length) == 0) and (card_length == 13 or card_length == 15 or card_length == 16):
        if 340000000000000 <= card_number < 350000000000000:
            print("AMEX")
        elif 370000000000000 <= card_number < 380000000000000:
            print("AMEX")
        elif 5100000000000000 <= card_number < 5600000000000000:
            print("MASTERCARD")
        elif 4000000000000 <= card_number < 5000000000000:
            print("VISA")
        elif 4000000000000000 <= card_number < 5000000000000000:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")

def checksum(card_number, card_length):
    total = 0
    for i in range(card_length):
        if (i % 2) == 0:
            total += card_number % 10
            card_number //= 10
        else:
            digit = 2 * (card_number % 10)
            total += (digit // 10) + (digit % 10)
            card_number //= 10

    return total % 10

main()
