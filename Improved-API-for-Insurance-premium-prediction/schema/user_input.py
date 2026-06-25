from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated, Dict
from config.tier_cities import tier_1_cities, tier_2_cities

# create the pydantic model for the data validation coming from the user.
class UserInput(BaseModel):

    age : Annotated[
        int, Field(..., gt = 0, description = 'Age of the user and it should be grater than 0', examples = [23])
    ]
    weight : Annotated[
        float, Field(..., gt = 0, description = 'Weight of the user and it also greater than 0 and also in kgs', examples = [45.5])
    ]
    height : Annotated[
        float,  Field(..., gt = 0, description = 'Height of the user and it should be greater than 0 and also in meters', examples = [170.4])
    ] 
    income_lpa : Annotated[
        float, Field(..., gt = 0, description = 'Income of the user and it also graeter than 0 and it is in LPA', examples = [14.56])
    ] 
    smoker : Annotated[
        bool, Field(description = 'Is the person is a smoker or not')
    ]
    city : Annotated[
        str, Field(..., max_length = 50, description = 'City of the user to which it belongs', examples = ['New Delhi'])
    ]
    occupation : Annotated[
        Literal['retired', 'freelancer', 'student', 'government_job',
        'business_owner', 'unemployed', 'private_job'], Field(description = 'Occupation of the user')
    ]

    @field_validator('city')
    @classmethod
    def normalize_city(cls, v : str) -> str:
        v = v.strip().title()
        return v

    # this computed field is calculated the bmi.
    @computed_field
    @property
    def bmi(self) -> float:
        calculate_bmi = self.weight / (self.height ** 2)
        return calculate_bmi 

    # this computed field is calculate the age_group of the user.
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"


    # this computed field is responsible for find their city_tier
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        

    # this computed field is responsible for find life_style_risk
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker and self.bmi > 27:
            return "medium"
        else:
            return "low"
        

# create this model for validating the data comes from the API.
class ModelPrediction(BaseModel):
    Predicted_Category : Annotated[
        str, Field(..., description = 'This is the class to which this user belongs according the model', examples = ['Low', 'Medium', 'High'])
    ]
    Confidence : Annotated[
        float, Field(...,description = 'This value tells how much our model is confident about the predicted category', examples = [45.5, 40.5, 61.2])
    ]
    Probabilities : Annotated[
        Dict[str, float],  Field(..., description = 'These key value pair tells about the probability of each class', examples = [{'Low' : 12.4}, {'Medium' : 36.6}, {'High' : 50.0}])
    ]


