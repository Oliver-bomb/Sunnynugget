class Patient:
    def __init__(self, name, age, symptoms):
        self.name = name
        self.age = age
        self.symptoms = symptoms
        self.triage_level = self.determine_triage_level()

    def determine_triage_level(self):
        if "chest pain" in self.symptoms or "difficulty breathing" in self.symptoms:
            return "Critical (Red)"
        elif "severe headache" in self.symptoms or "high fever" in self.symptoms:
            return "Urgent (Orange)"
        elif "mild headache" in self.symptoms or "cough" in self.symptoms:
            return "Less Urgent (Yellow)"
        else:
            return "Non-Urgent (Green)"

    def __str__(self):
        return f"Patient: {self.name}, Age: {self.age}, Triage Level: {self.triage_level}, Symptoms: {', '.join(self.symptoms)}"


def triage_system():
    patients = []
    print("Welcome to the Hospital Triage System.")
    
    while True:
        name = input("Enter patient's name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        
        age = input("Enter patient's age: ")
        symptoms = input("Enter patient's symptoms (comma separated): ").split(',')
        symptoms = [symptom.strip().lower() for symptom in symptoms]

        patient = Patient(name, age, symptoms)
        patients.append(patient)
        print(f"\n{patient}\n")

    print("All patients entered:")
    for patient in patients:
        print(patient)


if __name__ == "__main__":
    triage_system()
