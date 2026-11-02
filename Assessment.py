import pandas as pd

training_data = pd.read_csv('training_data.csv')
test_data = pd.read_csv('test_data.csv')

class RuleBasedAI:
    def __init__(self):
        # THE POINT SCORING SYSTEM
        # Amount needed for bad credit score
        self.threshold = 7
        # Points added depending on data
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

    def calculate_score(self, person_Data):
        score = 0

        housing = str(person_Data.get("housing", "")).strip().lower()
        points = self.rules["housing"].get(housing, 0)
        score = score + points

        savings = str(person_Data.get("savings", "")).strip().lower()
        points = self.rules["savings"].get(savings, 0)
        score = score + points

        checking = str(person_Data.get("checking", "")).strip().lower()
        points = self.rules["checking"].get(checking, 0)
        score = score + points

        duration = float(person_Data.get("duration", 0))
        if duration > 24:
            points = self.rules["duration"]["over_24_months"]
            score = score + points

        credit = float(person_Data.get("credit_amount", 0))
        if credit > 4000:
            points = self.rules["credit_amount"]["over_4000"]
            score = score + points

        purpose = str(person_Data.get("purpose", "")).strip().lower()
        points = self.rules["purpose"].get(purpose, 0)
        score = score + points

        return score