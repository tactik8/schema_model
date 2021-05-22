
'''
Convert between json schema to kraken schema with ability to manage data credibility.


'''

from kraken_record.kraken_record import Kraken_record as KR



import os

test = False

if test:

    os.system("pip install pytest")

    os.system("python -m pytest tests")



record = {
	"@type": "schema:person",
	"@id": "test_id",
	"schema:givenname": "test Name",
	"schema:familyname": "Test last name ",
	"schema:email": "  ",
	"schema:telephone": "  ",
	"schema:hasOccupation": {
		"@type": "schema:Occupation",
		"schema:name": "some occupation"
		},
	"schema:worksfor": {
		"@type": "schema:organization",
		"schema:name": "Some org",
		"schema:url": "https://www.test.com"
		}
}

kr = KR()
kr.set(record)
print(kr)