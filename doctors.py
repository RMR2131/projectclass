import csv
from os import path


class Doctor:
    
    ID, Name, Specialization, Working_Time, Qualification, Room_Number = '','','','','',''
    Updated_List = []    
    
    #Formats each doctor’s information (properties) in the same format used in the .txt file 
    def formatDrInfo(self):
        doc_property = []
        for records in self.Updated_List:
            formatting = records[0] + "_" + records[1] + "_" + records[2] + "_" + records[3] + "_" + records[4] + '_' + records[5] + '\n'
            doc_property.append(formatting)
        
        return doc_property
    
    def enterDrInfo(self):
        self.ID = input("Enter the doctor's ID: ")
        self.Name = input("Enter the doctor's name: ")
        self.Specialization = input("Enter the doctor's specialty: ")
        self.Working_Time = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        self.Qualification = input("Enter the doctor's qualification: ")
        self.Room_Number = input("Enter the doctor's room number: ")
        self.addDrToFile()
    
    def readDoctorsFile(self):
        List_of_Doctors = []
        #Checks if file exists
        if path.exists('doctors.txt'):
            f = open('doctors.txt','r')
            next(f)
            for x in list(f):
                splitting = x.split('_')
                splitting[len(splitting)-1] = splitting[len(splitting)-1].rstrip('\n')
                List_of_Doctors.append(splitting)
        else:
            print("No records of doctors yet. Insert one first")
        
        return List_of_Doctors
        
                 
    
    def searchDoctorById(self):
        Doctor_Found = None
        List_of_Doctors = self.readDoctorsFile()
        search = input("Enter the doctor Id: ")
        for x in List_of_Doctors:
            if x[0] == search:
                Doctor_Found = x
                break
        if Doctor_Found is not None:
            print(f'{"Id":{5}}{"Name":{30}}{"Specialty":{20}}{"Timing":{20}}{"Qualification":{20}}{"Room Number":{13}}','\n')
            self.displayDoctorInfo(Doctor_Found)
        else:
            print("Can't find the doctor with the same ID on the system")
    
    def searchDoctorByName(self):
        Doctor_Found = None
        List_of_Doctors = self.readDoctorsFile()
        search = input("Enter the doctor Id: ")
        for x in List_of_Doctors:
            if x[1] == search:
                Doctor_Found = x
                break
        if Doctor_Found is not None:
            print(f'{"Id":{5}}{"Name":{30}}{"Specialty":{20}}{"Timing":{20}}{"Qualification":{20}}{"Room Number":{13}}','\n')
            self.displayDoctorInfo(Doctor_Found)
        else:
            print("Can't find the doctor with the same name on the system")
            
    def displayDoctorInfo(self,doctor_info):
        print(f'{doctor_info[0]:{5}}{doctor_info[1]:{30}}{doctor_info[2]:{20}}{doctor_info[3]:{20}}{doctor_info[4]:{20}}{doctor_info[5]:{13}}','\n')
    
    
    def editDoctorInfo(self):
        doctor_index = None
        found = False
        List_of_Doctors = self.readDoctorsFile()
        search = input("Please enter the id of the doctor that you want to edit their information: ")
        try:
            for Doctor in List_of_Doctors:
                if search in Doctor:
                    doctor_index = List_of_Doctors.index(Doctor)
                    found = True         
        except:
            pass
        
        if found:
            print("Enter new Name: ")
            List_of_Doctors[doctor_index][1] = input()
            print("Enter new Specialist in: ")
            List_of_Doctors[doctor_index][2] = input()
            print("Enter new Timing: ")
            List_of_Doctors[doctor_index][3] = input()
            print("Enter new Qualification: ")
            List_of_Doctors[doctor_index][4] = input()
            print("Enter new Room number: ")
            List_of_Doctors[doctor_index][5] = input()
            self.Updated_List = List_of_Doctors
            self.writeListOfDoctorsToFile()
        else:
            print("Can't find the doctor with the same ID on the system")
    
    def displayDoctorsList(self):
        Doctor_List = self.readDoctorsFile()
        if len(Doctor_List) > 0:
            print(f'{"Id":{5}}{"Name":{30}}{"Specialty":{20}}{"Timing":{20}}{"Qualification":{20}}{"Room Number":{13}}','\n')
            for record in Doctor_List:
                self.displayDoctorInfo(record)
        else:
            print("No records of doctors yet. Insert one first")
    
    def writeListOfDoctorsToFile(self):
        formatted_list = self.formatDrInfo()
        f = open('doctors.txt','w')
        f.write('Id_Name_Specialty_Timing_Qualificatin_RoomNumber\n')
        
        for lines in formatted_list:
            f.writelines(lines)
        f.close()

    def addDrToFile(self):
        self.Updated_List = self.readDoctorsFile()
        self.Updated_List.append([self.ID,self.Name,self.Specialization,self.Working_Time,self.Qualification,self.Room_Number])
        self.writeListOfDoctorsToFile()
        

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
    
if __name__ == "__main__":
    start = Management()
    start.main()
