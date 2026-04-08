# Patient Monitoring and Intervention Platform

A full-stack healthcare system that monitors patient adherence and generates personalized intervention strategies.

## Features
- **Real-time Monitoring**: Track medication, appointments, and lifestyle factors.
- **AI-Driven Risk Prediction**: Automatically classifies patients into LOW, MEDIUM, or HIGH risk categories.
- **Personalized Interventions**: Generates custom reminders and care team notifications.
- **Population Analytics**: Data visualization for adherence trends and risk distribution.

## Tech Stack
- **Backend**: FastAPI, SQLAlchemy, SQLite, Pydantic.
- **AI Engine**: Python (Logic-based scoring).
- **Frontend**: React (Vite), TailwindCSS, Chart.js.

## Project Structure
```text
patient-monitoring-platform/
├── backend/            # FastAPI Server
├── ai_engine/          # Risk Scoring & Interventions
├── frontend/           # React Dashboard
├── seed_data.py        # Database Seeding Script
└── README.md
```

## Setup Instructions

### Backend
1. Navigate to the `backend` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend
1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

### Seeding Data (Optional)
Once the backend is running, run the seed script from the root directory to populate initial data:
```bash
python seed_data.py
```

## API Examples

### Register Patient
**POST** `/patients/`
```json
{
  "name": "John Doe",
  "medication_taken": 28,
  "medication_total": 30,
  "appointments_attended": 4,
  "appointments_total": 4,
  "daily_steps": 8500,
  "sleep_hours": 7.5,
  "diet_followed": true
}
```

### Analyze Adherence
**POST** `/analyze/?patient_id=1`
**Response:**
```json
{
  "patient_id": 1,
  "risk_level": "LOW",
  "recommendations": [
    "Great job! Keep up your current routine.",
    "Continue tracking your health data daily."
  ]
}
```

## UI Screenshots Description
- **Dashboard**: Displays high-level cards for each patient with colored risk badges and current adherence status.
- **Add Patient**: A clean, white-space oriented form for inputting patient health metrics.
- **Analytics**: Contains a bar chart showing medication adherence percentages across the population and a pie chart for risk stratification.
