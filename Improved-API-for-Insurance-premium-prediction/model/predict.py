import pandas as pd
import pickle


# import the machine-learning model.
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# it is a good practise to add the version of your loaded model.
# It is comes from MLFlow type software jaise model registry.
MODEL_VERSION = '1.0.0' 


# this method is useful for the prediction of the model.
def prediction(user_input : dict):

    # convert the dictionary into a dataframe.
    user_input_df = pd.DataFrame([user_input])

    # predict the class.
    output = model.predict(user_input_df)[0]

    probabilities = model.predict_proba(user_input_df)[0]

    # Get class labels from model (important for matching probabilities to class names)
    # class_labels = model.classes_.tolist() 

    return {
        "Predicted_Category": output,
        "Confidence" : max(probabilities),
        "Probabilities": {
            cls: float(prob)
            for cls, prob in zip(model.classes_, probabilities)
        }
    }
