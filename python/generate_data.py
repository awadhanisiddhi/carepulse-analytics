import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker("en_IN")

departments = [
    ("D001", "Cardiology", 50),
    ("D002", "Neurology", 40),
    ("D003", "Orthopedics", 60),
    ("D004", "Pediatrics", 50),
    ("D005", "General Medicine", 80),
    ("D006", "Emergency", 70),
    ("D007", "Gynecology", 40),
    ("D008", "Oncology", 35),
    ("D009", "Dermatology", 25),
    ("D010", "Gastroenterology", 50)
]

departments_df = pd.DataFrame(
    departments,
    columns=["department_id", "department_name", "bed_capacity"]
)

# print(departments_df)

specializations = {
    "D001": ["Cardiologist", "Interventional Cardiologist", "Cardiac Surgeon"],
    "D002": ["Neurologist", "Neurosurgeon", "Neurophysician"],
    "D003": ["Orthopedic Surgeon", "Sports Medicine Specialist", "Joint Replacement Specialist"],
    "D004": ["Pediatrician", "Neonatologist", "Child Specialist"],
    "D005": ["General Physician", "Internal Medicine Specialist"],
    "D006": ["Emergency Physician", "Trauma Specialist", "Critical Care Specialist"],
    "D007": ["Gynecologist", "Obstetrician", "Reproductive Health Specialist"],
    "D008": ["Oncologist", "Medical Oncologist", "Radiation Oncologist"],
    "D009": ["Dermatologist", "Cosmetologist", "Dermatologic Surgeon"],
    "D010": ["Gastroenterologist", "Hepatologist", "GI Surgeon"]
}

doctor_ids = [f"DOC{i:03d}" for i in range(1, 101)]

doctors = []

for doctor_id in doctor_ids:
    department_id = random.choice(list(specializations.keys()))
    specialization = random.choice(specializations[department_id])
    doctor_name = f"Dr. {fake.name()}"
    experience_years = random.randint(2, 30)

    doctors.append((
        doctor_id,
        doctor_name,
        department_id,
        specialization,
        experience_years
    ))

doctors_df = pd.DataFrame(
    doctors,
    columns=[
        "doctor_id",
        "doctor_name",
        "department_id",
        "specialization",
        "experience_years"
    ]
)

print(doctors_df.head(10))
print("\nNumber of doctors:", len(doctors_df))

cities = [
    "Pune",
    "Mumbai",
    "Nashik",
    "Nagpur",
    "Aurangabad",
    "Kolhapur",
    "Satara",
    "Ahmednagar",
    "Thane",
    "Sangli"
]

blood_groups = [
    "A+",
    "A-",
    "B+",
    "B-",
    "AB+",
    "AB-",
    "O+",
    "O-"
]

insurance_types = [
    "Private Insurance",
    "Government Insurance",
    "Self Pay",
    "Corporate Insurance"
]

genders = [
    "Male",
    "Female",
    "Other"
]

patient_ids = [f"PAT{i:05d}" for i in range(1, 10001)]
patients = []

for patient_id in patient_ids:
    patient_name = fake.name()
    age = np.random.randint(1, 91)
    gender = np.random.choice(
        genders,
        p=[0.48, 0.50, 0.02]
    )
    city = random.choice(cities)
    blood_group = random.choice(blood_groups)
    phone = "+91" + str(random.randint(6000000000, 9999999999))
    insurance_type = np.random.choice(
        insurance_types,
        p=[0.45, 0.25, 0.20, 0.10]
    )

    patients.append((
        patient_id,
        patient_name,
        age,
        gender,
        city,
        blood_group,
        phone,
        insurance_type
    ))

patients_df = pd.DataFrame(
    patients,
    columns=[
        "patient_id",
        "patient_name",
        "age",
        "gender",
        "city",
        "blood_group",
        "phone",
        "insurance_type"
    ]
)

print("\nPatient sample:")
print(patients_df.head(10))

print("\nNumber of patients:", len(patients_df))



admission_types = [
    "Emergency",
    "Scheduled",
    "Referral",
    "Transfer"
]

emergency_priorities = [
    "Critical",
    "High",
    "Medium",
    "Low"
]


diagnoses = [
    "Hypertension",
    "Diabetes",
    "Fracture",
    "Pneumonia",
    "Asthma",
    "Migraine",
    "Heart Disease",
    "Gastroenteritis",
    "Appendicitis",
    "Arthritis",
    "Skin Infection",
    "Kidney Disease",
    "Cancer",
    "Viral Infection",
    "Pregnancy Complications"
]

department_diagnoses = {
    "D001": ["Heart Disease", "Hypertension"],
    "D002": ["Migraine", "Stroke", "Neurological Disorder"],
    "D003": ["Fracture", "Arthritis", "Joint Injury"],
    "D004": ["Pneumonia", "Asthma", "Viral Infection"],
    "D005": ["Diabetes", "Hypertension", "Viral Infection", "Kidney Disease"],
    "D006": ["Trauma", "Fracture", "Asthma", "Heart Disease", "Appendicitis"],
    "D007": ["Pregnancy Complications", "Gynecological Disorder"],
    "D008": ["Cancer"],
    "D009": ["Skin Infection", "Dermatitis"],
    "D010": ["Gastroenteritis", "Appendicitis", "Liver Disease"]
}

admission_ids = [f"ADM{i:05d}" for i in range(1, 15001)]

admissions = []

start_date = pd.Timestamp("2024-01-01")
end_date = pd.Timestamp("2025-12-31")

def generate_admission_date():
    return pd.Timestamp(
        fake.date_between(
            start_date=start_date,
            end_date=end_date
        )
    )

def generate_length_of_stay():
    return np.random.randint(1, 15)

def generate_discharge_date(admission_date, length_of_stay):
    return admission_date + pd.Timedelta(days=length_of_stay)

test_admission_date = generate_admission_date()
test_length_of_stay = generate_length_of_stay()
test_discharge_date = generate_discharge_date(
    test_admission_date,
    test_length_of_stay
)

# print("Test admission date:", test_admission_date)
# print("Test length of stay:", test_length_of_stay)
# print("Test discharge date:", test_discharge_date)

for admission_id in admission_ids:
    patient_id = random.choice(patient_ids)

    doctor_id = random.choice(doctor_ids)

    doctor_department = doctors_df.loc[
        doctors_df["doctor_id"] == doctor_id,
        "department_id"
    ].iloc[0]

    department_id = doctor_department

    admission_date = generate_admission_date()

    length_of_stay = generate_length_of_stay()

    discharge_date = generate_discharge_date(
        admission_date,
        length_of_stay
    )

    admission_type = np.random.choice(
        admission_types,
        p=[0.40, 0.35, 0.15, 0.10]
    )

    if admission_type == "Emergency":
        emergency_priority = np.random.choice(
            emergency_priorities,
            p=[0.15, 0.30, 0.40, 0.15]
        )
    else:
        emergency_priority = "Not Applicable"

    diagnosis = random.choice(
        department_diagnoses[department_id]
    )

    waiting_time_minutes = np.random.randint(10, 181)

    admissions.append((
        admission_id,
        patient_id,
        doctor_id,
        department_id,
        admission_date,
        discharge_date,
        admission_type,
        diagnosis,
        waiting_time_minutes,
        emergency_priority
    ))

admissions_df = pd.DataFrame(
    admissions,
    columns=[
        "admission_id",
        "patient_id",
        "doctor_id",
        "department_id",
        "admission_date",
        "discharge_date",
        "admission_type",
        "diagnosis",
        "waiting_time_minutes",
        "emergency_priority"
    ]
)

invalid_diagnoses = admissions_df[
    ~admissions_df.apply(
        lambda row: row["diagnosis"] in department_diagnoses[row["department_id"]],
        axis=1
    )
]

# print("\nInvalid department-diagnosis records:", len(invalid_diagnoses))

invalid_dates = admissions_df[
    admissions_df["discharge_date"] <= admissions_df["admission_date"]
]

# print("Invalid admission dates:", len(invalid_dates))

invalid_waiting_times = admissions_df[
    (admissions_df["waiting_time_minutes"] < 10) |
    (admissions_df["waiting_time_minutes"] > 180)
]


print("\nAdmission sample:")
print(admissions_df.head(10))
print("\nNumber of admissions:", len(admissions_df))

print("\nInvalid department-diagnosis records:", len(invalid_diagnoses))
print("Invalid admission dates:", len(invalid_dates))
print("Invalid waiting times:", len(invalid_waiting_times))

invalid_priorities = admissions_df[
    (
        (admissions_df["admission_type"] == "Emergency") &
        (admissions_df["emergency_priority"] == "Not Applicable")
    )
    |
    (
        (admissions_df["admission_type"] != "Emergency") &
        (admissions_df["emergency_priority"] != "Not Applicable")
    )
]

print("Invalid emergency priorities:", len(invalid_priorities))

print("\nEmergency priority distribution:")
print(admissions_df["emergency_priority"].value_counts())

payment_statuses = [
    "Paid",
    "Pending",
    "Partially Paid"
]

bill_ids = [f"BILL{i:05d}" for i in range(1, 15001)]

billing = []

for bill_id, admission_id in zip(bill_ids, admission_ids):
    admission_row = admissions_df[
    admissions_df["admission_id"] == admission_id
    ].iloc[0]

    length_of_stay = (
    admission_row["discharge_date"]
    - admission_row["admission_date"]
    ).days
    treatment_cost = np.random.randint(5000, 100001)
    medicine_cost = np.random.randint(1000, 30001)
    room_charge_per_day = np.random.randint(1000, 5001)

    room_charges = room_charge_per_day * length_of_stay
    total_bill = treatment_cost + medicine_cost + room_charges
    insurance_covered = round(
    total_bill * np.random.uniform(0.50, 0.90),
    2
    )
    payment_status = np.random.choice(
    payment_statuses,
    p=[0.70, 0.20, 0.10]
    )
    billing.append((
    bill_id,
    admission_id,
    treatment_cost,
    medicine_cost,
    room_charges,
    total_bill,
    insurance_covered,
    payment_status
    ))

billing_df = pd.DataFrame(
    billing,
    columns=[
        "bill_id",
        "admission_id",
        "treatment_cost",
        "medicine_cost",
        "room_charges",
        "total_bill",
        "insurance_covered",
        "payment_status"
    ]
)

print("\nBilling sample:")
print(billing_df.head(10))

print("\nNumber of billing records:", len(billing_df))

invalid_total_bill = billing_df[
    billing_df["total_bill"] != (
        billing_df["treatment_cost"]
        + billing_df["medicine_cost"]
        + billing_df["room_charges"]
    )
]

print("Invalid total bills:", len(invalid_total_bill))

invalid_insurance = billing_df[
    billing_df["insurance_covered"] > billing_df["total_bill"]
]

print("Invalid insurance amounts:", len(invalid_insurance))

print("\nPayment status distribution:")
print(billing_df["payment_status"].value_counts())

departments_df.to_csv("data/departments.csv", index=False)
doctors_df.to_csv("data/doctors.csv", index=False)
patients_df.to_csv("data/patients.csv", index=False)
admissions_df.to_csv("data/admissions.csv", index=False)
billing_df.to_csv("data/billing.csv", index=False)