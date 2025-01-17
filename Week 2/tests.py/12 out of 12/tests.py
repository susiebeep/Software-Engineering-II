import unittest
from credit_card_validator import credit_card_validator

# For each test case, I generated the credit card numbers using Luhn checksum
# validator/generator:
# https://evilacid.com/luhn-checksum-validator-generator
# I generated the test cases using a selection of the test frames generated
# by TSLgenerator and manually (error guessing, boundary values). I created
# a specs file with length and prefix constraints to generate 16 test cases,
# then used error guessing to generate the rest. I feel I may have had too
# many constraints in my specs file which is why I was unable to replicate
# the 35 test cases which were generated by the instructor


class TestCase(unittest.TestCase):
    # Invalid American Express length (too short)- length 14, prefix 34
    def test_1(self):
        cardNum = 34890589408586
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid American Express length (too long) - length 16, prefix 37
    def test_2(self):
        cardNum = 3783838290492834
        self.assertFalse(credit_card_validator(cardNum))

    # Valid American Express length - length 15, prefix 34
    def test_3(self):
        cardNum = 348710375931230
        self.assertTrue(credit_card_validator(cardNum))

    # Valid American Express length - length 15, prefix 37
    def test_4(self):
        cardNum = 379350123768659
        self.assertTrue(credit_card_validator(cardNum))

    # Invalid American Express prefix (edge case) - prefix 33, length 15
    def test_5(self):
        cardNum = 338964839082641
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid American Express prefix (edge case) - prefix 38, length 15
    def test_6(self):
        cardNum = 389287109264584
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid American Express prefix (edge case) - prefix 35, length 15
    def test_7(self):
        cardNum = 354789091845685
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid MasterCard length (too short) - length 15, prefix 51
    def test_8(self):
        cardNum = 519382903890297
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid MasterCard length (too long) - length 17, prefix 52
    def test_9(self):
        cardNum = 52857309817458342
        self.assertFalse(credit_card_validator(cardNum))

    # Valid MasterCard length - length 16, prefix 53
    def test_10(self):
        cardNum = 5308275610268761
        self.assertTrue(credit_card_validator(cardNum))

    # Invalid MasterCard prefix (edge case) - prefix 50, length 16
    def test_11(self):
        cardNum = 5013857392018377
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid MasterCard prefix (edge case) - prefix 56, length 16
    def test_12(self):
        cardNum = 5683620283747507
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid MasterCard prefix (edge case) - prefix 2220, length 16
    def test_13(self):
        cardNum = 2220784937123981
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid MasterCard prefix (edge case) - prefix 2721, length 16
    def test_14(self):
        cardNum = 2721749302738451
        self.assertFalse(credit_card_validator(cardNum))

    # Valid MasterCard prefix (edge value) - length 16, prefix 51
    def test_15(self):
        cardNum = 5182395783901260
        self.assertTrue(credit_card_validator(cardNum))

    # Valid MasterCard prefix (edge value) - length 16, prefix 55
    def test_16(self):
        cardNum = 5591749366849269
        self.assertTrue(credit_card_validator(cardNum))

    # Valid MasterCard prefix (edge value) - length 16, prefix 2221
    def test_17(self):
        cardNum = 2221953865823511
        self.assertTrue(credit_card_validator(cardNum))

    # Valid MasterCard prefix (edge value) - length 16, prefix 2720
    def test_18(self):
        cardNum = 2720349856491176
        self.assertTrue(credit_card_validator(cardNum))

    # Valid MasterCard prefix (middle value) - length 16, prefix 52
    def test_19(self):
        cardNum = 5287493012884599
        self.assertTrue(credit_card_validator(cardNum))

    # Valid MasterCard prefix (middle value) - length 16, prefix 54
    def test_20(self):
        cardNum = 5491678230717587
        self.assertTrue(credit_card_validator(cardNum))

    # Valid MasterCard prefix (middle value) - length 16, prefix 2345
    def test_21(self):
        cardNum = 2345987610293456
        self.assertTrue(credit_card_validator(cardNum))

    # Valid MasterCard prefix (middle value) - length 16, prefix 2222
    def test_22(self):
        cardNum = 2222678489193764
        self.assertTrue(credit_card_validator(cardNum))

    # Valid MasterCard prefix (middle value) - length 16, prefix 2719
    def test_23(self):
        cardNum = 2719784692645127
        self.assertTrue(credit_card_validator(cardNum))

    # Invalid Visa length (too short) - length 15, prefix 4
    def test_24(self):
        cardNum = 418290468291011
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid Visa length (too long) - length 17, prefix 4
    def test_25(self):
        cardNum = 48729051823659786
        self.assertFalse(credit_card_validator(cardNum))

    # Valid Visa length - length 16, prefix 4
    def test_26(self):
        cardNum = 4821995366103877
        self.assertTrue(credit_card_validator(cardNum))

    # Invalid Credit Card Prefix - prefix 1, length 15
    def test_27(self):
        cardNum = 123456789123458
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid Credit Card Prefix - prefix 7, length 15
    def test_28(self):
        cardNum = 712345678912344
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid Checksum (Visa)
    def test_29(self):
        cardNum = 4829034582310297
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid Checksum (MasterCard)
    def test_30(self):
        cardNum = 5498102938402345
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid Checksum (MasterCard)
    def test_31(self):
        cardNum = 2222333344445558
        self.assertFalse(credit_card_validator(cardNum))

    # Invalid Checksum (American Express)
    def test_32(self):
        cardNum = 379374950123391
        self.assertFalse(credit_card_validator(cardNum))

    # Empty credit card number
    def test_33(self):
        cardNum = ""
        self.assertFalse(credit_card_validator(cardNum))

if __name__ == '__main__':
    unittest.main()
