import pymongo
import bson
from dbAPI.Database import Database
from strongtyping.strong_typing import match_class_typing, match_typing
from strongtyping.strong_typing_utils import TypeMisMatch
from typing import Optional, List, Dict, Union, Any, Tuple
from datetime import datetime
import pprint
from dbAPI.db_config import IP, PORT, DB_NAME, MAX_PRSERVE_RECORD, COLLECTION_LIST
from dbAPI.input_schema import NecessaryEarthquakeType, NecessaryElectricityType, NecessaryReservoirType

#change dbAPI.* to * if none dbAPI directory exists


@match_class_typing
class MongoDB(Database):
    
    def __init__(self, ip: Optional[str] = None, port: Optional[int]=None, db_name: Optional[str] = None, collection_list:  Optional[list] = None):
        if ip == None or port == None or db_name == None or collection_list == None:
            print("[MongoDB] At least one input is invalid or not specified. Loading db_config")
            ip = IP
            port = PORT
            db_name = DB_NAME
            collection_list = COLLECTION_LIST
        super().__init__(ip=ip, port=port, db_name=db_name)
        self.collection_list = collection_list
        if self.collection_list == None:
            print("[MongoDB] None collection_list specified. Loading db_config")
            self.collection_list = COLLECTION_LIST

        for collection in self.collection_list:
            self.db[collection].create_index("time")

        self.necessary_key_for_collection = {"reservoir": NecessaryReservoirType, "earthquake":NecessaryEarthquakeType, "electricity":NecessaryElectricityType}

    @match_typing
    def __check_input_type(self, data: Dict, collection: str):
        try:
            self.necessary_key_for_collection[collection](data)
        except:
            print("[MongoDB] Some necessary columns are missing or type is incorrect. Aborting...")
            raise

    def __insert_into_factory_and_earthqake(self, single_data: Dict):
        factory_data = single_data.pop('magnitude')
        self.insert_data("earthquake", single_data)
        for factory in factory_data:
            del single_data['_id']  # insertion will assign "_id" key to insert data
            single_data['factory'] = factory['factory']
            single_data['magnitude'] = factory['magnitude']
            self.insert_data("factory", single_data)


    def insert_earthquake_data(self, data: Dict):
        self.__check_input_type(data, "earthquake")
        self.__insert_into_factory_and_earthqake(data)
    
    
    def insert_electricity_data(self, data: dict):
        self.__check_input_type(data, "electricity")
        self.insert_data("electricity", data)
        
    
    def insert_reservoir_data(self, data: dict):
        self.__check_input_type(data, "reservoir")
        self.insert_data("reservoir", data)
        
    
    def retrieve_earthquake_data_by_factory(self, factory: str=None, quantity:int =1):  # factory_location = ["竹", "中", "南"]
        assert factory is not None, "[MongoDB] Fatory was not specified in given request"
        assert type(quantity) == int, "[MongoDB] Quantity must be integer"
        return [x for x in self.retrieve_data(
                collection_name="factory", condition={"factory": factory}, sort=('time', -1), limit=quantity)]

    def retrieve_earthquake_data(self, quantity:int =1):
        assert type(quantity) == int, "[MongoDB] Quantity must be integer"
        return [x for x in self.retrieve_data(
                collection_name="earthquake", condition={}, sort=('time', -1), limit=quantity)]
    
    def retrieve_reservoir_data_by_name(self, name: str=None, quantity:int =1):
        assert name is not None, "[MongoDB] Resovoir name was not specified in given request"
        assert type(quantity) == int, "[MongoDB] Quantity must be integer"
        return [x for x in self.retrieve_data(
                collection_name="reservoir", condition={"name": name}, sort=('time', -1), limit=quantity)]
    
    
    def retrieve_electricity_data_by_region(self, region: str=None, quantity:int =1):  # region = ["北", "中", "南"]
        assert type(quantity) == int, "[MongoDB] Quantity must be integer"
        assert region is not None, "[MongoDB] Region was not specified in given request"
        return [x for x in self.retrieve_data(
                collection_name="electricity", condition={"region": region}, sort=('time', 1), limit=quantity)]
    
    
    def print_all_data(self, collection: str):
        print(f"Collection: {collection}")
        for post in self.db[collection].find():
            pprint.pprint(post)   
        print("\n")
    
    
    def clean_collection(self, collection: str):
        self.db[collection].delete_many({})
        

    def reset(self):
        self.clean_all_collection()

    def clean_all_collection(self):
        if self.collection_list is not None:
            for collection in self.collection_list:
                self.clean_collection(collection)
                