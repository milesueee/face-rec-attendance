############################################# IMPORTING ################################################
import csv
import datetime
import time
import tkinter as tk
import tkinter.simpledialog as tsd
from tkinter import messagebox as mess
from tkinter import ttk
import cv2
import numpy as np
import os
import pandas as pd
from PIL import Image
import sys


#                                        FUNCTIONS

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)



#

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)


###################################################################################

def contact():
    mess._show(title='Contact us', message="Please contact me on : 'mikoybailon250@gmail.com' ")


###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()


###################################################################################

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = (old.get())
    newp = (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if (newp == nnewp):
            txf = open("TrainingImageLabel\psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()


###################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(True, True)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master, text='    Enter Old Password', bg='white', font=('SF Pro', 12, ' bold '))
    lbl4.place(x=10, y=10)
    global old
    old = tk.Entry(master, width=25, fg="black", relief='solid', font=('SF Pro', 12, ' bold '), show='*')
    old.place(x=180, y=10)
    lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('SF Pro', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black", relief='solid', font=('SF Pro', 12, ' bold '), show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('SF Pro', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid', font=('SF Pro', 12, ' bold '), show='*')
    nnew.place(x=180, y=80)
    cancel = tk.Button(master, text="Cancel", command=master.destroy, fg="black", bg="red", height=1, width=25,
                       activebackground="white", font=('SF Pro', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height=1, width=25,
                      activebackground="white", font=('SF Pro', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()


#####################################################################################

def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')


######################################################################################

def clear():
    txt.delete(0, 'end')
    res = "Take Images  >>>  Save Profile"
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "Take Images  >>>  Save Profile"
    message1.configure(text=res)


#######################################################################################

def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
    Id = (txt.get())
    name = (txt2.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        #                     CAMERA SETTINGS FOR FACE AND PROFILE REGISTRATION

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('Taking Images', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is more than 20
            elif sampleNum > 50:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Taken for ID : " + Id
        row = [serial, '', Id, '', name]
        with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            message.configure(text=res)


#

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='No Registrations', message='Please Register a student first')
        return
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Student profile saved successfully"
    message1.configure(text=res)


#
def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids


###########################################################################################

def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    for k in tv.get_children():
        tv.delete(k)
    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
    if exists3:
        recognizer.read("TrainingImageLabel\Trainner.yml")
    else:
        mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists1:
        df = pd.read_csv("StudentDetails\StudentDetails.csv")
    else:
        mess._show(title='Details Missing', message='Students details are missing, please check!')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(aa)
                bb = bb[2:-2]
                attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]
            else:
                Id = 'Unknown'
                bb = str(Id)
            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('Taking Attendance ( PRESS ANY KEY TO CONTINUE )', im)
        key = cv2.waitKey(1) & 0xFF
        """use == instead of != to record the entry immediately"""
        if key != 255:
            break

    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
    if exists:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(attendance)
        csvFile1.close()
    else:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(col_names)
            writer.writerow(attendance)
        csvFile1.close()
    with open("Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
    csvFile1.close()
    cam.release()
    cv2.destroyAllWindows()


##              global variables for time and date

global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year = date.split("-")

mont = {'01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
        }

######################################## GUI FRONT-END ###########################################

window = tk.Tk()
window.geometry("1920x720")
window.resizable(True, True)
window.title("Attendance System For GAS SY 2022 - 2023 Culminating Activity")
window.configure(background='#262523')

#               main frame for attendance and registration


frame1 = tk.Frame(window, bg="#5DADE2")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#5DADE2")
frame2.place(relx=0.51, rely=0.17, relwidth=0.39, relheight=0.80)

message3 = tk.Label(window, text="Attendance System for Culminating Activity", fg="white", bg="#262523", width=80,
                    height=1, font=('Helvetica', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.34, rely=0.09, relwidth=0.18, relheight=0.07)

datef = tk.Label(frame3, text=day + "  -  " + mont[month] + "  -  " + year, fg="orange", bg="#262523", width=10,
                 height=1, font=('SF Pro', 22, ' normal '))
datef.pack(fill='both', expand=1)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.50, rely=0.09, relwidth=0.09, relheight=0.07)

clock = tk.Label(frame4, fg="orange", bg="#262523", width=70, height=1, font=('SF Pro', 22, ' normal '))
clock.pack(fill='both', expand=1)
tick()

head2 = tk.Label(frame2, text="                       For New Registrations                       ", fg="black",
                 bg="#3ece48", font=('Malgun Gothic', 17, ' normal '), width=60)
head2.grid(row=0, column=0)

head1 = tk.Label(frame1, text="                       For Already Registered                       ", fg="black",
                 bg="#3ece48", font=('Malgun Gothic', 17, ' normal '), width=60)
head1.place(x=-25, y=0)

lbl = tk.Label(frame2, text="Enter ID", width=50, height=1, fg="black", bg="#5DADE2",
               font=('Bahnschrift', 15, ' normal '))
lbl.place(x=100, y=60)

txt = tk.Entry(frame2, width=50, fg="black", font=('Arial', 13, ' normal '))
txt.place(x=145, y=90)

lbl2 = tk.Label(frame2, text="Enter Name", width=50, fg="black", bg="#5DADE2", font=('Bahnschrift', 15, ' normal '))
lbl2.place(x=100, y=170)

txt2 = tk.Entry(frame2, width=50, fg="black", font=('Arial', 13, ' normal '))
txt2.place(x=145, y=200)

message1 = tk.Label(frame2, text="Take Images  >>>  Save Profile", bg="#5DADE2", fg="black", width=68, height=1,
                    activebackground="yellow", font=('Bahnschrift', 13, ' bold '))
message1.place(x=70, y=280)

message = tk.Label(frame2, text="DCFVREG", bg="#5DADE2", fg="black", width=39, height=1, activebackground="red",
                   font=('times', 16, ' bold '))
message.place(x=7, y=450)
lbl3 = tk.Label(frame1, text="Attendance", width=20, fg="black", bg="#5DADE2", height=1,
                font=('Bahnschrift', 15, ' normal '))
lbl3.place(x=240, y=115)

res=0
exists = os.path.isfile("StudentDetails\StudentDetails.csv")
if exists:
    with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(font=('Google Sans', 17, 'normal'), text="Total Students Registered :  " + str(res))
message.place(x=130, y=500)


##################### MENUBAR #################################

menubar = tk.Menu(window, relief='ridge')

################## TREEVIEW ATTENDANCE TABLE ####################

tv = ttk.Treeview(frame1, height=13, columns=('name', 'date', 'time'))
tv.column('#0', width=50)
tv.column('name', width=220, anchor="center")
tv.column('date', width=80, anchor="center")
tv.column('time', width=80, anchor="center")
tv.grid(row=2, column=0, padx=(125, 0), pady=(150, 0), columnspan=4)
tv.heading('#0', text='ID')
tv.heading('name', text='NAME')
tv.heading('date', text='DATE')
tv.heading('time', text='TIME')

###################### SCROLLBAR ################################

scroll = ttk.Scrollbar(frame1, orient='vertical', command=tv.yview)
scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
tv.configure(yscrollcommand=scroll.set)


###################### BUTTONS ##################################
def restart_program():
    python = sys.executable
    os.execl(sys.executable, sys.executable, python, python, *sys.argv)


clearButton = tk.Button(frame2, text="Clear", command=clear, fg="white", bg="#F17054", width=11,
                        activebackground="white", borderwidth="0", font=('Google Sans', 10, ' normal '))
clearButton.place(x=335, y=115)

clearButton2 = tk.Button(frame2, text="Clear", command=clear2, fg="white", bg="#F17054", width=11,
                         activebackground="white", borderwidth="0", font=('Google Sans', 10, ' normal '))
clearButton2.place(x=335, y=225)

takeImg = tk.Button(frame2, text="Take Images", command=TakeImages, fg="black", bg="white", width=25, height=1,
                    activebackground="green", borderwidth="0", font=('Google Sans', 15, ' normal '))
takeImg.place(x=230, y=340)

trainImg = tk.Button(frame2, text="Save Profile", command=psw, fg="black", bg="white", width=25, height=1,
                     activebackground="green", borderwidth="0", font=('Google Sans', 15, ' normal '))
trainImg.place(x=230, y=420)

trackImg = tk.Button(frame1, text="Take Attendance", command=TrackImages, fg="black", bg="yellow", width=35, height=1,
                     activebackground="white", borderwidth="0", font=('Google Sans', 15, ' normal '))
trackImg.place(x=140, y=50)

quitWindow = tk.Button(frame1, text="Quit", command=window.destroy, fg="black", bg="#F46D2E", width=15, height=1,
                       activebackground="white", borderwidth="0", font=('Google Sans', 17, ' normal '))
quitWindow.place(x=140, y=500)

restartButton = tk.Button(frame1, text='Restart', command=restart_program, fg="black", bg="#7DD9DC", width=15, height=1,
                          activebackground="white", borderwidth="0", font=('Google Sans', 17, ' normal '))
restartButton.place(x=360, y=500)

#                END

window.configure(menu=menubar)
window.mainloop()
