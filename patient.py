class Patient:

    def __init__(self, pid, Name, Disease, Gender, Age):
        self.pid = pid
        self.Name = Name
        self.Disease = Disease
        self.Gender = Gender
        self.Age = Age
    
    def formatPatientInfo(self):
        return f"{self.pid}_{self.Name}_{self.Disease}_{self.Gender}_{self.Age}"

    def enterPatientInfo(self):
        self.pid = input("Enter Patient ID: ")
        self.Name = input("Enter Patient Name: ")
        self.Disease = input("Enter Patient Disease: ")
        self.Gender = input("Enter Patient Gender: ")
        self.Age = input("Enter Patient Age: ")

    def readPatientsFile(self, file_name):
        patients_list = []
        with open(file_name, "r") as file:
            for line in file:
                patient_info = line.split("_")
                patients_list.append(self.__init__(patient_info[0], patient_info[1], patient_info[2], patient_info[3], patient_info[4]))
        return patients_list

    def searchPatientById(self, id, patients_list):
        for patient in patients_list:
            if patient.pid == id:
                return patient
        return None

    def displayPatientInfo(self):
        print(f"Patient ID: {self.pid}")
        print(f"Patient Name: {self.Name}")
        print(f"Patient Disease: {self.Disease}")
        print(f"Patient Gender: {self.Gender}")
        print(f"Patient Age: {self.Age}")

    def editPatientInfo(self, id, patients_list):
        index = -1
        for i in range(len(patients_list)):
            if patients_list[i].pid == id:
                index = i
        if index == -1:
            return False
        self.enterPatientInfo()
        patients_list[index] = self
        return True

    def displayPatientsList(self, patients_list):
        for patient in patients_list:
            patient.displayPatientInfo()
            print()

    def writeListOfPatientsToFile(self, patients_list, file_name):
        with open(file_name, "w") as file:
            for patient in patients_list:
                file.write(patient.formatPatientInfo() + "\n")
    
    def addPatientToFile(self, file_name):
        with open(file_name, "a") as file:
            self.enterPatientInfo()
            file.write(self.formatPatientInfo() + "\n")
           
