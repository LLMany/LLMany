# Key elements of class diagram
- RequestHandler - takes care of processing the requests coming in from frontend, and creates appropriate request class
- DatabaseHandler - handles all connections to the database
- ModelHandlerFactory - creates models handlers for models created by the user

# Desing patterns
Design patterns used in the app:
- bridge - joins the react frontend with the python backend
- Model-View-ViewModel - used to create the frontend
- Factory - creates the appropriate request class,
for the requests sent from frontend
- Command - handles all the information about requests sent to backend
