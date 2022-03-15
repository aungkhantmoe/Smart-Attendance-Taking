# Smart-Attendance-Taking
Concept of smart attendance taking using facial recognition 


# How this works? 

The whole product consists of two parts which is the web portal and the local application. The students will register with their details and images which will placed in the azure MySQL database. The local application will perform facial recognition on the student by matching the picture that the student has uploaded with the picture taken of student from his/her webcam. The figure below summarizes how the product will work.


![alt text](https://github.com/aungkhantmoe/Smart-Attendance-Taking/blob/main/documentation_pics/concept_photo.png?raw=true)


# Web portal flow

This proportion will describe how the web portal works. The web portal is built using python web framework, Flask. The web portal consists of 3 pages: the home page, registration page and download page. Home page is a simple static web page giving a brief description on the mission and vision of the product. At the registration page students will fill up all the necessary details and upload a picture of themselves. The download page is another static web page which basically provides download links to the local application. 

# Local Application

The local application will tell the students if their registration has been approved. If it is approved, they will be able to perform facial recognition it confirms their identity. However, the interaction with a sort of backend to systematically respond if their identity is verified has yet to be set up.

# Security

As far as security goes, on the web portal the input fields do not accept special characters and upload functionality only allow two file extensions: jpg and png. Also, the download page is only accessible if the refer URL is from the registration page. The product is currently using RAW SQL queries to interact with the database. Use of stored query causes conflict with the mysql connector module which is used to interact with the database in python

# Future development work 

A web page which can allow lecturers to change the registration status after checking the images of the student will be an essential add-on to the product. 

A better database design with columns names with makes more sense can be done. In the current database, columns such as DataTimeDecision can be redundant as it does not make much sense without another complementary column which tracks the confirmation of verification. 

A better security by making use of prepared SQL queries to interact with the database. 

Interaction with the backend on side of the local application to handle the process after verification. 

Packing the python script into a system application 


# Running through environment

  
  ![alt text](https://github.com/aungkhantmoe/Smart-Attendance-Taking/blob/main/documentation_pics/activate.png?raw=true)
  
  ![alt text](https://github.com/aungkhantmoe/Smart-Attendance-Taking/blob/main/documentation_pics/install.png?raw=true)

