from MongoDB import MongoDB


def API_example():
    earthEqake_test = {
        "time": "2023-5-12 03:40:52",
        "M_L": 3.6,
        "focal_dep": 3.2,
        "longitude": 41.0,
        "latitude": 20.7,
        "magnitude": [
            {"factory": "竹", "magnitude": 0.00032644588703523386},
            {"factory": "中", "magnitude": 0.00019905740360289052},
            {"factory": "南", "magnitude": 0.0003714193582435097},
        ],
    }
    earthEqake_test2 = {
        "time": "2023-5-12 03:40:51",
        "M_L": 3.6,
        "focal_dep": 3.2,
        "longitude": 41.0,
        "latitude": 20.7,
        "magnitude": [
            {"factory": "竹", "magnitude": 0.00032644588703523386},
            {"factory": "中", "magnitude": 0.00019905740360289052},
            {"factory": "南", "magnitude": 0.0003714193582435097},
        ],
    }
    electricity_test = {
        "region": "北",
        "power_usage": 512.3,
        "power_generate": 482.1,
        "time": "2023-5-12 03:40:52",
    }
    electricity_test2 = {
        "region": "南",
        "power_usage": 510.3,
        "power_generate": 472.1,
        "time": "2023-5-12 03:40:52",
    }
    reservoir_test = {
        "time": "2023-5-12 03:40:52",
        "percentage": 427.6,
        "water_supply": 321.2,
        "name": "德基水庫",
    }
    reservoir_test2 = {
        "time": "2023-5-12 03:40:52",
        "percentage": 42.6,
        "water_supply": 321.2,
        "name": "德基水庫",
    }

    ip = "172.26.85.148"
    port = 27017
    db = MongoDB(ip=ip, port=port)
    db.reset()
    db.insert_earthquake_data(earthEqake_test)
    db.insert_earthquake_data(earthEqake_test2)
    db.insert_electricity_data(electricity_test)
    db.insert_electricity_data(electricity_test2)
    db.insert_reservoir_data(reservoir_test)
    db.insert_reservoir_data(reservoir_test2)

    print(f"RETRIEVING RESERVOIR...")
    print(db.retrieve_reservoir_data_by_name(quantity=50, name="德基水庫"))
    for i in db.retrieve_reservoir_data_by_name(quantity=50, name="2"):
        print(i)

    print(f"\n\n\nRETRIEVING ELECTRICITY...\n\n")

    for i in db.retrieve_electricity_data_by_region(quantity=50, region="北"):
        print(i)

    print(f"\n\n\nRETRIEVING EARTHQUAKE...\n\n")
    for i in db.retrieve_earthquake_data(5):
        print(i)

    print(f"\n\n\nRETRIEVING EARTHQUAKE FOR FACTORY...\n\n")

    for i in db.retrieve_earthquake_data_by_factory(factory="竹", quantity=10):
        print(i)

    db.reset()


if __name__ == "__main__":
    API_example()
