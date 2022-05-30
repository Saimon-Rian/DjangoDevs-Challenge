Project objectives
-

This project was made as my participation in the Django-Devs-001 challenge. This project is an API made in Django with 
rest architecture in integration with Postman. Also used to test my API skills and show my knowledge. 
I will continue to develop this project with new technologies and acquired knowledge.

What needs to be installed
-

- Docker
- Docker-compose
- Makefile


# Makefile commands:

To install all the requirements and make migrations run:
-

    make build

To build docker-compose:
-

    make up

To take down docker-compose:
-

    make down

To run the tests:
-

    make tests

To see the coverage of your application: 
-
- The coverage percentage also appears on your terminal.

- For a more detailed report, go to "htmlconv" folder and look for index.html.


    make coverage

To set the ipdb trace:
-
- Remember to put the ipdb in your code before doing the "make attach".


    make attach

To see actions taken on URLs:
-

    make logs


Source:
-
https://github.com/JungleDevs/django-challenge-001
