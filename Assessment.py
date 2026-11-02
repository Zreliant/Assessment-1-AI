import pandas as pd

# Importing the data sets
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

    # RISKS TO POINTS
    # Calculates risk score depending on data
    def calculate_score(self, person_Data):
        score = 0

        # Calculates house into score
        housing = str(person_Data.get("housing", "")).strip().lower()
        points = self.rules["housing"].get(housing, 0)
        score = score + points

        # Calculates savings into score
        savings = str(person_Data.get("savings", "")).strip().lower()
        points = self.rules["savings"].get(savings, 0)
        score = score + points

        # Calculates checking into score
        checking = str(person_Data.get("checking", "")).strip().lower()
        points = self.rules["checking"].get(checking, 0)
        score = score + points

        # Calculates loan duration into score 
        duration = float(person_Data.get("duration", 0))
        if duration > 24:
            points = self.rules["duration"]["over_24_months"]
            score = score + points

        # Calculates credit amount into score
        credit = float(person_Data.get("credit_amount", 0))
        if credit > 4000:
            points = self.rules["credit_amount"]["over_4000"]
            score = score + points

        # Calculates loan purpose into score
        purpose = str(person_Data.get("purpose", "")).strip().lower()
        points = self.rules["purpose"].get(purpose, 0)
        score = score + points

        return score

    # RESPONSE ON RISK ASSESSMENT
    # Adds up the score and returns a risk assessment
    def respond(self, person_Data):
        score = self.calculate_score(person_Data)

        if score >= self.threshold:
            risk = "High Risk"
        else:
            risk = "Low Risk"

        return (
            f"Risk Assessment: {risk}\n"
            f"Score: {score}\n"
        )

# Creating an AI instance
ai = RuleBasedAI()


# CREATING A PERCENTAGE COMPARISON FOR TRAINING DATA    
# Variables used for comparison
comparison = {
    "same": 0,
    "total": 0
}

# A for loop used to check each row
for _, row in training_data.iterrows():
    person = {
        "housing": row["Housing"],
        "savings": row["Saving accounts"],
        "checking": row["Checking account"],
        "duration": row["Duration"],
        "credit_amount": row["Credit amount"],
        "purpose": row["Purpose"]
    }

    # Calculate the score for the person
    score = ai.calculate_score(person)

    # Checks threshold and assigns a risk value
    predicted = "bad" if score >= ai.threshold else "good"
    actual = str(row["Risk"]).strip().lower()

    # adds up the total and same values for comparison + actual risk values
    if actual in ["good", "bad"]:
        comparison["total"] += 1
        if predicted == actual:
            comparison["same"] += 1

# Print the comparison results (percentage)
print(f"Same risk: {comparison['same'] / comparison['total'] * 100:.2f}%")


# CREATING A TABLE FOR TEST DATA
# Predict the credit risk for every row
predicted_risks = []
scores = []

# A for loop used to check each row
for _, row in test_data.iterrows():
    person = {
        "housing": row["Housing"],
        "savings": row["Saving accounts"],
        "checking": row["Checking account"],
        "duration": row["Duration"],
        "credit_amount": row["Credit amount"],
        "purpose": row["Purpose"]
    }

    # Calculate the score for the person
    score = ai.calculate_score(person)

    # Checks threshold and assigns a risk value
    risk = "bad" if score >= ai.threshold else "good"

    # Gets the risk
    predicted_risks.append(risk)

# Add the results to the dataset
test_data["Risk"] = predicted_risks

# Save to a new CSV file
test_data.to_csv("test_data_predictions.csv", index=False)

print("Credit risk predictions saved to test_data_predictions.csv")