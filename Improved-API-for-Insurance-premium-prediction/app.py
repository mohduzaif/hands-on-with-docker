from fastapi import FastAPI
from fastapi.responses import JSONResponse

from schema.user_input import UserInput
from schema.user_input import ModelPrediction
from model.predict import model, MODEL_VERSION, prediction


# create the object of the FastAPI
app1 = FastAPI()

# Home route.
# human readable.
@app1.get('/')
def home():
    return {
        'message' : 'Insurance Premium Prediction API'
    }

# health check route for the AWS services they hit this route for the correct working of our API.
# machine readable 
@app1.get('/health')
def health_check():
    return {
        'status' : 'OK',
        'version' : MODEL_VERSION, 
        'model_loaded' : model is not None
    }

# create an end-point for the prediction
@app1.post('/predict', response_model = ModelPrediction, summary="Predict Diabetes Risk",
    description="This endpoint accepts user health and demographic data and returns the predicted diabetes risk."
)
def predicted_result(userData : UserInput):
    
    current_input = {
        'bmi' : userData.bmi, 
        'age_group' : userData.age_group, 
        'lifestyle_risk' : userData.lifestyle_risk, 
        'city_tier' : userData.city_tier, 
        'income_lpa' : userData.income_lpa, 
        'occupation' : userData.occupation
    }

    try:
        output = prediction(current_input)
        return JSONResponse(
            status_code = 200, content={'response': output}
        )
    except Exception as e:
        return JSONResponse(
            status_code = 500, 
            content = str(e)
        )




