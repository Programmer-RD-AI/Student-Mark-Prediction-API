import requests

# URL of the Flask API
url = "http://127.0.0.1:5000/"

# Example student data
data = [
    {
        "student_id": "GIS-2024-0011",
        "syllabus": "Edexcel",
        "subject": "1",
        "marks": {
            "sem_1": "70",
            "sem_2": "68",  # Actual second semester mark
            "sem_3": "72",  # Actual third semester mark
        },
    },
    {
        "student_id": "GIS-2024-0013",
        "syllabus": "Edexcel",
        "subject": "1",
        "marks": {
            "sem_1": "75",
            "sem_2": "73",  # Actual second semester mark
            "sem_3": "76",  # Actual third semester mark
        },
    },
    {
        "student_id": "GIS-2024-0015",
        "syllabus": "Edexcel",
        "subject": "1",
        "marks": {
            "sem_1": "50",
            "sem_2": "90",  # Actual second semester mark
            "sem_3": "82",  # Actual third semester mark
        },
    },
]

# Send POST request
response = requests.post(url, json=data)

# Print the response from the API
print(response.json())
