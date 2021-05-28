# Hospital-API
Hospital API is a Covid-19 hospital bed booking REST API (built using Python and MongoDB) that handles CRUD operations for a specific user like get bed list(based on filters like patient critical level, pin-code, hospital, time slot), book bed, reschedule booking and cancel booking.

## Endpoints

Here is the list of endpoints available in the app. Use these endpoints after **api/v1/**. For instance if you want to get a list of beds go to http://127.0.0.1:8000/api/v1/.

| Endpoints                         | HTTP Verb |
|-----------------------------------|-----------|
| /                                 | GET       |
| /:pk                              | GET       |
| /bookings                         | GET       |
| /bookings/create                  | POST      |
| /bookings/:pk                     | GET       |
| users/                            | GET       |
| users/:pk/                        | GET       |
| /rest-auth/registration           | POST      |
| /rest-auth/login                  | POST      |
| /rest-auth/logout                 | GET       |
| /rest-auth/password/reset         | POST      |
| /rest-auth/password/reset/confirm | POST      |

## Installation Instructions

### STEP 1. Activate virtual environment

Create a virtual environment and activate it.

### STEP 2. Install Dependencies

Use the following command in the terminal to install all the dependencies from requirement.txt file.
```
pip install -r requirements.txt
```
### STEP 3. Setup MongoDB Database

Go to MongoDB compass and create a new database. Remember the name of the database to update database settings.

Go to settings.py and change the database settings. Replace the &#39;NAME&#39; field with the name of your database.

```
DATABASES = {

  'default': {

    'ENGINE': 'djongo',

    'NAME': 'database_name',

  }

}
```
### STEP 4. Migrate

Run the following commands in terminal to migrate to database and start the server.
```
python manage.py migrate
python manage.py runserver
```
To learn more about the endpoints go to /docs (http://127.0.0.1:8000/docs/).
