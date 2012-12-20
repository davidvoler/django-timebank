django-timebank
===============
A time banking application using Django, jQuery Mobile. 

Status
-------
The project is in Alpha stage

The idea
---------
Time banking site/application accesible from smartphones and comupter alike

This project can also work as an example of combining django & jquery mobile

Time Banking Solution
---------------------
For more inftrmation about the time banking concept see:
http://en.wikipedia.org/wiki/Time_banking

This application implements time banking in the following way. 
The currency of the bank is time, in minutes granularity. When a user Dafny is providing a service (Private Yoga lesson for example ) that last an hour to Barbara. 60 minutes from barbara accounts is passed to Dafny's Account.
The transaction is happening when Dafny and Barbara set an pointment
 
*Admin define service categories or themse
*Users define service, locations and service category
*Once a service is published, other users can reserve, or ask to recieve this service from the service ownser or service provider.
*Service provider will get informed (view notification section later) about pending reservations, will accept/reject or suggest a new date location
*When a appointment is accepted the actual transaction is taking place. 
*Both users will recive a reminder 24 hours before the appointment
 


Instalation
-----------

Assuming you have python and django(1.4.x) installed. (for instruction on installing python and django please refer to https://docs.djangoproject.com/en/1.4/intro/install/ )

1. Get the files from github

2. Save local_setting_example.py as local_setting.py

3. modify the local settings to agree with your environment, change path, db and secret key

4. run python manage.py syncdb

5. ran python manage.py runserver 

Configuration & Usage
---------------------
Go to admin and add themse



Users & Registration
-------------------
We did not add a registration mechanism to this project.

You may add one of the django user registration mechanimsm or use admin to provision users.

Notification
-------------
The notification mechanism will notify users for:
*new reservations/messages
*reservation accepted 
*Apointment reminder

To add SMS notification we suggest using django_sms package, for using email please configure your email server in setting.py
The notification mecahnism when called will search for new notification and will send them to the user. 
To run the notification we are using django manage.py command, This comand should run using the operating system scedualer (crontab in linux). 



 