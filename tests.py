# Name: Jennifer Daniels
# Assignment: HW3
# Description: Program performs tests on function contrived_func
# using random testing method


from credit_card_validator import credit_card_validator
import random
import unittest


class TestCase(unittest.TestCase):
    pass


def build_test_func(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result,
                         message.format(test_case, expected, result))

    return test


def v_card():
    v_length = [00000000000000, 99999999999999, 000000000000000,
                999999999999999, 0000000000000000, 9999999999999999]
    v_length_cases = [0, 2, 4]
    v_length_choice = random.choice(v_length_cases)
    v_card_num = "4" + ''.join(str(random.
                                   randint(v_length[v_length_choice],
                                           v_length[v_length_choice + 1])))

    return v_card_num


def m_card():
    m_length_1 = [00000000000, 99999999999, 000000000000,
                  999999999999, 0000000000000, 9999999999999]
    m_length_2 = [0000000000000, 9999999999999, 00000000000000,
                  99999999999999, 000000000000000, 999999999999999]
    m_length_cases = [0, 2, 4]
    m_length_choice = random.choice(m_length_cases)
    m_prefix = random.randint(0, 1)
    if m_prefix == 0:
        s_prefix = random.randint(2221, 2720)
        m_card_num = str(s_prefix) + ''.join(str(random.
                         randint(m_length_1[m_length_choice],
                                 m_length_1[m_length_choice + 1])))
    else:
        s_prefix = random.randint(51, 55)
        m_card_num = str(s_prefix) + ''.join(str(random.
                         randint(m_length_2[m_length_choice],
                                 m_length_2[m_length_choice + 1])))

    return m_card_num


def e_card():
    e_length = [0000000000000, 9999999999999, 00000000000000,
                99999999999999, 000000000000000, 999999999999999]
    e_length_cases = [0, 2, 4]
    e_length_choice = random.choice(e_length_cases)
    e_card_num = "4" + ''.join(str(random.
                       randint(e_length[e_length_choice],
                               e_length[e_length_choice + 1])))

    return e_card_num


# def rnd_card():
#     c_length = [00000000000000, 99999999999999, 000000000000000,
#                 999999999999999, 0000000000000000, 9999999999999999,
#                 00000000000000000, 99999999999999999]
#     c_length_cases = [0, 2, 4, 6]
#     c_length_choice = random.choice(c_length_cases)
#     c_card_num = "4" + ''.join(str(random.
#                        randint(c_length[c_length_choice],
#                                c_length[c_length_choice + 1])))
#
#     return c_card_num

def luhn_calc(c_num, c_len):

    if len(c_num) == c_len:
        sum = 0
        for i in range(c_len-1):
            if i % 2 == 0:
                sum = sum + int(c_num[i])
            else:
                sum += int(c_num)
        sum = sum % 10
        sum = (c_len - sum)
        if c_num == sum:
            return True
        else:
            return False
    else:
        return False


def generate_testcases(tests_to_generate=10000):
    for i in range(tests_to_generate):
        expected = True
        c_case_choice = random.randint(1, 4)
        message = 'Test case: {}, Expected: {}, Result: {}'
        if c_case_choice == 1:
            v_crd = v_card()
            if len(v_crd) == 16:
                if luhn_calc(v_crd):
                    expected = True
                    print('v_card True')
                else:
                    expected = False
            else:
                expected = False
            # if luhn_calc(v_crd, 16):
            #     expected = True
            # else:
            #     expected = False
            new_test = build_test_func(expected, v_crd, credit_card_validator, message)
            setattr(TestCase, 'test_{}'.format(v_crd), new_test)
        if c_case_choice == 2:
            m_crd = m_card()
            if len(m_crd) == 16:
                if luhn_calc(m_crd):
                    expected = True
                    print('m_card True')
                else:
                    expected = False
            else:
                expected = False
            # if luhn_calc(m_crd, 16):
            #     expected = True
            # else:
            #     expected = False
            new_test = build_test_func(expected, m_crd, credit_card_validator, message)
            setattr(TestCase, 'test_{}'.format(m_crd), new_test)
        if c_case_choice == 3:
            e_crd = e_card()
            if len(e_crd) == 15:
                if luhn_calc(e_crd):
                    expected = True
                    print('e_card True')
                else:
                    expected = False
            else:
                expected = False
            # if luhn_calc(e_crd, 15):
            #     expected = True
            # else:
            #     expected = False
            new_test = build_test_func(expected, m_crd, credit_card_validator, message)
            setattr(TestCase, 'test_{}'.format(m_crd), new_test)
        if c_case_choice == 4:
            r_crd = rnd_card()
            expected = False
            new_test = build_test_func(expected, r_crd, credit_card_validator, message)
            setattr(TestCase, 'test_{}'.format(r_crd), new_test)


if __name__ == '__main__':
    generate_testcases()
    unittest.main()
