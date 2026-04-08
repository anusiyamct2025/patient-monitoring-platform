import requests
import json

BASE_URL = "http://localhost:8000"

patients = [
    {
        "name": "John Doe",
        "medication_taken": 28,
        "medication_total": 30,
        "appointments_attended": 4,
        "appointments_total": 4,
        "daily_steps": 8500,
        "sleep_hours": 7.5,
        "diet_followed": True
    },
    {
        "name": "Jane Smith",
        "medication_taken": 15,
        "medication_total": 30,
        "appointments_attended": 2,
        "appointments_total": 4,
        "daily_steps": 3000,
        "sleep_hours": 5.0,
        "diet_followed": False
    },
    {
        "name": "Robert Brown",
        "medication_taken": 20,
        "medication_total": 30,
        "appointments_attended": 3,
        "appointments_total": 4,
        "daily_steps": 5500,
        "sleep_hours": 6.5,
        "diet_followed": True
    }
]

def seed():
    print("Seeding data...")
    for p in patients:
        try:
            # Create patient
            resp = requests.post(f"{BASE_URL}/patients/", json=p)
            patient_id = resp.json()['id']
            print(f"Created patient {p['name']} with ID {patient_id}")
            
            # Trigger analysis
            analysis_resp = requests.post(f"{BASE_URL}/analyze/?patient_id={patient_id}")
            print(f"Analyzed risk for {p['name']}: {analysis_resp.json()['risk_level']}")
        except Exception as e:
            print(f"Error seeding {p['name']}: {e}")

if __name__ == "__main__":
    seed()
