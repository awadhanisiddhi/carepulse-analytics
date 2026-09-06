import pandas as pd

departments_df = pd.read_csv("data/departments.csv")
doctors_df = pd.read_csv("data/doctors.csv")
patients_df = pd.read_csv("data/patients.csv")
admissions_df = pd.read_csv("data/admissions.csv")
billing_df = pd.read_csv("data/billing.csv")

print("Departments:", departments_df.shape) #checked no.of rows and columns in each dataset
print("Doctors:", doctors_df.shape) #confirmed the amount of data generated
print("Patients:", patients_df.shape)
print("Admissions:", admissions_df.shape)
print("Billing:", billing_df.shape)

print("\nMissing values:") #checked for missing values 
print("Departments:", departments_df.isnull().sum().sum())
print("Doctors:", doctors_df.isnull().sum().sum())
print("Patients:", patients_df.isnull().sum().sum())
print("Admissions:", admissions_df.isnull().sum().sum())
print("Billing:", billing_df.isnull().sum().sum())

print("\nDuplicate rows:") #checked for duplicate rows 
print("Departments:", departments_df.duplicated().sum())
print("Doctors:", doctors_df.duplicated().sum())
print("Patients:", patients_df.duplicated().sum())
print("Admissions:", admissions_df.duplicated().sum())
print("Billing:", billing_df.duplicated().sum())

print("\nDuplicate IDs:") #checked for duplicate IDs
print("Departments:", departments_df["department_id"].duplicated().sum())
print("Doctors:", doctors_df["doctor_id"].duplicated().sum())
print("Patients:", patients_df["patient_id"].duplicated().sum())
print("Admissions:", admissions_df["admission_id"].duplicated().sum())
print("Billing:", billing_df["bill_id"].duplicated().sum())

print("\nInvalid foreign keys:") #checked whether IDs used in one table actually exist in the related table
print(
    "Admissions → Patients:",
    (~admissions_df["patient_id"].isin(patients_df["patient_id"])).sum()
)

print(
    "Admissions → Doctors:",
    (~admissions_df["doctor_id"].isin(doctors_df["doctor_id"])).sum()
)

print(
    "Admissions → Departments:",
    (~admissions_df["department_id"].isin(departments_df["department_id"])).sum()
)

print(
    "Billing → Admissions:",
    (~billing_df["admission_id"].isin(admissions_df["admission_id"])).sum()
)

print("\nDate validation:") #made sure all admission dates fall within 2024-25
print(
    "Invalid admission dates:",
    ((admissions_df["admission_date"] < "2024-01-01") |
     (admissions_df["admission_date"] > "2025-12-31")).sum()
)

print(
    "Discharge before admission:",
    (admissions_df["discharge_date"] < admissions_df["admission_date"]).sum()
)

print( #waiting times should be between 10-180 minutes
    "\nInvalid waiting times:",
    ((admissions_df["waiting_time_minutes"] < 10) |
     (admissions_df["waiting_time_minutes"] > 180)).sum()
)

print("\nEmergency priority validation:") #emergency admissions are validated
invalid_emergency = (
    ((admissions_df["admission_type"] == "Emergency") &
     (~admissions_df["emergency_priority"].isin(
         ["Critical", "High", "Medium", "Low"]
     )))
    |
    ((admissions_df["admission_type"] != "Emergency") &
     (admissions_df["emergency_priority"] != "Not Applicable"))
)

print("Invalid emergency priorities:", invalid_emergency.sum())

print("\nBilling validation:") #total bill= treatment cost+ medicine cost+room charges
invalid_total_bill = (
    billing_df["total_bill"]
    != billing_df["treatment_cost"]
    + billing_df["medicine_cost"]
    + billing_df["room_charges"]
)

print("Invalid total bills:", invalid_total_bill.sum())

invalid_insurance = ( #insurance covered should never be -ve
    (billing_df["insurance_covered"] < 0)
    |
    (billing_df["insurance_covered"] > billing_df["total_bill"])
)

print("Invalid insurance amounts:", invalid_insurance.sum())

valid_payment_statuses = [ #validated payment statuses
    "Paid",
    "Pending",
    "Partially Paid"
]

invalid_payment_status = (
    ~billing_df["payment_status"].isin(valid_payment_statuses)
)

print(
    "Invalid payment statuses:",
    invalid_payment_status.sum()
)

print("\nDATA VALIDATION COMPLETED SUCCESSFULLY.")