
from kraken_record.kraken_attribute import Kraken_attribute

import inspect



class Test_kraken_attribute:

    def __init__(self):

        a=1

    def test_all(self):

        


        self.test_null_value()
        self.test_simple_value()
        self.test_less_than()
        self.test_less_than_2()
        self.test_equal_1()
        self.test_equal_2()
        self.test_greater_than_1()
        self.test_greater_than_2()
        self.test_greater_or_equal_1()


    def test_null_value(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)

        # Scenario values:
        kr = Kraken_attribute()
        test_value = None


        # Test conditions
        
        kr.set(test_value)

        # Expected outcome
        result_value = None


        # Test evaluation
        if kr.value == result_value:
            print('passed')
        else:
            print('failed')

        return




    def test_simple_value(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)


        # Scenario values:
        kr = Kraken_attribute()
        test_value = 'test'


        # Test conditions
        
        kr.set(test_value)

        # Expected outcome
        value = 'test'


        # Test evaluation
        if kr.value == value:
            print('passed')
        else:
            print('failed')

        return

    def test_dict_value(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)


        # Scenario values:
        kr = Kraken_attribute()
        test_value = {'credibility': 30}


        # Test conditions
        
        kr.set(test_value)

        # Expected outcome
        result_credibility = 30


        # Test evaluation
        if kr.credibility == result_credibility:
            print('passed')
        else:
            print('failed')

        return


    def test_less_than(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)


        # Scenario values:        
        test_value = {}

        test_value['value1'] = {'kraken:value': 'test2_1', 'kraken:credibility': 30}
        test_value['value2'] = {'kraken:value': 'test_2', 'kraken:credibility': 40}
        
        expected_result = True

        # Test conditions
        kr1 = Kraken_attribute()
        kr1.set(test_value['value1'])

        kr2 = Kraken_attribute()
        kr2.set(test_value['value2'])

        actual_result = kr1 < kr2


        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', test_value)
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return



    def test_less_than_2(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)


        # Scenario values:        
        test_value = {}

        test_value['value1'] = {'value': 'test_31', 'credibility': 30}
        test_value['value2'] = {'value': 'test_2', 'credibility': 40}
        
        expected_result = False

        # Test conditions
        kr1 = Kraken_attribute()
        kr1.set(test_value['value1'])

        kr2 = Kraken_attribute()
        kr2.set(test_value['value2'])

        actual_result = kr2 < kr1


        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', test_value)
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return

    def test_equal_1(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)
        # Scenario values:        
        test_value = {}

        test_value['value1'] = {'value': 'test_1', 'credibility': 30}
        test_value['value2'] = {'value': 'test_2', 'credibility': 40}
        
        expected_result = False

        # Test conditions
        kr1 = Kraken_attribute()
        kr1.set(test_value['value1'])

        kr2 = Kraken_attribute()
        kr2.set(test_value['value2'])

        actual_result = kr2 == kr1


        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', test_value)
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return

    def test_equal_2(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)
        # Scenario values:        
        test_value = {}

        test_value['value1'] = {'value': 'test_1', 'credibility': 30}
        test_value['value2'] = {'value': 'test_1', 'credibility': 30}
        
        expected_result = True

        # Test conditions
        kr1 = Kraken_attribute()
        kr1.set(test_value['value1'])

        kr2 = Kraken_attribute()
        kr2.set(test_value['value2'])

        actual_result = kr2 == kr1


        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', test_value)
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return

    def test_greater_or_equal_1(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)
        
        # Scenario values:        
        test_value = {}

        test_value['value1'] = {'value': 'test_1', 'credibility': 30}
        test_value['value2'] = {'value': 'test_1', 'credibility': 30}
        
        expected_result = True

        # Test conditions
        kr1 = Kraken_attribute()
        kr1.set(test_value['value1'])

        kr2 = Kraken_attribute()
        kr2.set(test_value['value2'])

        actual_result = kr2 >= kr1


        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', test_value)
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return


    def test_greater_than_1(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)
        
        # Scenario values:        
        test_value = {}

        test_value['value1'] = {'value': 'test_1', 'credibility': 30}
        test_value['value2'] = {'value': 'test_2', 'credibility': 40}
        
        expected_result = True

        # Test conditions
        kr1 = Kraken_attribute()
        kr1.set(test_value['value1'])

        kr2 = Kraken_attribute()
        kr2.set(test_value['value2'])

        actual_result = kr2 > kr1


        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', test_value)
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return

    def test_greater_than_2(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)


        # Scenario values:        
        test_value = {}

        test_value['value1'] = {'value': 'test_1', 'credibility': 30}
        test_value['value2'] = {'value': 'test_2', 'credibility': 40}
        
        expected_result = False

        # Test conditions
        kr1 = Kraken_attribute()
        kr1.set(test_value['value1'])

        kr2 = Kraken_attribute()
        kr2.set(test_value['value2'])

        actual_result = kr1 > kr2


        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', test_value)
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return
