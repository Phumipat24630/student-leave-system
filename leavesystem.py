#Module
import csv

import pandas as pd

def CheckID(ID):
    LIST = ReadCSV('students.csv')
    for i in range(len(LIST)):
        if ID == LIST[i][0]:
            return True

    return False

def CheckDATE(DATE):
    if DATE.count('-') != 2:
        return False
    else:
        DD, MM, YYYY = DATE.split('-')
        if not DD.isdigit() or not MM.isdigit() or not YYYY.isdigit():
            return False
        else:
            DD = int(DD)
            MM = int(MM)
            YYYY = int(YYYY)
            Day28 = {2}
            Day30 = {4, 6, 9, 11}
            Day31 = {1, 3, 5, 7, 8, 10, 12}
            if MM in Day28 and (DD < 1 or DD > 28):
                return False
            elif MM in Day30 and (DD < 1 or DD > 30):
                return False
            elif MM in Day31 and (DD < 1 or DD > 31):
                return False
            else:
                return True

def CheckName(NAME):
    LIST = ReadCSV('students.csv')
    for i in range(len(LIST)):
        if NAME in LIST[i][1]:
            return True

    return False
    
def ReadCSV(filename):
    File = open(filename, 'r')
    CSV = csv.reader(File)

    LIST = []
    for row in CSV:
        LIST.append(row)
  
    return LIST

#interface
option = " "
while (option != "0"):
 print("MUICT Student Leave System")
 print("1. print a list of students")
 print("2. submit a leave request")
 print("3. check leave with class date")
 print("4. check leave with student ID")
 print("5. check leave with student first name")
 print("6. print leave summary")
 print("0. exit")
 option=str(input("Option: "))

#option1_printalistofstudents
 if option == "1":
     data = pd.read_csv("students.csv")
     print(data)
     print("===================")
     print()

#option2submitaleaveequest
 if option == "2":
    with open('leave.csv', 'a') as f:
        w = csv.writer(f, quoting=csv.QUOTE_NONE, lineterminator='\n')
        id = str(input("ID: "))
        if CheckID(id):
            leave = str(input("Leave (S=Sick/B=Business/T=Travel/O=Others): "))
            date = str(input("Class date (DD-MM-YYYY): "))
            if CheckDATE(date):
                w.writerow([id, leave, date])
            else:
                print("Invalid Class date, Please try again.")
        else:
            print("No ID in database, Please try again.")
                  
    print("===================\n")



#option3checkleavewithclassdate
 if option == "3":
    Date = input("Date (DD-MM-YYYY): ")
    if CheckDATE(Date):
        LIST_Leave = ReadCSV('leave.csv')
        LIST_Student = ReadCSV('students.csv')

        Student_Leave = []
        for i in range(len(LIST_Leave)):
            if Date == LIST_Leave[i][2]:
                for j in range(len(LIST_Student)):
                    if LIST_Leave[i][0] == LIST_Student[j][0]:
                        if LIST_Leave[i][1] == 'S':
                            ID = str(LIST_Student[j][0])
                            Name = str(LIST_Student[j][1]) + " " + str(LIST_Student[j][2])
                            Student_Leave.append("(Sick) " + ID + " " + Name)
                        elif LIST_Leave[i][1] == 'B':
                            ID = str(LIST_Student[j][0])
                            Name = str(LIST_Student[j][1]) + " " + str(LIST_Student[j][2])
                            Student_Leave.append("(Business) " + ID + " " + Name)
                        elif LIST_Leave[i][1] == 'T':
                            ID = str(LIST_Student[j][0])
                            Name = str(LIST_Student[j][1]) + " " + str(LIST_Student[j][2])
                            Student_Leave.append("(Travel) " + ID + " " + Name)
                        elif LIST_Leave[i][1] == 'O':
                            ID = str(LIST_Student[j][0])
                            Name = str(LIST_Student[j][1]) + " " + str(LIST_Student[j][2])
                            Student_Leave.append("(Others) " + ID + " " + Name)
                        break

        print(f"There are {len(Student_Leave)} students leave on {Date}")
        for i in range(len(Student_Leave)):
            print(Student_Leave[i])
            
    else:
        print("Invalid Date, Please try again.")
          
    print("===================\n")

#option4checkleavewithstudentID
 if option == "4":
    ID = input("ID: ")
    if CheckID(ID):
        LIST_Leave = ReadCSV('leave.csv')
        LIST_Student = ReadCSV('students.csv')

        Student_Leave = []
        for i in range(len(LIST_Leave)):
            if ID == LIST_Leave[i][0]:
                for j in range(len(LIST_Student)):
                    if LIST_Leave[i][0] == LIST_Student[j][0]:
                        if LIST_Leave[i][1] == 'S':
                            ID = str(LIST_Student[j][0])
                            Name = str(LIST_Student[j][1]) + " " + str(LIST_Student[j][2])
                            Student_Leave.append(ID + " " + Name + ": Sick Leave on " + LIST_Leave[i][2])
                        elif LIST_Leave[i][1] == 'B':
                            ID = str(LIST_Student[j][0])
                            Name = str(LIST_Student[j][1]) + " " + str(LIST_Student[j][2])
                            Student_Leave.append(ID + " " + Name + ": Business Leave on " + LIST_Leave[i][2])
                        elif LIST_Leave[i][1] == 'T':
                            ID = str(LIST_Student[j][0])
                            Name = str(LIST_Student[j][1]) + " " + str(LIST_Student[j][2])
                            Student_Leave.append(ID + " " + Name + ": Travel Leave on " + LIST_Leave[i][2])
                        elif LIST_Leave[i][1] == 'O':
                            ID = str(LIST_Student[j][0])
                            Name = str(LIST_Student[j][1]) + " " + str(LIST_Student[j][2])
                            Student_Leave.append(ID + " " + Name + ": Others Leave on " + LIST_Leave[i][2])
                        break

        if len(Student_Leave) == 0:
            print("There is no student leave record.")
        else:
            for i in range(len(Student_Leave)):
                print(Student_Leave[i])
            
    else:
        print("No ID in database, Please try again.")
          
    print("===================\n")




#option5checkleavewithfirstname
 if option == "5":
    String = input("Firstname: ")
    if CheckName(String):
        LIST_Leave = ReadCSV('leave.csv')
        LIST_Student = ReadCSV('students.csv')


        All_Student_Leave = []
        for i in range(len(LIST_Leave)):
            for j in range(len(LIST_Student)):
                if LIST_Leave[i][0] == LIST_Student[j][0]:
                    JOIN = LIST_Leave[i] + [LIST_Student[j][1], LIST_Student[j][2]]
                    All_Student_Leave.append(JOIN)
            

        Student_Leave = []
        for i in range(len(All_Student_Leave)):

            if String in All_Student_Leave[i][3]:
                if All_Student_Leave[i][1] == 'S':
                    ID = str(All_Student_Leave[i][0])
                    Name = str(All_Student_Leave[i][3]) + " " + str(All_Student_Leave[i][4])
                    Student_Leave.append(ID + " " + Name + ": Sick Leave on " + All_Student_Leave[i][2])
                elif All_Student_Leave[i][1] == 'B':
                    ID = str(LIST_Student[i][0])
                    Name = str(All_Student_Leave[i][3]) + " " + str(All_Student_Leave[i][4])
                    Student_Leave.append(ID + " " + Name + ": Sick Leave on " + All_Student_Leave[i][2])
                elif All_Student_Leave[i][1] == 'T':
                    ID = str(LIST_Student[i][0])
                    Name = str(All_Student_Leave[i][3]) + " " + str(All_Student_Leave[i][4])
                    Student_Leave.append(ID + " " + Name + ": Sick Leave on " + All_Student_Leave[i][2])
                elif All_Student_Leave[i][1] == 'O':
                    ID = str(LIST_Student[i][0])
                    Name = str(All_Student_Leave[i][3]) + " " + str(All_Student_Leave[i][4])
                    Student_Leave.append(ID + " " + Name + ": Sick Leave on " + All_Student_Leave[i][2])

        if len(Student_Leave) == 0:
            print("There is no student leave record.")
        else:
            for i in range(len(Student_Leave)):
                print(Student_Leave[i])
            
    else:
        print("There is no student found.")
          
    print("===================\n")

#option6printleavesummary
 if option == "6":
    LIST_Leave = ReadCSV('leave.csv')
    LIST_Student = ReadCSV('students.csv')




    DICT_Student_Leave = {'Sick':[],'Business':[],'Travel':[],'Others':[],}
    for i in range(len(LIST_Leave)):
        for j in range(len(LIST_Student)):
            if LIST_Leave[i][0] == LIST_Student[j][0]:
                JOIN = LIST_Leave[i] + [LIST_Student[j][1], LIST_Student[j][2]]
                if JOIN[1] == 'S':
                    ID = str(JOIN[0])
                    Name = str(JOIN[3]) + " " + str(JOIN[4])
                    
                    DICT_Student_Leave['Sick'].append(ID + " " + Name + " leave on " + JOIN[2])
                    
                elif JOIN[1] == 'B':
                    ID = str(JOIN[0])
                    Name = str(JOIN[3]) + " " + str(JOIN[4])
                    
                    DICT_Student_Leave['Business'].append(ID + " " + Name + " leave on " + JOIN[2])
                    
                elif JOIN[1] == 'T':
                    ID = str(JOIN[0])
                    Name = str(JOIN[3]) + " " + str(JOIN[4])
                    
                    DICT_Student_Leave['Travel'].append(ID + " " + Name + " leave on " + JOIN[2])
                    
                elif JOIN[1] == 'O':
                    ID = str(JOIN[0])
                    Name = str(JOIN[3]) + " " + str(JOIN[4])
                    
                    DICT_Student_Leave['Others'].append(ID + " " + Name + " leave on " + JOIN[2])
    
    for KEY in DICT_Student_Leave.keys():
        if len(DICT_Student_Leave[KEY]) == 0:
            print(" None")
        else:
            print(KEY)
            for i in range(len(DICT_Student_Leave[KEY])):
                print(" ",end="")
                print(DICT_Student_Leave[KEY][i])
          
    print("===================\n")





#option0_exit
if option == "0":
   print("Thank you for using my program")