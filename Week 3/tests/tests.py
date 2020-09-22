import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):

    # test first condition (first if):
    #       val<150 is true, val>100 is true, outcome is true
    def test_1(self):
        val = 120
        self.assertTrue(contrived_func(val))

    # test first condition (first if):
    #       val<150 is true, val>100 is false, outcome is false
    # test second condition (first elif):
    #       val*5<361 is true, val/2<24 is true, outcome is true
    # test third condition (second if):
    #       val==6 is false, outcome is true
    def test_2(self):
        val = 40
        self.assertTrue(contrived_func(val))

    # test first condition (first if):
    #       val<150 is false, val>100 is true, outcome is false
    # test second condition (first elif):
    #       val*5<361 is false, outcome is false
    # test fourth condition (second elif):
    #       val>75 true, val/8<10 false, val**val%5==0 true, outcome true
    def test_3(self):
        val = 160
        self.assertTrue(contrived_func(val))

    # test first condition (first if):
    #       val<150 is true, val>100 is false, outcome is false
    # test second condition (elif):
    #       val*5<361 is true, val/2<24 is true, outcome is true
    # test third condition (second if):
    #       val==6 is true, outcome is false
    def test_4(self):
        val = 6
        self.assertFalse(contrived_func(val))

    # test first condition (first if):
    #       val<150 is true, val>100 is false, outcome is false
    # test second condition (first elif):
    #       val*5<361 is true, val/2<24 is false, outcome is false
    # test fourth condition (second elif):
    #       val>75 false, val/8<10 true, val**val%5==0 true, outcome true
    def test_5(self):
        val = 50
        self.assertTrue(contrived_func(val))

    # test first condition (first if):
    #       val<150 is true, val>100 is false, outcome is false
    # test second condition (first elif):
    #       val*5<361 is false, outcome is false
    # test fourth condition (second elif, or):
    #       val>75 true, val/8<10 false, val**val%5==0 true, outcome true
    def test_6(self):
        val = 100
        self.assertTrue(contrived_func(val))

    # test first condition (first if):
    #       val<150 is true, val>100 is false, outcome is false
    # test second condition (first elif):
    #       val*5<361 is true, val/2<24 is false, outcome is false
    # test fourth condition (second elif):
    #       val>75 false, val/8<10 true, val**val%5==0 false, outcome false
    def test_7(self):
        val = 161
        self.assertFalse(contrived_func(val))

    # test first condition (first if):
    #       val<150 is true, val>100 is false, outcome is false
    # test second condition (first elif):
    #       val*5<361 is true, val/2<24 is false, outcome is false
    # test fourth condition (second elif):
    #       val>75 false, val/8<10 true, val**val%5==0 false, outcome false
    def test_8(self):
        val = 51
        self.assertFalse(contrived_func(val))


if __name__ == '__main__':
    unittest.main()
