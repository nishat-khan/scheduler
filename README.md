This is a simple scheduling system for a organiser who can get bookings from their attendee/user using a calendar.

It sort of tries to get a form filled by user and updates host's calendar.


Requirements:

Assumptions:
1. Only one attendee per slot
2. Slot is fixed
3. Only one organizer
4. Attendee's availability is not checked through their calendar.

Functional requirements(Must haves):
1. Create an event for the attendee based on Organizer's availability. Ask to fill a form with details
   1. Name
   2. Email
   3. contact
   4. start date time (resolve time zone)
   5. end date time (resolve time zone)
2. Send an invite to attendee's email. Direct to received appointment page.
3. Update the meeting on user's request- modify, cancel.
4. Update organiser's calendar

Working process:
0. Read about a little on system design concepts. Youtube videos had examples, but couldn't really give me the pattern except for some basic relational datatables.
1. Able to set up PyCharm for Flask on Friday, Feb 4, 2022.

Saturday,February 5, 2022:
1. 6 pm: Tried setting up google login for users. Made assumptions. Got home html template.
2. 7 pm:
   1. Outlined functional requirements. 
   2. Is google login necessary? 
   3. Google login would help get user email id and their calendar.
   4. Set up Github key in Pycharm, pushed and updated README.md
   5. Thinking about Google authentication... Would a simple calendar layout work?
3. 11 pm: 
   1. Decided not to complicate things by asking google oAuth login (secondary requirement for now)
4. 11 35 pm:
   1. Think about database tables
   2. User datatable - id, Functional requirements 1 points, booking_status
   3. 
   
   
    
    




References:

1. https://realpython.com/flask-google-login/ - Didnt implement
2. https://www.youtube.com/watch?v=rHZwE1AK1h8  -  Appointment form
