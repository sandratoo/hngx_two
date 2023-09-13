# REST API
 A simple REST API capable of CRUD operations on a "person" resource. Built using Flask, Sqlalchemy ORM and SQLite database.
## API Setup and Usage
### Prerequisites
Before setting up and using the API, make sure you have the following prerequisites installed:
- Flask
- SQLAlchemy
### Installation
1. Clone the GitHub repository to your local machine:
>```
> gh repo clone sandratoo/hngx_two

2. Create and activate a virtual environment:
> ```
> python -m venv venv
> source venv/bin/activate

3. Install the required dependencies:
> ```
> pip install -r requirements.txt
### Run the application
Export the app then start app
> ```
> export FLASK_APP=<application_name>
> flask run
The server will start running on the specified port (default: 5000).
## API ENDPOINTS
- GET /api/: Retrieves all users from the database.
- GET /api/id Retrieves a specific user by their ID.
- POST /api/: Creates a new user. Requires a JSON body with a name property.
- PUT /api/id Updates a user by their ID. Requires a JSON body with a name property.
- DELETE /api/id Deletes a user by their ID.
  
For detailed documentation on the API, please refer to the **documentation.md** file
## TESTING
Testing the API can be done using tools like Postman. Test each CRUD operation:
- Adding a new person (e.g., "example Name").
- Fetching details of a person.
- Modifying the details of an existing person.
- Removing a person.
