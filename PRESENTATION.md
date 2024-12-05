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


# Summary of unit tests
Metrics:   
- 26 unit tests in total
- 90% Code coverage in backend

Example test results:
- factory class tests - they validate whether the correct implementation of an interface is created for the given parameters; they return true if the correct class is created
- database handler tests - they validate whether data is correctly stored in the detabase or correctly read from it; they return true if the data is correctly written/read
- initialization tests - they validate if objects are created with their values properly assigned
- request tests - they validate if the requests call the right methods, with the right parameters, in the right object

Problems encountered during testing:
- difficulties predicting the exact input and output format for many methods
    - we created an API contract to specify the format of 
    information sent in from the frontend
    - tests are designed with easy changing of the expected
    format in mind
- working with 3rd party software and API (such as database systems, and AI providers APIs)
    - we mocked those objects and/or their responses
- difficulty of predicting the exact code strurequest tests - they validate if a request was pcture and the
methods created in the frontend, as they often are dictated by the framework, not the developers choice
    - we moved creating of frontend tests to a later date
    - we are considering using types of test other than unit tests for the frontend