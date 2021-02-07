# Name: Jennifer Daniels
# Assignment: HW3
# Description: Program performs tests on function contrived_func
# using random testing method

from credit_card_validator import credit_card_validator
import random
import string
import unittest

class TestCase(unittest.TestCase):
    pass

def build_test_func(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result, message.format(test_case, expected, result))
    return test

def generate_testcases(tests_to_generate=100):
    for i in range(tests_to_generate):
        expected = True
        # visa_prefix
        v_prefix = random.randint(4)
        m_prefix_set = random.randint(51, 55)
        m_prefix_set2 = random.randint(2221, 2720)
        ae_prefix_start = random.randint(34, 34)
        # length test
        # length_test = [0, 14, 15, 16, 17]
        length_test = [16]
        # 50% chance of generating an edge case
        # odds = random.randint(0,1)
        # if odds == 1:
        #     length = random.choice(edge_cases)
        # else:
        #     # Random length
        #     length = random.randint(0,30)



        # Random number of lower case
        low = random.randint(0, length)
        # Random number of upper case
        up = random.randint(0, length - low)
        # Random number of numbers
        dig = random.randint(0, length - low - up)
        # Random number of symbols
        sym = random.randint(0, length - low - up - dig)
        # Determine final length of string
        length = low + up + dig + sym
        # Set expected result based on specification
        if length < 15 or length > 20:
            expected = False
        if low < 1 or up < 1 or dig < 1 or sym < 1:
            expected = False
        # Generate credit card
        pwd = gen_creditcard(length, low, up, dig, sym)
        # Build test function
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, pwd, check_pwd, message)
        setattr(TestCase, 'test_{}'.format(pwd), new_test)

def gen_creditcard(length=16, low=1, up=1, dig=1, sym=1, spa=False):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    all_pos = lower_case + upper_case + digits + symbols

    pwd = ''
    pwd = pwd + ''.join(random.choice(lower_case) for i in range(low))
    pwd = pwd + ''.join(random.choice(upper_case) for i in range(up))
    pwd = pwd + ''.join(random.choice(digits) for i in range(dig))
    pwd = pwd + ''.join(random.choice(symbols) for i in range(sym))
    pwd = pwd + ''.join(random.choice(all_pos) for i in range(length - len(pwd)))

    return ''.join(random.sample(pwd,len(pwd)))

if __name__ == '__main__':
    generate_testcases()
    unittest.main()