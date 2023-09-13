import json
import joblib
import pandas as pd
import os

MODEL_PATH = os.path.join(os.environ["LAMBDA_TASK_ROOT"], "model.joblib")

model = joblib.load(MODEL_PATH)

CLASS_NAMES = ['Iris-Setosa', 'Iris-Versicolour', 'Iris-Virginica']


def lambda_handler(event, context):
    '''
    Request format: {
        ...
        "body": {
            "features": {
                "sepal length (cm)": <value>,
                "sepal width (cm)": <value>,
                "petal length (cm)": <value>,
                "petal width (cm)": <value>
            }
        }
        ...
    }
    '''
    text = event['body']['features']
    X = pd.DataFrame(text, index=[0])
    prediction = model.predict(X)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Predicted class: {CLASS_NAMES[prediction[0]]}"
        }),
    }
