from kraken_record.kraken_attribute import Kraken_attribute



def test_null_value():


    # Scenario values:
    kr = Kraken_attribute()
    test_value = None


    # Test conditions
    
    kr.set(test_value)

    # Expected outcome
    result_value = None


    # Test evaluation

    assert(kr.value == result_value)





def test_simple_value():



    # Scenario values:
    kr = Kraken_attribute()
    test_value = 'test'


    # Test conditions
    
    kr.set(test_value)

    # Expected outcome
    value = 'test'


    # Test evaluation
    assert(kr.value == value)


def test_dict_value():



    # Scenario values:
    kr = Kraken_attribute()
    test_value = {'credibility': 30}


    # Test conditions
    
    kr.set(test_value)

    # Expected outcome
    result_credibility = 30


    # Test evaluation
    assert(kr.credibility == result_credibility)



def test_less_than():



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
    # Test evaluation
    assert(actual_result == expected_result)




def test_less_than_2():



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
    assert(actual_result == expected_result)



def test_equal_1():

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
    assert(actual_result == expected_result)



def test_equal_2():

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
    assert(actual_result == expected_result)



def test_greater_or_equal_1():

    
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
    assert(actual_result == expected_result)




def test_greater_than_1():

    
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
    assert(actual_result == expected_result)



def test_greater_than_2():



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
    assert(actual_result == expected_result)


