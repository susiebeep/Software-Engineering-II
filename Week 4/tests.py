import random
import unittest
from credit_card_validator import credit_card_validator

# Resources used: Luhn Algorithm, Wikipedia.org


def luhn(card_no):
    # count number of digits in credit card number
    card_length = int(len(card_no))

    # initialize checksum and count values
    checksum = 0
    valid_checksum = 0
    count = 0

    for i in range(0, card_length):
        # start at end of credit card number
        digit = int(card_no[card_length - 1 - i])

        # multiply every other digit by 2
        if count % 2 == 0:
            digit *= 2

        # if result of doubling the digit is greater than 9, subtract
        # 9 from the result
        if digit > 9:
            digit -= 9

        # sum the digits
        checksum += digit

        # add one to the count
        count += 1

    # multiply by 9 then take modulus 10
    valid_checksum = (checksum*9) % 10
    return valid_checksum


class TestCase(unittest.TestCase):
    # invalid credit card number prefix
    def test0(self):
        for i in range(0, 100):
            val = random.randint(600000000000000, 999999999999999)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # valid visa card number
    def test1(self):
        for i in range(0, 100):
            val = random.randint(400000000000000, 499999999999999)
            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # valid mastercard card number - 51 to 55
    def test2(self):
        for i in range(0, 100):
            val = random.randint(510000000000000, 559999999999999)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # valid mastercard card number - 2221 to 2720
    def test3(self):
        for i in range(0, 100):
            val = random.randint(222100000000000, 272099999999999)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # valid american express card number - 34
    def test4(self):
        for i in range(0, 100):
            val = random.randint(34000000000000, 34999999999999)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # valid american express card number - 37
    def test5(self):
        for i in range(0, 100):
            val = random.randint(37000000000000, 37999999999999)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # visa card number starting with 4052
    def test6(self):
        for i in range(0, 100):
            val = random.randint(405200000000000, 405299999999999)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # 1111 in a visa card number
    def test7(self):
        suffix = 1111
        for i in range(0, 100):
            prefix = random.randint(40000000000, 49999999999)
            val = str(prefix) + str(suffix)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # 1111 in a mastercard card number
    def test8(self):
        suffix = 1111
        for i in range(0, 100):
            prefix = random.randint(51000000000, 55999999999)
            val = str(prefix) + str(suffix)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # 1111 at end of american express card number
    def test9(self):
        suffix = 1111
        for i in range(0, 100):
            prefix = random.randint(3700000000, 3799999999)
            val = str(prefix) + str(suffix)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # 270 appearing twice in mastercard number (52 prefix)
    def test10(self):
        suffix = 5270
        for i in range(0, 100):
            prefix = random.randint(52700000000, 52709999999)
            val = str(prefix) + str(suffix)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # 270 appearing twice at the end of mastercard number (2221-2720 prefix)
    def test11(self):
        num = 270
        for i in range(0, 100):
            prefix = random.randint(222100000, 272099999)
            val = str(prefix) + str(num) + str(num)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # 270 appearing three times in a mastercard card number
    def test12(self):
        num = 270
        for i in range(0, 100):
            prefix = random.randint(270000000, 270999999)
            val = str(prefix) + str(num) + str(num)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # 270 appearing twice in a visa card number
    def test13(self):
        num = 270
        for i in range(0, 100):
            prefix = random.randint(427000000000, 427099999999)
            val = str(prefix) + str(num)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)

    # 270 appearing twice in an american express card number
    def test14(self):
        num = 270
        for i in range(0, 100):
            prefix = random.randint(34000000, 34999999)
            val = str(prefix) + str(num) + str(num)

            # calculate Luhn digit and append to get a valid credit card number
            checksum = luhn(str(val))
            card_no = str(val) + str(checksum)
            credit_card_validator(card_no)


if __name__ == '__main__':
    unittest.main()
