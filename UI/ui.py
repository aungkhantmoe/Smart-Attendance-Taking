#imports 
import mysql.connector
from mysql.connector import Error
import os
from tkinter import *
from PIL import Image, ImageTk
import face_recognition
import cv2 
import glob
from time import sleep

#initialisation 

#get absolute path of current directory 
mainpath = os.path.abspath("") 

#connecting to database
connection = mysql.connector.connect (user='XXXX', password='XXXX',
                            host='XXXX', port = 'XXXX', use_pure=True,
                            database='XXXX', ssl_ca='XXXX')




#functions to interact with database 

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


#fetching the image and if the user is registered successfully then will return success, or else an error statement 
def fetch_image(userid, statement): 
    cursor = connection.cursor()
    sql_fetch_blob_query = "SELECT Name,Image,EnroledStatus from studentmaster where UserID = %s"

    cursor.execute(sql_fetch_blob_query, (userid,))
    result = cursor.fetchall()
    if (result != []):
        for row in result:
            if row[2] != '3':
                statement = 'Pending registeration, try again later!'
            else:
                name = row[0]
                photo = row[1]
                image_path = os.path.join(mainpath,'known_pic',('%s.jpg'%name))
                write_file(photo,image_path)
                statement = 'success'
    else:
        statement = 'User does not exist!'
    return (statement)
    cursor.close()


#global variables used for GUI and customizations
gui = Tk()
userid = StringVar()
gui.title('Ariia Facial Recognition')
gui.geometry('700x600') 
main_logo = PhotoImage(file = os.path.join(mainpath, 'logo.png'))
verified = PhotoImage(file = os.path.join(mainpath, 'thankyou.png'))


#functions for displaying GUI & for face recognition
def face_reco():
    tolerance = 0.5
    image_path = glob.glob(os.path.join(mainpath, 'known_pic','*.jpg'))[0]
    known_image = face_recognition.load_image_file(image_path)
    unknown_image = face_recognition.load_image_file("./unknown_pic/photo.jpg")
    
    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)

    if len(unknown_encoding) > 0:
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        result = face_recognition.compare_faces([known_encoding], unknown_encoding,tolerance)
        result = result[0]
    else:
        result = False
    print(result)
    return result
    



# taking picture using webcam 
def take_pic():
    key = cv2.waitKey(2)
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = webcam.read()
            cv2.imshow("Look at the camera! Press 's' to snap a picture!", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename='./unknown_pic/photo.jpg', img=frame)
                webcam.release()
                cv2.destroyAllWindows()
                break

            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break
            
        except(KeyboardInterrupt):
            webcam.release()
            cv2.destroyAllWindows()
            break
        
    sleep(1)
    result = face_reco()
    if result: 
        goodlabel = Label(gui, image = verified).pack()
    else:
        badlabel = Label(gui, text = 'UNVERIFIED! TRY AGAIN!', bg='red')
        badlabel.pack()
        badlabel.after(1500 , lambda: badlabel.destroy())
        
    

    
#second layer (if logged in successfully)
def logged_in():
    usrid = userid.get()
    statement = ''
    fetch_status = fetch_image(usrid,statement)
    output = StringVar()

    if (fetch_status != 'success'):
        warning = Label(gui, text = fetch_status, bg='red')
        warning.pack()
        warning.after(1500 , lambda: warning.destroy())
    else:
        widget_list = gui.pack_slaves()
        for l in widget_list:
            l.destroy()
        success_label = Label(gui, text= 'Login SUCCESSFUL!', font=(None, 40)).pack()
        guide_label = Label(gui, text= 'Click the button below to perform facial recognition').pack()
        button = Button(gui, text= 'facial_recognition', command = lambda: take_pic(), fg = 'red', activeforeground = 'blue')
        button.pack()




#login page 
def main_page():
    logo = Label(gui, image = main_logo).pack() #to display logo

    user_label = Label(gui, text = 'UserID:').pack()
    user_field = Entry(gui, textvariable = userid).pack()

    button = Button(gui, text = 'Login', command = logged_in, fg = 'red', activeforeground = 'blue').pack()

main_page()

gui.mainloop()


