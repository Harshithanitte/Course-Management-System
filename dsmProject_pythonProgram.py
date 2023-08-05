import mysql.connector
myconnection=mysql.connector.connect(host="localhost",user="root",password="qwerty@123!",database="elearning")
if myconnection:
    print("Connection is successful!")
cur=myconnection.cursor()

###ADMIN MENUE###
def admin_menue():
    while True:
        myconnection=mysql.connector.connect(host="localhost",user="root",password="qwerty@123!",database="elearning")
        cur=myconnection.cursor()
        print("""
                                                  _________________________________________________
        
                                                            i)INSERT :                           

                                                                       1.TO STUDENT
                                                                       2.TO COURSE
                                                                       3.TO INSTRUCTOR
                                                                       4.TO DOMAIN
                                                            ii)UPDATE :

                                                                       5.COURSE
                                                                       6.INSTRUCTOR
                          

                                                            iii)DELETE :

                                                                       7.STUDENT
                                                                       8.COURSE
                                                                       9.INSTRUCTOR
                                                                       10.DOMAIN
                          
                                                            iv)VIEW :

                                                                       11.RESULT
                                                                       12.PROGRESS
                          
                                                            13.EXIT ADMIN
                                                  ___________________________________________________

                                            """);
        ch=int(input("Enter your choice : "))
        if ch==1:
            sid=input("Enter sid : ")
            name=input("Enter name : ")
            clg=input("Enter college name : ")
            email=input("Enter E-mail : ")
            age=input("Enter age : ")
            gender=input("Enter gender : ")
            dob=input("Enter DOB : ")
            try:
                cur.execute("insert into student values('%s','%s','%s','%s',%s,'%s','%s')"%(sid,name,clg,email,age,gender,dob))
                myconnection.commit()
                myconnection.close()
                print("Record inserted successfully!!")
            except:
                print("Insert record unsuccessful!!");
                
        elif ch==2:
            cid=input("Enter cid : ")
            name=input("Enter name : ")
            fees=input("Enter fees : ")
            dur=input("Enter duration : ")
            iid=input("Enter iid : ")
            try:
                cur.execute("insert into course values('%s','%s',%s,%s,'%s')"%(cid,name,fees,dur,iid))
                myconnection.commit()
                myconnection.close()
                print("Record inserted successfully!!")
            except:
                print("Insert record unsuccessful!!");
        elif ch==3:
            iid=input("Enter iid : ")
            name=input("Enter name : ")
            salary=input("Enter salary : ")
            domain=input("Enter domain : ")
            try:
                cur.execute("insert into instructor values('%s','%s',%s,'%s')"%(iid,name,salary,domain))
                myconnection.commit()
                myconnection.close()
                print("Record inserted successfully!!")
            except:
                print("Insert record unsuccessful!!");
        elif ch==4:
            did=input("Enter did : ")
            name=input("Enter name : ")
            iid=input("Enter iid : ")
            tp=input("Enter instructor trained period :")
            try:
                cur.execute("insert into domain values('%s','%s','%s',%s)"%(did,name,iid,tp))
                myconnection.commit()
                myconnection.close()
                print("Record inserted successfully!!")
            except:
                print("Insert record unsuccessful!!");
        elif ch==5:
            cid=input("Enter cid : ")
            fees=input("Enter new fees : ")
            dur=input("Enter new duration : ")
            try:
                cur.execute("update course set fees=%s and duration=%s where cid='%s'"%(fees,dur,cid))
                myconnection.commit()
                myconnection.close()
                print("Record updated successfully!!")
            except:
                print("Update record unsuccessful!!");
        elif ch==6:
            iid=input("Enter iid : ")
            salary=input("Enter new salary : ")
            try:
                cur.execute("update instructor set salary=%s where iid='%s'"%(salary,iid))
                myconnection.commit()
                myconnection.close()
                print("Record updated successfully!!")
            except:
                print("Update record unsuccessful!!");
        elif ch==7:
            sid=input("Enter sid : ")
            try:
                cur.execute("delete from student where sid='%s'"%(sid))
                myconnection.commit()
                myconnection.close()
                print("Record deleted successfully!!")
            except:
                print("Delete record unsuccessful!!");
        elif ch==8:
            cid=input("Enter cid : ")
            try:
                cur.execute("delete from course where cid='%s'"%(cid))
                myconnection.commit()
                myconnection.close()
                print("Record deleted successfully!!")
            except:
                print("Delete record unsuccessful!!");
        elif ch==9:
            iid=input("Enter iid : ")
            try:
                cur.execute("delete from instructor where iid='%s'"%(iid))
                myconnection.commit()
                myconnection.close()
                print("Record deleted successfully!!")
            except:
                print("Delete record unsuccessful!!");
        elif ch==10:
            did=input("Enter did : ")
            try:
                cur.execute("delete from domain where did='%s'"%(did))
                myconnection.commit()
                myconnection.close()
                print("Record deleted successfully!!")
            except:
                print("Delete record unsuccessful!!");
        elif ch==11:
            cur.execute("select * from result")
            print("sid      cid     percentage grade")
            for x in cur:
                for j in x:
                    print(j,end='\t')
                print()
            myconnection.commit()
            myconnection.close()
        elif ch==12:
            cur.execute("select * from progress")
            print("sid     cid     status    deadline")
            for x in cur:
                for j in x:
                    print(j,end='\t')
                print()
            myconnection.commit()
            myconnection.close()
        elif ch==13:
            print("**************ADMIN EXITING************".center(150))
            break
        else:
            print("Invalid choice!!!")
        




###STUDENT MENUE###
def student_menue():
    while True:
        myconnection=mysql.connector.connect(host="localhost",user="root",password="qwerty@123!",database="elearning")
        cur=myconnection.cursor()
        print("""
                                                       _____________________________________
                           
              
                                                                 1.VIEW PROGRESS
                                                                 2.VIEW RESULT
                                                                 3.VIEW COURSE
                                                                 4.EXIT STUDENT

                                                       _____________________________________
                                      """) 
        ch=int(input("Enter your choice : "))
        if ch==1:
            id=input("Enter sid : ")
            cur.execute("select * from progress where sid='%s'"%(id))
            print("sid    cid   status    deadline")
            for x in cur:
                for j in x:
                    print(j,end='\t')
                print()
            myconnection.commit()
            myconnection.close()
        elif ch==2:
            id=input("Enter sid : ")
            cur.execute("select * from result where sid='%s'"%(id))
            c=0
            for x in cur:
                    c+=1
            if c==0:
                print("No records found!!")
            else:
                cur.execute("select * from result where sid='%s'"%(id))
                print("sid    cid  percentage grade")
                for x in cur:
                    for j in x:
                        print(j,end='\t')
                    print()
            myconnection.commit()
            myconnection.close() 
        elif ch==3:
            cur.execute("select title,fees,duration,iname from course,instructor where course.iid=instructor.iid")
            print("Title    fees duration instructor")
            for x in cur:
                for j in x:
                    print(j,end='\t')
                print()
            myconnection.commit()
            myconnection.close()
        elif ch==4:
            print("**************STUDENT EXITING************".center(150))
            break
        else:
            print("Invalid choice!!!")

        







###INSTRUCTOR MENUE###

def instructor_menue():
    while True:
        myconnection=mysql.connector.connect(host="localhost",user="root",password="qwerty@123!",database="elearning")
        cur=myconnection.cursor()
        print("""
                                                      ______________________________________

                                                               1.INSERT TO RESULT
                                                               2.INSERT TO PROGRESS
                                                               3.VIEW PROGRESS
                                                               4.UPDATE PROGRESS
                                                               5.EXIT INSTRUCTOR

                                                      _____________________________________
 
                                           """)
        ch=int(input("Enter your choice :"))
        if ch==1:
            sid=input("Enter sid : ")
            cid=input("Enter cid : ")
            per=input("Enter percentage : ")
            grade=input("Enter grade : ")
            try:
                cur.execute("insert into result values('%s','%s',%s,'%s')"%(sid,cid,per,grade))
                myconnection.commit()
                myconnection.close()
                print("Record inserted successfully!!")
            except:
                print("Insert record unsuccessful!!");
        elif ch==2:
            sid=input("Enter sid : ")
            cid=input("Enter cid : ")
            status=input("Enter status : ")
            dead=input("Enter deadline : ")
            try:
                cur.execute("insert into progress values('%s','%s',%s,'%s')"%(sid,cid,status,dead))
                myconnection.commit()
                myconnection.close()
                print("Record inserted successfully!!")
            except:
                print("Insert record unsuccessful!!");
        elif ch ==3:
            cid=input("Enter cid : ")
            cur.execute("select * from progress where cid='%s'"%(cid))
            print("sid    cid   status    deadline")
            for x in cur:
                for j in x:
                    print(j,end='\t')
                print()
            myconnection.commit()
            myconnection.close()
        elif ch==4 :
            sid=input("Enter sid : ")
            cid=input("Enter cid : ")
            status=input("Enter new status : ")
            try:
                cur.execute("update progress set course_status=%s  where cid='%s' and sid='%s'"%(status,cid,sid))
                myconnection.commit()
                myconnection.close()
                print("Record updated successfully!!")
            except:
                print("Update record unsuccessful!!");
        elif ch==5:
            print("**************INSTRUCTOR EXITING************".center(150))
            break
        else:
            print("Invalid choice!!!")





###MAIN FUNCTION###
print("-----------------------------------------------------------------------".center(150))
print("-----------------------------------------------------------------------".center(150))
print("\n")
print("****************NMAM INSTITUTE OF TECHNOLOGY**********************".center(150))
print("************WELCOME TO COURSE MANAGEMENT SYSTEM ****************".center(150))
print("\n")
print("-----------------------------------------------------------------------".center(150))
print("-----------------------------------------------------------------------".center(150))

while True:
    print()
    print("______________________________________________".center(150))
    print("______________________________________________".center(150))
    print()
    print("Press 1: To login as ADMIN".center(150))
    print("Press 2: To login as STUDENT".center(150))
    print("Press 3:To login as INSTRUCTOR".center(150))
    print("Press 4:To EXIT".center(150))
    print("______________________________________________".center(150))
    print("______________________________________________".center(150))
    print()
    
    ch=int(input("Enter your choice : "))
    if ch==1:
        a = input(" Enter Admin Password : ")
        if a == "admin":
            print("\n\n")
            print("*** WELCOME ADMIN : Here is the Menu ***".center(150))
            admin_menue()
        else:
            print("Invalid password!!! LOGIN UNSUCCESSFUL")
    elif ch==2:
        a=input("Enter your name:")
        print("\n\n")
        s="*** WELCOME "+a+" : Here is the Menu ***"
        print(s.center(150))
        student_menue()
    elif ch==3:
        a=input("Enter your name:")
        print("\n\n")
        s="*** WELCOME "+a+" : Here is the Menu ***"
        print(s.center(150))
        instructor_menue()
    elif ch==4:
        print("---------------------------------------------------".center(150))
        print("****************THANK YOU**************".center(150))
        print("---------------------------------------------------".center(150))
        break
    else:
        print("Invalid choice!!!")
    
    
    
 



