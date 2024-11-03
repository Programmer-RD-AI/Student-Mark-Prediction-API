from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from joblib import load
import numpy as np

app = Flask(__name__)
api = Api(app)

# Load the saved model
model = load("model.joblib")


class NextSemesterMarkPredictor(Resource):
    def post(self):
        # Get data from the request
        data = request.get_json()

        # Prepare predictions
        predictions = []

        for student in data:
            # Extract student information
            student_id = student["student_id"]
            syllabus = student["syllabus"]
            subject = student["subject"]
            marks = student["marks"]

            # Get previous semester marks
            sem_1 = int(marks["sem_1"])
            sem_2 = int(marks["sem_2"])
            sem_3 = int(marks["sem_3"])

            # Log the input values for debugging
            print(
                f"Student ID: {student_id}, sem_1: {sem_1}, sem_2: {sem_2}, sem_3: {sem_3}"
            )

            # Predict second semester mark using the model
            predicted_sem_2 = model.predict([[sem_1]])[0]
            difference_sem_2 = predicted_sem_2 - sem_2

            # Predict third semester mark using the model
            predicted_sem_3 = model.predict([[predicted_sem_2]])[0]
            difference_sem_3 = predicted_sem_3 - sem_3

            # Calculate the average difference
            average_difference = (difference_sem_2 + difference_sem_3) / 2

            # Adjust the predicted third semester mark
            adjusted_predicted_sem_3 = round(predicted_sem_3 + average_difference, 2)

            # Predict the fourth semester mark using the adjusted third semester mark
            predicted_sem_4 = model.predict([[adjusted_predicted_sem_3]])[0]

            # Convert predictions to regular floats
            predicted_sem_2 = float(predicted_sem_2)
            predicted_sem_3 = float(predicted_sem_3)
            predicted_sem_4 = float(predicted_sem_4)

            # Prepare prediction result
            prediction = {
                "student_id": student_id,
                "syllabus": syllabus,
                "subject": subject,
                "predicted_semester_4_mark": round(predicted_sem_4, 2),
            }
            predictions.append(prediction)

        return jsonify(predictions)


# Add resource to the API
api.add_resource(NextSemesterMarkPredictor, "/")

if __name__ == "__main__":
    app.run(debug=True)
