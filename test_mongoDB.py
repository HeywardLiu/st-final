import unittest
from MongoDB import MongoDB
from Database import Database
import pymongo
import bson
from strongtyping.strong_typing import match_class_typing, match_typing
from typing import Optional, List, Dict, Union, Any, Tuple
from datetime import datetime
import pprint
from input_schema import NecessaryEarthquakeType, NecessaryElectricityType, NecessaryReservoirType
import os
from dotenv import load_dotenv
from unittest.mock import MagicMock
from strongtyping.strong_typing_utils import TypeMisMatch

class TestMongoDB(unittest.TestCase):
    
    def set_up(self):
        self.db = MongoDB()
        self.db.reset()
        with open("./testcases.json", "r") as f:
            self.test_cases = json.load(f)
    
    def test_init_TTTTT(self):
        db = MongoDB(IP, PORT, DB_NAME, COLLECTION_LIST)
    
    def test_init_FTTTT(self):
        db = MongoDB(None, PORT, DB_NAME, COLLECTION_LIST)
        #self.assertEqual(db.ip, IP)
        #db = MongoDB(IP, None, DB_NAME, COLLECTION_LIST)
        #self.assertEqual

        #db = MongoDB(IP, PORT, None, COLLECTION_LIST)
        #self.assertEqual

        #db = MongoDB(IP, PORT, DB_NAME, None)
        #self.assertEqual
    
    def test_init_TFTTT(self):
        with self.assertRaises(TypeMisMatch):
            db = MongoDB(1721234514, PORT, "my_mongoDB", ["earthquake", "electricity", "reservoir"])
            
    def test_init_TTFTT(self):
        with self.assertRaises(TypeMisMatch):
            db = MongoDB(IP, "27017", "my_mongoDB", ["earthquake", "electricity", "reservoir"])

    def test_init_TTTFT(self):
        with self.assertRaises(TypeMisMatch):
            db = MongoDB(IP, PORT, 123, ["earthquake", "electricity", "reservoir"])
    
    def test_init_TTTTF(self):
        with self.assertRaises(TypeMisMatch):
            db = MongoDB(IP, PORT, "my_mongoDB", {"earthquake": 123})
    
    def test_insert_earthquake_data_TT(self):
        self.set_up()
        case = self.test_cases['insert_earthquake_TT']
        self.db.insert_earthquake_data(case)
    
    def test_insert_earthquake_data_FF(self):
        self.set_up()
        case = self.test_cases['insert_earthquake_FF']
        with self.assertRaises(TypeMisMatch):
            self.db.insert_earthquake_data(case)

    def test_insert_earthquake_data_TF(self):
        self.set_up()
        case = self.test_cases['insert_earthquake_TF']
        with self.assertRaises(AssertionError):
            self.db.insert_earthquake_data(case)
    
    def test_insert_electricity_data_TT(self):
        self.set_up()
        case = self.test_cases['insert_electricity_TT']
        self.db.insert_electricity_data(case)
    
    def test_insert_electricity_data_FF(self):
        self.set_up()
        case = self.test_cases['insert_electricity_FF']
        with self.assertRaises(TypeMisMatch):
            self.db.insert_electricity_data(case)

    def test_insert_electricity_data_TF(self):
        self.set_up()
        case = self.test_cases['insert_electricity_TF']
        with self.assertRaises(AssertionError):
            self.db.insert_electricity_data(case)

    def test_insert_reservoir_data_TT(self):
        self.set_up()
        case = self.test_cases['insert_reservoir_TT']
        self.db.insert_reservoir_data(case)
    
    def test_insert_reservoir_data_FF(self):
        self.set_up()
        case = self.test_cases['insert_reservoir_FF']
        with self.assertRaises(TypeMisMatch):
            self.db.insert_reservoir_data(case)

    def test_insert_reservoir_data_TF(self):
        self.set_up()
        case = self.test_cases['insert_reservoir_TF']
        with self.assertRaises(AssertionError):
            self.db.insert_reservoir_data(case)

    def test_retrieve_earthquake_data_by_factory_TTT(self):
        self.set_up()
        cases = self.test_cases['retrieve_earthEqake_T']
        l = []

        for case in cases:
            self.db.insert_earthquake_data(case)

        for x in self.db.retrieve_data(
            collection_name="factory",
            condition={"factory": "竹"},
            sort=("time", -1),
            limit=10,
            ):
            l.append(x)
        
        self.assertEqual(l, self.db.retrieve_earthquake_data_by_factory(factory="竹", quantity=10))
    
    def test_retrieve_earthquake_data_by_factory_FTT(self):
        self.set_up()
        cases = self.test_cases['retrieve_earthEqake_T']

        for case in cases:
            self.db.insert_earthquake_data(case)

        with self.assertRaises(TypeMisMatch):
            self.db.retrieve_earthquake_data_by_factory(factory=12, quantity=10)

    def test_retrieve_earthquake_data_by_factory_TFT(self):
        self.set_up()
        cases = self.test_cases['retrieve_earthEqake_T']

        for case in cases:
            self.db.insert_earthquake_data(case)

        with self.assertRaises(TypeMisMatch):
            self.db.retrieve_earthquake_data_by_factory(factory="竹", quantity="10")

    def test_retrieve_earthquake_data_by_factory_TTF(self):
        self.set_up()
        cases = self.test_cases['retrieve_earthEqake_F']

        for case in cases:
            self.db.insert_earthquake_data(case)

        self.assertEqual([], self.db.retrieve_earthquake_data_by_factory(factory="竹", quantity=10))
    
    def test_retrieve_earthquake_data_TT(self):
        self.set_up()
        cases = self.test_cases['retrieve_earthEqake_T']
        l = []

        for case in cases:
            self.db.insert_earthquake_data(case)

        for x in self.db.retrieve_data(
            collection_name="earthquake",
            condition={},
            sort=("time", -1),
            limit=10,
            ):
            l.append(x)
        
        self.assertEqual(l, self.db.retrieve_earthquake_data(quantity=10))
    
    def test_retrieve_earthquake_data_FT(self):
        self.set_up()
        cases = self.test_cases['retrieve_earthEqake_T']

        for case in cases:
            self.db.insert_earthquake_data(case)

        with self.assertRaises(TypeMisMatch):
            self.db.retrieve_earthquake_data(quantity="10")

    def test_retrieve_earthquake_data_TF(self):
        self.set_up()
        cases = self.test_cases['retrieve_earthEqake_F']

        for case in cases:
            self.db.insert_earthquake_data(case)

        self.assertEqual([], self.db.retrieve_earthquake_data(quantity=10))
    
    def test_retrieve_reservoir_data_by_name_TTT(self):
        self.set_up()
        cases = self.test_cases['retrieve_reservoir_T']
        l = []

        for case in cases:
            self.db.insert_reservoir_data(case)

        for x in self.db.retrieve_data(
                collection_name="reservoir",
                condition={"name": "翡翠水庫"},
                sort=("time", -1),
                limit=10,
            ):
            l.append(x)
        
        self.assertEqual(l, self.db.retrieve_reservoir_data_by_name(name="翡翠水庫", quantity=10))
    
    def test_retrieve_reservoir_data_by_name_FTT(self):
        self.set_up()
        cases = self.test_cases['retrieve_reservoir_T']

        for case in cases:
            self.db.insert_reservoir_data(case)

        with self.assertRaises(TypeMisMatch):
            self.db.retrieve_reservoir_data_by_name(name=12, quantity=10)

    def test_retrieve_reservoir_data_by_name_TFT(self):
        self.set_up()
        cases = self.test_cases['retrieve_reservoir_T']

        for case in cases:
            self.db.insert_reservoir_data(case)

        with self.assertRaises(TypeMisMatch):
            self.db.retrieve_reservoir_data_by_name(name="翡翠水庫", quantity="10")

    def test_retrieve_reservoir_data_by_name_TTF(self):
        self.set_up()
        cases = self.test_cases['retrieve_reservoir_F']

        for case in cases:
            self.db.insert_reservoir_data(case)

        self.assertEqual([], self.db.retrieve_reservoir_data_by_name(name="翡翠水庫", quantity=10))
    

if __name__ == "__main__":    
    unittest.main()