import os
from dotenv import load_dotenv
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

load_dotenv()

'''Loading configuration'''
prediction_endpoint = os.getenv('PredictionEndpoint')
prediction_key = os.getenv('PredictionKey')
project_id = os.getenv('ProjectID')
model_name = os.getenv('ModelName')


'''Authentication'''
credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
prediction_client=CustomVisionPredictionClient(endpoint=prediction_endpoint, credentials=credentials)

image_dir = r'D:\Internship\upload\Task4\test_image' 


'''Prediction'''
for image_name in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_name)
        with open(image_path, "rb") as image_data:
            results = prediction_client.classify_image(project_id, model_name, image_data)

            for prediction in results.predictions:
                if prediction.probability > 0.5:
                    print(f"{image_name}: {prediction.tag_name} ({prediction.probability:.4f})")
