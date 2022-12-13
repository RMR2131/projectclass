import csv
from os import path

class Management():
    def main(self):
        while True:
            choice = int(input("""
Welcome to Alberta Hospital (AH) Managment system 
Select from the following options, or select 0 to stop: 
1 - 	Doctors
2 - 	Facilities
3 - 	Laboratories
4 - 	Patients

"""))
            match choice:
                case 0:
                    print("The program will now exit.")
                    exit()
                case 1:
                    self.doctor_menu()
                case 2:
                    self.faci_menu()
                case 3:
                    self.lab_menu()
                case 4:
                    self.patient_menu()
    
    def doctor_menu(self):
        doc = Doctor()
        while True:
            choice = int(input("""
Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

"""))
            match choice:
                case 1:
                    doc.displayDoctorsList()
                case 2:
                    doc.searchDoctorById()
                case 3:
                    doc.searchDoctorByName()
                case 4:
                    doc.enterDrInfo()
                case 5:
                    doc.editDoctorInfo()
                case 6:
                    break
    
    def faci_menu(self):
        faci = Facility()
        while True:
            choice = int(input("""
Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu

"""))
            match choice:
                case 1:
                    faci.displayFacilities()
                case 2:
                    faci.addFacility()
                case 3:
                    break
    
    
    def lab_menu(self):
        lab = Laboratory()
        while True:
            choice = int(input("""
Laboratories Menu:
1 - Display laboratories list
2 - Add laboratory
3 - Back to the Main Menu

"""))
            match choice:
                case 1:
                    lab.displayLabsList()
                case 2:
                    lab.enterLaboratoryInfo()
                case 3:
                    break
    
    def patient_menu(self):
        patient = Patient()
        while True:
            choice = int(input("""
Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

"""))
            match choice:
                case 1:
                    patient.displayPatientsList()
                case 2:
                    patient.searchPatientById()
                case 3:
                    patient.enterPatientInfo()
                case 4:
                    patient.editPatientInfo()
                case 5:
                    break


if __name__ == "__main__":
    start = Management()
    start.main()
     