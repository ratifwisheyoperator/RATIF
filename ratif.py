import json
import os

class Patient:
    # Class variable to track total patients
    total_patients = 0

    def __init__(self, name, age, gender, diagnosis, contact,date, district, religion, status):
        self._name = name
        self._age = age
        self._gender = gender
        self._diagnosis = diagnosis
        self._contact = contact
        self._date = date
        self._district = district
        self._religion = religion
        self._status = status
        Patient.total_patients += 1

    # Getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_gender(self):
        return self._gender

    def get_diagnosis(self):
        return self._diagnosis

    def get_contact(self):
        return self._contact

    def get_date(self):
        return self._date

    def get_district(self):
        return self._district

    def get_religion(self):
        return self._religion

    def get_status(self):
        return self._status

    # Setter methods
    def set_name(self, new_name):
        self._name = new_name

    def set_age(self, new_age):
        if Patient.validate_age(new_age):
            self._age = new_age
        else:
            print("Invalid age!")

    def set_gender(self, new_gender):
        self._gender = new_gender

    def set_diagnosis(self, new_diagnosis):
        self._diagnosis = new_diagnosis

    def set_contact(self, new_contact):
        self._contact = new_contact

    def set_date(self, new_date):
        self._date = new_date

    def set_district(self, new_district):
        self._district = new_district

    def set_religion(self, new_religion):
        self._religion = new_religion

    def set_status(self, new_status):
        self._status = new_status

    # Class Method
    @classmethod
    def show_total_patients(cls):
        print(f"Total patients tracked: {cls.total_patients}")

    # Static Method
    @staticmethod
    def validate_age(age):
        return 0 < age < 120

    # Convert patient to dictionary for JSON
    def to_dict(self):
        return {
            "name": self._name,
            "age": self._age,
            "gender": self._gender,
            "diagnosis": self._diagnosis,
            "contact": self._contact,
            "date": self._date,
            "district": self._district,
            "religion": self._religion,
            "status": self._status
        }


class PatientManagementSystem:
    def __init__(self, filename="patients.json"):
        self.filename = filename
        self.patients = self.load_patients()

    def load_patients(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                Patient.total_patients = len(data)
                return data
        return []

    def save_patients(self):
        with open(self.filename, "w") as file:
            json.dump(self.patients, file, indent=4)

    def add_patient(self, patient):
        self.patients.append(patient.to_dict())
        self.save_patients()
        print("Patient added successfully!")

    def view_patients(self):
        for idx, patient in enumerate(self.patients, start=1):
            print(f"{idx}. {patient}")

    def update_patient(self, index, key, value):
        if 0 <= index < len(self.patients):
            self.patients[index][key] = value
            self.save_patients()
            print("Patient updated successfully!")
        else:
            print("Invalid patient index!")

    def delete_patient(self, index):
        if 0 <= index < len(self.patients):
            self.patients.pop(index)
            Patient.total_patients -= 1
            self.save_patients()
            print("Patient deleted successfully!")
        else:
            print("Invalid patient index!")


# Example usage
if __name__ == "__main__":
    system = PatientManagementSystem()

    while True:
        print("\n--- Patient Management System ---")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Show Total Patients")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            diagnosis = input("Diagnosis: ")
            contact = input("Contact: ")
            date = input("date: ")
            district = input("District: ")
            religion = input("religion: ")
            status = input("status: ")
            patient = Patient(name, age, gender, diagnosis, contact, date, district, religion,status)
            system.add_patient(patient)

        elif choice == "2":
            system.view_patients()

        elif choice == "3":
            idx = int(input("Enter patient index to update: ")) - 1
            key = input("Enter field to update (name, age, gender, diagnosis, contact, date, district, religion,status ): ")
            value = input("Enter new value: ")
            if key == "age":
                value = int(value)
            system.update_patient(idx, key, value)

        elif choice == "4":
            idx = int(input("Enter patient index to delete: ")) - 1
            system.delete_patient(idx)

        elif choice == "5":
            Patient.show_total_patients()

        elif choice == "6":
            print("Exiting system...")
            break

        else:
            print("Invalid choice, try again.")
