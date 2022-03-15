# Smart-Attendance-Taking
Concept of smart attendance taking using facial recognition 


# How this works? 

The whole product consists of two parts which is the web portal and the local application. The students will register with their details and images which will placed in the azure MySQL database. The local application will perform facial recognition on the student by matching the picture that the student has uploaded with the picture taken of student from his/her webcam. The figure below summarizes how the product will work.


![alt text](https://github.com/aungkhantmoe/Smart-Attendance-Taking/blob/main/concept_photo.png?raw=true)


# Web portal flow

This proportion will describe how the web portal works. The web portal is built using python web framework, Flask. The web portal consists of 3 pages: the home page, registration page and download page. Home page is a simple static web page giving a brief description on the mission and vision of the product. At the registration page students will fill up all the necessary details and upload a picture of themselves. The download page is another static web page which basically provides download links to the local application. 
