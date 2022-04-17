Feature: As a Vaccine Appointment User I want to Schedule multiple new appointments


Scenario Outline: Scheduling multiple new appointments
Given with the <appointmentId> is starting at <startTime> and <endTime> is entered
When the appointment is scheduled 
Then Success is reported 
Examples:
|appointmentId          | startTime     | endTime |
|1						| "9:30" 		| "10:30" |
|2						| "10:30"		| "11:30" |
|3						| "12:30" 	    | "13:30" |