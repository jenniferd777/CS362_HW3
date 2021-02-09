# Name: Jennifer Daniels
# Assignment: HW3
# Description: Program performs tests on function contrived_func
# using random testing method

# Function being tested
from credit_card_validator import credit_card_validator
import random
import unittest


class TestCase(unittest.TestCase):
    """
    Class contains methods that generate random numbers for Visa,
    Master, and American Express credit cards. Credit card numbers
    are generated with lengths of 14 - 17, set prefixs, and random.
    Visa credit card:
     prefix: 4
    Master credit card:
     prefix: 51-55
     prefix: 2221 - 2720
    American Express:
     prefix: 34
     prefix: 37
    """

    def test_generate_testcases(self):
        """
        Method iterates through each type of credit card with correct
        length and performs 100000 iterations. A random test is
        performed on different lengths and 100000 iterations
        """
        c_length = [14, 15, 16, 17]
        for i in range(0, 4):
            for j in range(100000):
                if i == 0:
                    credit_card_num = self.v_card(15)
                elif i == 1:
                    credit_card_num = self.m_card(14)
                elif i == 2:
                    credit_card_num = self.e_card(13)
                elif i == 3:
                    c_choice = random.choice(c_length)  # chooses length
                    credit_card_num = self.rnd_card(c_choice)
                # passed credit card number into test function
                credit_card_validator(credit_card_num)
                print('Failure: {} should be {}'.format(credit_card_num, True))

    def v_card(self, v_len):
        """
        Generates and returns Visa credit card, length 16, and prefix 4
        """
        v_num = ''
        for j in range(v_len):
            # generates and combines credit card number
            v_num = v_num + ''.join(str(random.randint(0, 9)))
            # combines prefix and generated numbers
        v_card_num = "4" + ''.join(v_num)
        return v_card_num

    def m_card(self, m_len):
        """
        Generates and returns Master credit card, length 16,
        and random prefixes from 51-55 and 2221-2720.
        """
        # 50% choice for choosing initial prefix
        m_prefix = random.randint(0, 1)
        if m_prefix == 0:
            s_prefix = random.randint(2221, 2720)
            m_num = ''
            for j in range(m_len-2):
                # generates and combines credit card number
                m_num = m_num + ''.join(str(random.randint(0, 9)))
            # combines prefix and generated numbers
            m_card_num = str(s_prefix) + ''.join(m_num)
        else:
            s_prefix = random.randint(51, 55)
            m_num = ''
            for j in range(m_len):
                # generates and combines credit card number
                m_num = m_num + ''.join(str(random.randint(0, 9)))
            # combines prefix and generated numbers
            m_card_num = str(s_prefix) + ''.join(m_num)
        return m_card_num

    def e_card(self, e_len):
        """
        Generates and returns American Express credit card,
        length 16, and random prefixes 34 and 37.
        """
        # 50% choice for choosing initial prefix
        e_prefix = random.randint(0, 1)
        if e_prefix == 0:
            e_num = ''
            for j in range(e_len):
                # generates and combines credit card number
                e_num = e_num + ''.join(str(random.randint(0, 9)))
            # combines prefix and generated numbers
            e_card_num = "34" + ''.join(e_num)
        else:
            e_num = ''
            for j in range(e_len):
                # generates and combines credit card number
                e_num = e_num + ''.join(str(random.randint(0, 9)))
            # combines prefix and generated numbers
            e_card_num = "37" + ''.join(e_num)
        return e_card_num

    def rnd_card(self, rnd_len):
        """
        Generates and returns random credit of various lengths and
        prefixes.
        """
        rnd_num = ''
        for j in range(rnd_len):
            # generates and combines credit card number
            rnd_num = rnd_num + ''.join(str(random.randint(0, 9)))
        # combines prefix and generated numbers
        rnd_card_num = rnd_num
        return rnd_card_num


if __name__ == '__main__':
    unittest.main()
