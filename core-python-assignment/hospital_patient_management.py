class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

def search_patients(patients, search_disease):
    result = [patient['Name'] for patient in patients if patient['Disease'] == search_disease]
    return result

# input
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = "Flu"

# search patients
patients_with_disease = search_patients(patients, search_disease)
print(f"Patients with {search_disease}: {patients_with_disease}")
