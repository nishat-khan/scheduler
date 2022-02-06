This is a simple scheduling system for a organiser who can get bookings from their attendee/user using a calendar.

It sort of tries to build a Calendly like system.


Requirements:

Assumptions:
1. Only one attendee per slot
2. Slot is fixed
3. Only one organizer
4. Attendee's availability is not checked through their calendar.

Functional requirements(Must haves):
1. Create an event for the attendee based on Organizer's availability.
2. Send an invite to attendee's email.
3. Update the meeting - modify, cancel.

Working process:
0. Read about a little on system design concepts. Youtube videos had examples, but couldn't really give me the pattern except for some basic relational datatables.
1. Able to set up PyCharm for Flask on Friday, Feb 4, 2022.
2. Saturday,February 5, 2022:
   1. 6 pm: Tried setting up google login for users. Made assumptions. Got home html template.
   2. 7 pm:
      a. Outlined functional requirements. 
      b. Is google login necessary? 
      c. Google login would help get user email id and their calendar.
      d. Set up github key in Pycharm
    
    




References:

https://realpython.com/flask-google-login/