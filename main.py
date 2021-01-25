


from test_scripts.test_kraken_attribute import Test_kraken_attribute

from test_scripts.test_kraken_record import Test_kraken_record


tests_attr = Test_kraken_attribute()

tests_attr.test_all()


tests_record = Test_kraken_record()
tests_record.test_all()