import unittest
from MongoDB import MongoDB
from Database import Database
import pymongo
import json
import math
from datetime import datetime
from db_config import IP, PORT, MAX_PRSERVE_RECORD
from unittest.mock import MagicMock
from strongtyping.strong_typing_utils import TypeMisMatch

class TestMongoDB(unittest.TestCase):
    
    def set_up(self):
        self.db = MongoDB()
        with open("./testcases.json", "r") as f:
            self.test_cases = json.load(f)
    
    def test_init_TTTTT(self):
        db = MongoDB(IP, PORT, "my_mongoDB", ["earthquake", "electricity", "reservoir"])
    
    def test_init_FTTTT(self):
        db = MongoDB(None, PORT, "my_mongoDB", ["earthquake", "electricity", "reservoir"])
        #self.assertEqual(ip, IP)
        db = MongoDB(IP, None, "my_mongoDB", ["earthquake", "electricity", "reservoir"])
        #self.assertEqual

        # source doesn't update yet
        #db = MongoDB(IP, PORT, None, ["earthquake", "electricity", "reservoir"])
        #self.assertEqual

        db = MongoDB(IP, PORT, "my_mongoDB", None)
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

    

if __name__ == "__main__":    
    unittest.main()