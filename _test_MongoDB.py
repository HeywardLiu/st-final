import unittest
import pymongo
import json
import math
from datetime import datetime
from unittest.mock import MagicMock
from MongoDB import MongoDB
from dotenv import load_dotenv
from strongtyping.strong_typing_utils import TypeMisMatch

class TestMongoDB(unittest.TestCase):
    def setup(self):
        self.db=MongoDB()
        self.db.reset = MagicMock(side_effect=self.mock_reset())
        with open("_testcases.json", "r") as f:
            self.testcases = json.load(f)


    def test_retrieve_earthquake_data_by_factory(self):
        self.setup()
        self.testcases=self.testcases["test_retrieve_earthquake_data_by_factory"]
        self.db.insert_earthquake_data=MagicMock(side_effect=self.mock_insert_earthquake)
        for case in self.testcases:
            with self.subTest(case['case']):
                self.mock_reset()
                if(case.get("mock_insert_data") != None):
                    self.db.insert_earthquake_data(case["mock_insert_data"])
                if("Exception" in case["outcome"]):
                    e = case["outcome"].split(":")[1]
                    with self.assertRaises(eval(e)):
                        self.db.retrieve_earthquake_data_by_factory(factory=case['factory'], quantity=case['quantity'])
                else:
                    result=[x for x in self.db.retrieve_earthquake_data_by_factory(factory=case['factory'], quantity=case['quantity'])]
                    self.assertEqual(result, case['outcome'])

    def mock_insert_earthquake(self, data):
        # Insert data into "factory" collection
        insert_list = []
        for i in data['magnitude']:
            temp = data.copy()
            temp['factory']=i['factory']
            temp["magnitude"] = i["magnitude"]
            insert_list.append(temp)

        for j in insert_list:
            self.db.insert_data(collection_name="factory", data=j)

        # Insert data into "earthquake" collection
        temp=data.copy()
        del temp['magnitude']
        self.db.insert_data(collection_name="earthquake", data=temp)

    def mock_reset(self):
        for collection in ["earthquake", "reservoir", "electricity", "factory"]:
            self.db.db[collection].delete_many({})

