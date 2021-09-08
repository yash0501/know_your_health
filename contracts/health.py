# This smart contract takes the user data provided in survey form and then gives the aggregate result

import smartpy as sp

class Health(sp.Contract):

    def __init__(self):
    
        self.init(
            age = {
                "0 - 18": sp.nat(0),
                "19 - 30": sp.nat(0),
                "31 - 50": sp.nat(0),
                "51 - 65": sp.nat(0),
                "66 - 85": sp.nat(0),
                "86+": sp.nat(0)
            },
            water_tds = {
                "0 - 300": sp.nat(0),
                "301 - 600": sp.nat(0),
                "601 - 900": sp.nat(0),
                "901 - 1200": sp.nat(0),
                "1201 - 1500": sp.nat(0),
                ">= 1501": sp.nat(0)
            },
            aqi = {
                "0 - 50": sp.nat(0),
                "51 - 100": sp.nat(0),
                "101 - 150": sp.nat(0),
                "151 - 200": sp.nat(0),
                "201 - 300": sp.nat(0),
                ">= 301": sp.nat(0)
            },
            distance_from_industry = {
                "0 - 2": sp.nat(0),
                "3 - 5": sp.nat(0),
                "6 - 10": sp.nat(0),
                "11 - 15": sp.nat(0),
                ">= 16": sp.nat(0)
            },
            disease_type = {
                "respiratory": sp.nat(0),
                "skin": sp.nat(0),
                "eye": sp.nat(0),
                "heart": sp.nat(0),
                "lung": sp.nat(0),
                "kidney": sp.nat(0),
                "diabetes": sp.nat(0),
                "asthma": sp.nat(0),
                "skin_rash": sp.nat(0),
                "hepatitis": sp.nat(0),
                "kidney_disease": sp.nat(0),
                "high_blood_pressure": sp.nat(0),
                "flu": sp.nat(0),
                "kidney_failure": sp.nat(0),
                "diabetes_mellitus": sp.nat(0),
                "heart_failure": sp.nat(0),
                "chronic_kidney_disease": sp.nat(0),
                "asthma_attack": sp.nat(0),
                "chronic_pulmonary": sp.nat(0),
                "chronic_obstructive_pulmonary": sp.nat(0),
                "chronic_cardio": sp.nat(0),
                "chronic_liver": sp.nat(0),
                "chronic_hepatitis": sp.nat(0),
                "chronic_hypertension": sp.nat(0),
                "chronic_asthma": sp.nat(0),
                "chronic_pulmonary_disease": sp.nat(0),
                "chronic_diabetes": sp.nat(0),
                "chronic_arthritis": sp.nat(0),
                "chronic_rheumatoid_arthritis": sp.nat(0),
                "chronic_virus": sp.nat(0),
                "chronic_mental": sp.nat(0),
                "chronic_other": sp.nat(0),
                "other": sp.nat(0)
            },
            sleep_hours = {
                "0 - 6": sp.nat(0),
                "7 - 12": sp.nat(0),
                "13 - 18": sp.nat(0),
                ">= 19": sp.nat(0)
            },
            exercise_hours = {
                "0 - 2": sp.nat(0),
                "3 - 5": sp.nat(0),
                "6 - 10": sp.nat(0),
                "11 - 15": sp.nat(0),
                ">= 16": sp.nat(0)
            },
            weight = {
                "0 - 30": sp.nat(0),
                "31 - 60": sp.nat(0),
                "61 - 90": sp.nat(0),
                "91 - 120": sp.nat(0),
                ">= 121": sp.nat(0)
            },
            height = {
                "0 - 150": sp.nat(0),
                "151 - 200": sp.nat(0),
                "201 - 250": sp.nat(0),
                ">= 251": sp.nat(0)
            },
        )
    
    @sp.entry_point
    def add_age(self, age):
        self.data.age[age] += 1

    @sp.entry_point
    def add_water_tds(self, water_tds):
        self.data.water_tds[water_tds] += 1

    @sp.entry_point
    def add_aqi(self, aqi):
        self.data.aqi[aqi] += 1

    @sp.entry_point
    def add_distance_from_industry(self, distance_from_industry):
        self.data.distance_from_industry[distance_from_industry] += 1

    @sp.entry_point
    def add_disease_type(self, disease_type):
        self.data.disease_type[disease_type] += 1

    @sp.entry_point
    def add_sleep_hours(self, sleep_hours):
        self.data.sleep_hours[sleep_hours] += 1

    @sp.entry_point
    def add_exercise_hours(self, exercise_hours):
        self.data.exercise_hours[exercise_hours] += 1

    @sp.entry_point
    def add_weight(self, weight):
        self.data.weight[weight] += 1
    
    @sp.entry_point
    def add_height(self, height):
        self.data.height[height] += 1
"""
    @sp.entry_point
    def get_age(self):
        return self.data.age

    @sp.entry_point
    def get_water_tds(self):
        return self.data.water_tds

    @sp.entry_point
    def get_aqi(self):
        return self.data.aqi

    @sp.entry_point
    def get_distance_from_industry(self):
        return self.data.distance_from_industry

    @sp.entry_point
    def get_disease_type(self):
        return self.data.disease_type

    @sp.entry_point
    def get_sleep_hours(self):
        return self.data.sleep_hours
    
    @sp.entry_point
    def get_exercise_hours(self):
        return self.data.exercise_hours

    @sp.entry_point
    def get_weight(self):
        return self.data.weight

    @sp.entry_point
    def get_height(self):
        return self.data.height
"""
@sp.add_test(name = "Test")
def test():
    scenario = sp.test_scenario()
    health = Health()
    scenario += health
    scenario += health.add_age("19 - 30")
    scenario += health.add_water_tds("0 - 300")
    scenario += health.add_aqi("101 - 150")
    scenario += health.add_distance_from_industry("0 - 2")
    scenario += health.add_disease_type("flu")
    scenario += health.add_sleep_hours("0 - 6")
    scenario += health.add_exercise_hours("0 - 2")
    scenario += health.add_weight("31 - 60")
    scenario += health.add_height("151 - 200")
    
    