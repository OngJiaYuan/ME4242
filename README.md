# ME4242

Project overview <br /> 

This project is a full stack web application for a cloud based claw machine <br /> 
It is made with Django and to start you need a raspberry pi control board a motor driver to control your motors and a fluid control board which we used to control the claw of the claw machine<br /> 





To start:
python -m pip install django<br /> 
python -m pip install -r requirements.txt<br />
cd .\ME4242_QR\  <br />   
py manage.py runserver<br />

download npm and execute this command
npm install -g jquery


database handling:
read User model from QR folder to find user template<br />
user = User(username="jy", credit=0)<br />