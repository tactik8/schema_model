from models.kraken_record import Kraken_record
import inspect

class Test_kraken_record:

    def __init__(self):

        a=1

    def test_all(self):

        self.test_clean_input_value_blank()
        self.test_clean_input_value_simple()
        self.test_clean_input_value_complex()
        self.test_set_attribute()
        self.test_set_attribute_multiple()
        self.test_set()
        self.test_set_2()
        self.test_set_no_id()
        self.test_set_subschema()
        self.test_set_subschema2()
        self.test_add_different_values()
        self.test_add_same_values()
        self.test_equal_true()
        self.test_equal_false()
        self.test_less_or_equal_true()
        self.test_load()
        self.test_dump()

    def test_clean_input_value_blank(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)

        # Scenario values:
        kr = Kraken_record()
        test_value = None


        # Test conditions
        kr.input_value = test_value
        kr._clean_input_value_keys()

        # Expected outcome
        result_value = None


        # Test evaluation
        if kr.input_value == result_value:
            print('passed')
        else:
            print('failed')

        return


    def test_clean_input_value_simple(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)

        # Scenario values:        
        test_value = {
            'record_type': 'schema:test', 
            'record_id': 'test123', 
            'kraken:name': 'test_name'
            }

        expected_result =  {
            'kraken:record_type': 'schema:test', 
            'kraken:record_id': 'test123', 
            'kraken:name': 'test_name'
            }


        # Test conditions
        kr = Kraken_record()
        kr.input_value = test_value
        kr._clean_input_value_keys()

        actual_result = kr.input_value



        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', test_value)
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return



    def test_clean_input_value_complex(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)


        # Scenario values:        
        test_value = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'kraken:name': 'test_name'
            }

        expected_result =  {
            'kraken:record_type': 'schema:test', 
            'kraken:record_id': 'test123', 
            'kraken:name': 'test_name'
            }


        # Test conditions
        kr = Kraken_record()
        kr.input_value = test_value
        kr._clean_input_value_keys()

        actual_result = kr.input_value



        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', test_value)
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return



    def test_set_attribute(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)


        # Scenario values:        
        test_value = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'kraken:name': 'test_name'
            }

        expected_result =  {
            'kraken:record_type': 'schema:test', 
            'kraken:record_id': 'test123', 
            'kraken:name': 'test_name'
            }

        attr_value = {'value': 'test_2', 'credibility': 40}


        expected_result = [{'value': 'test_2', 'credibility': 40}]


        # Test conditions
        kr = Kraken_record()
        kr.record_type = 'schema:test'
        kr.record_id = 'test123'
        kr.set_attr('schema:test_attr', attr_value)

        actual_result = kr.get_attr_record('schema:test_attr')



        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', test_value)
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return


    
    def test_set_attribute_multiple(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)


        # Scenario values:        
       

        attr_value1 = {'value': 'test_1', 'kraken:credibility': 30}
        attr_value2 = {'value': 'test_2', 'kraken:credibility': 40}


        expected_result = [{'value': 'test_2', 'credibility': 40}, {'value': 'test_1', 'credibility': 30}]


        # Test conditions
        kr = Kraken_record()
        kr.record_type = 'schema:test'
        kr.record_id = 'test123'
        kr.set_attr('schema:test_attr', attr_value1)
        kr.set_attr('schema:test_attr', attr_value2)

        actual_result = kr.get_attr_record('schema:test_attr')



        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return

    
    def test_set(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)
        
        # Scenario values:        
       

        test_value = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 50,
            'schema:name': 'test_name',
            'schema:test': 'test_var'
            }


        expected_result = {'@type': 'schema:test', '@id': 'test123', 'schema:name': [{'value': 'test_name', 'credibility': 50}], 'schema:test': [{'value': 'test_var', 'credibility': 50}]}


        # Test conditions
        kr = Kraken_record()
        kr.set(test_value)
        


        actual_result = kr.get()



        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return

    
    def test_set_2(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)

        
        # Scenario values:        
       

        test_value_1 = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 50,
            'schema:name': 'test_name',
            'schema:test': 'test_var'
            }

        test_value_2 = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 40,
            'schema:name': 'test_name2',
            'schema:test': 'test_var2'
            }


        expected_result = {'@type': 'schema:test', '@id': 'test123', 'schema:name': [{'value': 'test_name', 'credibility': 50}, {'value': 'test_name2', 'credibility': 40}], 'schema:test': [{'value': 'test_var', 'credibility': 50}, {'value': 'test_var2', 'credibility': 40}]}



        # Test conditions
        kr = Kraken_record()
        kr.set(test_value_1)
        kr.set(test_value_2)

        actual_result = kr.get()




        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return


    def test_set_no_id(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)
        
        # Scenario values:        
       

        test_value = {
            'record_Type': 'schema:webpage', 
            'credibility': 50,
            'schema:name': 'test_name',
            'schema:test': 'test_var',
            'schema:url': 'https://www.test.com'
            }


        expected_result = {'@type': 'schema:webpage', '@id': 'https://www.test.com', 'schema:name': [{'value': 'test_name', 'credibility': 50}], 'schema:test': [{'value': 'test_var', 'credibility': 50}], 'schema:url': [{'value': 'https://www.test.com', 'credibility': 50}]}


        # Test conditions
        kr = Kraken_record()
        kr.set(test_value)
        


        actual_result = kr.get()



        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return


    
    def test_set_subschema(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)

        
        # Scenario values:        
       

        test_value_1 = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 50,
            'schema:name': 'test_name',
            'schema:test': 'test_var',
            'schema:sub_schema': {
                'schema:sub_var': 'testsubvar'
                }
            }


        expected_result = {'@type': 'schema:test', '@id': 'test123', 'schema:name': [{'value': 'test_name', 'credibility': 50}], 'schema:test': [{'value': 'test_var', 'credibility': 50}], 'schema:sub_schema': [{'value': {'schema:sub_var': 'testsubvar'}, 'credibility': 50}]}



        # Test conditions
        kr = Kraken_record()
        kr.set(test_value_1)

        actual_result = kr.get()




        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return

    
    def test_set_subschema2(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)

        
        # Scenario values:        
       

        test_value_1 = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 50,
            'schema:name': 'test_name',
            'schema:test': 'test_var',
            'schema:sub_schema': {
                '@type': 'schema:sub',
                '@id': 'sub_id',
                'schema:sub_var': 'testsubvar'
                }
            }


        expected_result = {'@type': 'schema:test', '@id': 'test123', 'schema:name': [{'value': 'test_name', 'credibility': 50}], 'schema:test': [{'value': 'test_var', 'credibility': 50}], 'schema:sub_schema': [{'value': {'@type': 'schema:sub', '@id': 'sub_id'}, 'credibility': 50}]}



        # Test conditions
        kr = Kraken_record()
        kr.set(test_value_1)

        actual_result = kr.get()


        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return


     
    def test_add_different_values(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)

        
        # Scenario values:        
       

        test_value_1 = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 50,
            'schema:name': 'test_name',
            'schema:test': 'test_var'
            }

        test_value_2 = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 40,
            'schema:name': 'test_name2',
            'schema:test': 'test_var2'
            }


        expected_result = {'@type': 'schema:test', '@id': 'test123', 'schema:name': [{'value': 'test_name', 'credibility': 50}, {'value': 'test_name2', 'credibility': 40}], 'schema:test': [{'value': 'test_var', 'credibility': 50}, {'value': 'test_var2', 'credibility': 40}]}



        # Test conditions
        kr1 = Kraken_record()
        kr1.set(test_value_1)

        kr2 = Kraken_record()
        kr2.set(test_value_2)

        kr_total = kr1 + kr2

        actual_result = kr_total.get()




        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return

    def test_add_same_values(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)

        
        # Scenario values:        
       

        test_value_1 = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 50,
            'schema:name': 'test_name',
            'schema:test': 'test_var'
            }



        expected_result = {'@type': 'schema:test', '@id': 'test123', 'schema:name': [{'value': 'test_name', 'credibility': 50}], 'schema:test': [{'value': 'test_var', 'credibility': 50}]}


        # Test conditions
        kr1 = Kraken_record()
        kr1.set(test_value_1)

        kr2 = Kraken_record()
        kr2.set(test_value_1)

        kr_total = kr1 + kr2

        actual_result = kr_total.get()




        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return

    def test_equal_true(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)

        
        # Scenario values:        
       

        test_value_1 = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 50,
            'schema:name': 'test_name',
            'schema:test': 'test_var'
            }



        expected_result = True


        # Test conditions
        kr1 = Kraken_record()
        kr1.set(test_value_1)

        kr2 = Kraken_record()
        kr2.set(test_value_1)


        actual_result = kr1 == kr2




        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return
    
    def test_equal_false(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)

        
        # Scenario values:        
       

        test_value_1 = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 50,
            'schema:name': 'test_name',
            'schema:test': 'test_var'
            }

        test_value_2 = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 40,
            'schema:name': 'test_name2',
            'schema:test': 'test_var2'
            }

        expected_result = False


        # Test conditions
        kr1 = Kraken_record()
        kr1.set(test_value_1)

        kr2 = Kraken_record()
        kr2.set(test_value_2)


        actual_result = kr1 == kr2




        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return


    def test_less_or_equal_true(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)

        
        # Scenario values:        
       

        test_value_1 = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 50,
            'schema:name': 'test_name'
            }

        test_value_2 = {
            'record_Type': 'schema:test', 
            'RECORD_ID': 'test123', 
            'credibility': 50,
            'schema:name': 'test_name',
            'schema:test': 'test'
            }

        expected_result = True


        # Test conditions
        kr1 = Kraken_record()
        kr1.set(test_value_1)

        kr2 = Kraken_record()
        kr2.set(test_value_2)


        actual_result = kr1 <= kr2




        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return


    
    def test_load(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)
        
        # Scenario values:        
       

        test_value = {'kraken:record_type': 'schema:test', 'kraken:record_id': 'test123', 'schema:name': [{'value': 'test_name', 'credibility': 50}], 'schema:test': [{'value': 'test_var', 'credibility': 50}]}


        expected_result = {'@type': 'schema:test', '@id': 'test123', 'schema:name': [{'value': 'test_name', 'credibility': 50}], 'schema:test': [{'value': 'test_var', 'credibility': 50}]}

        # Test conditions
        kr = Kraken_record()
        kr.load(test_value)
        
        actual_result = kr.get()

        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return
    
    
    def test_dump(self):
        print('-')
        print(inspect.currentframe().f_code.co_name)
        
        # Scenario values:        
        
        test_value = {'@type': 'schema:test', '@id': 'test123', 'schema:name': [{'value': 'test_name', 'credibility': 50}], 'schema:test': [{'value': 'test_var', 'credibility': 50}]}


        expected_result = {'kraken:record_type': 'schema:test', 'kraken:record_id': 'test123', 'schema:name': [{'value': [{'value': 'test_name', 'credibility': 50}]}], 'schema:test': [{'value': [{'value': 'test_var', 'credibility': 50}]}]}


        # Test conditions
        kr = Kraken_record()
        kr.set(test_value)
        
        actual_result = kr.dump()

        # Test evaluation
        if actual_result == expected_result:
            print('passed')
        else:
            print('failed')
            print('Input value', '')
            print('Expected result', expected_result)
            print('actual_result', actual_result)


        return
