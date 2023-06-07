import pymongo
import bson
from Database import Database
from strongtyping.strong_typing import match_class_typing, match_typing
from strongtyping.strong_typing_utils import TypeMisMatch
from typing import Optional, List, Dict, Union, Any, Tuple
from datetime import datetime
import pprint
import json
from input_schema import (
    NecessaryEarthquakeType,
    NecessaryElectricityType,
    NecessaryReservoirType,
)
import os
from dotenv import load_dotenv

a = ""
with open("./ISP_testcases.json", "r") as f:
    a = json.load(f)

count=0
for name, cases in a.items():
    for case in cases:
        count=count+1
print(count)