import pandas as pd

training_data = pd.read_csv('training_data.csv')
test_data = pd.read_csv('test_data.csv')

class RuleBasedAI:
    def __init__(self):
        self.threshold = 7
        self.rules = {
            "housing": {
                "rent": 2,
                "free": 1,
                "own": 0
            },
            "savings": {
                "little": 3,
                "moderate": 2,
                "rich": 1,
                "quite rich": 0
            },
            "checking": {
                "little": 3,
                "moderate": 2,
                "rich": 1, 
            },
            "duration": {
                "over_24_months": 2
            },
            "credit_amount": {
                "over_4000": 2
            },
            "purpose": {
                "education": 1,
                "vacation/others": 1,
                "car": 1,
                "furniture/equipment": 1,
                "radio/tv": 1,
                "business": 1,
                "domestic appliance": 1,
                "repairs": 1,
            }
        }