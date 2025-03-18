# Healthcare Backend

## Overview
This project is a backend system for a healthcare application built using Django, Django REST Framework (DRF), and PostgreSQL. The system provides authentication, patient and doctor management, and patient-doctor mapping functionalities with secure RESTful APIs.

## Features
- **User Authentication:** JWT-based authentication using `djangorestframework-simplejwt`.
- **Patient Management:** CRUD operations for patients.
- **Doctor Management:** CRUD operations for doctors.
- **Patient-Doctor Mapping:** Assign and manage doctors for patients.
- **Role-based Access Control:** Secure endpoints with authentication.

## Tech Stack
- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Token)
- **Environment Management:** `dotenv`

## Installation & Setup

### Prerequisites
- Python 
- PostgreSQL
- Git

### Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/Dhruvil2511/healthcare_backend.git
   cd healthcare_backend
   ```
2. **Create a virtual environment and activate it**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up environment variables**
   - Create a `.env` file in the project root and add:
     ```env
      DJANGO_SECRET_KEY = your django secret
      POSTGRES_DB_NAME = your db name
      POSTGRES_DB_USER = your db username
      POSTGRES_DB_PASSWORD = your db password
      POSTGRES_DB_HOST = your db host 
      POSTGRES_DB_PORT = your db port 
     ```
5. **Apply migrations**
   ```sh
   python manage.py migrate
   ```
6. **Run the development server**
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and get JWT token

### Patient Management
- `POST /api/patients/` - Add a new patient
- `GET /api/patients/` - List all patients
- `GET /api/patients/<id>/` - Retrieve a specific patient
- `PUT /api/patients/<id>/` - Update a patient record
- `DELETE /api/patients/<id>/` - Delete a patient

### Doctor Management
- `POST /api/doctors/` - Add a new doctor
- `GET /api/doctors/` - List all doctors
- `GET /api/doctors/<id>/` - Retrieve a specific doctor
- `PUT /api/doctors/<id>/` - Update a doctor record
- `DELETE /api/doctors/<id>/` - Delete a doctor

### Patient-Doctor Mapping
- `POST /api/mappings/` - Assign a doctor to a patient
- `GET /api/mappings/` - List all patient-doctor mappings
- `GET /api/mappings/doctors/<patient_id>/` - Get all doctors assigned to a specific patient
- `DELETE /api/mappings/<id>/` - Remove a doctor from a patient

### Post Endpoints Request Bodies

#### Register a new user
**Endpoint:** `POST /api/auth/register/`  
**Request Body:**
```json
{
  "username": "john",
  "email": "johndoe@example.com",
  "password": "securepassword123",
  "confirm_password":"securepassword123"
}
```

#### Login
**Endpoint:** `POST /api/auth/login/`  
**Request Body:**
```json
{
  "username":"john",
  "password": "securepassword123"
}
```

#### Add a new patient
**Endpoint:** `POST /api/patients/`  
**Request Body:**
```json
{
  "first_name": "Jane",
  "last_name": "Doe",
  "dob": "1990-05-20",
  "gender": "F",
  "phone": "1234567890",
  "medical_history": "Diabetes"
}
```

#### Add a new doctor
**Endpoint:** `POST /api/doctors/`  
**Request Body:**
```json
{
  "name": "Dr. Smith",
  "experience_years":10,
  "specialization": "Cardiology",
  "phone": "9876543210"
}
```

#### Assign a doctor to a patient
**Endpoint:** `POST /api/mappings/`  
**Request Body:**
```json
{
  "patient_id": 1,
  "doctor_id": 5
}
```

## License
MIT License

