## Overview  

In this project, I have implemented an API to manage app information (name, version, description) using a SQLite database. The API is built with **Flask** and **Flask-SQLAlchemy**, and the database is integrated to store, retrieve, and delete app data.  

## Features  

- **Add an app**: Allows adding new app information (name, version, description) to the database.  
- **Retrieve an app**: Fetch details of an app by its unique ID.  
- **Delete an app**: Delete an app record by its unique ID.  
- **SQLite Database**: Stores the app information in a SQLite database.  

## Requirements  

- **Flask**: A lightweight web framework for Python.  
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy, an ORM for databases.  

To install the necessary dependencies, run:  

```bash  
pip install -r requirements.txt  
```  

## Database Schema  

The database schema is created automatically based on the model defined in the `app.py` file. It contains a single table, `app`, with the following columns:  

- `id` (integer, primary key)  
- `app_name` (string)  
- `version` (string)  
- `description` (string)  

The `id` field is automatically generated for each app and is the primary key.  

## API Endpoints  

### 1. Add an app  

- **URL**: `/add-app`  
- **Method**: `POST`  
- **Request Body**:  
    ```json  
    [
        {
            "app_name": "App 1",
            "version": "1.0",
            "description": "First app"
        },
        {
            "app_name": "App 2",
            "version": "1.0",
            "description": "Second app"
        }
    ]
    ```  
- **Response**:  
    ```json  
    [
        {  
            "app": {
                "app_name": "App 1",
                "version": "1.0",
                "description": "First app"
            },
            "id": 1
        },
        {
            "app": {
                "app_name": "App 2",
                "version": "1.0",
                "description": "Second app"
            },
            "id": 2
        }
    ]
    ```  

### 2. Get an app by ID  

- **URL**: `/get-app/<int:app_id>`  
- **Method**: `GET`  
- **Response**:  
    ```json  
    {
        "app": {
            "app_name": "App 1",
            "version": "1.0",
            "description": "First app"
        },
        "id": 1
    }
    ```  

### 3. Delete an app by ID  

- **URL**: `/delete-app/<int:app_id>`  
- **Method**: `DELETE`  
- **Response**: `204 No Content`  

## Sample Data for Testing  

You can use **Postman** or **cURL** to test the following endpoints:  

1. **Add apps**: Use the `POST /add-app` endpoint with the following sample data:  
    ```json  
    [
        {
            "app_name": "App 1",
            "version": "1.0",
            "description": "First app"
        },
        {
            "app_name": "App 2",
            "version": "1.0",
            "description": "Second app"
        }
    ]
    ```  

2. **Get app by ID**: Use the `GET /get-app/<app_id>` endpoint, replacing `<app_id>` with the ID of the app you want to retrieve.  

3. **Delete app by ID**: Use the `DELETE /delete-app/<app_id>` endpoint, replacing `<app_id>` with the ID of the app you want to delete.  

## Testing the API  

You can test the API using:  

1. **Postman**:  
   - Import the endpoints manually or use a collection file.  
   - Set the request body (for `POST` requests) in JSON format.  
   - Send the requests and view responses directly in Postman.  

2. **cURL**:  
   - Add apps:  
     ```bash  
     curl -X POST -H "Content-Type: application/json" -d '[{"app_name": "App 1", "version": "1.0", "description": "First app"}]' http://127.0.0.1:5000/add-app
     ```  
   - Get an app by ID:  
     ```bash  
     curl -X GET http://127.0.0.1:5000/get-app/1
     ```  
   - Delete an app by ID:  
     ```bash  
     curl -X DELETE http://127.0.0.1:5000/delete-app/1
     ```  

## Running the Application  

1. Download the project.  
2. Install dependencies:  
    ```bash  
    pip install -r requirements.txt  
    ```  
3. Run the application:  
    ```bash  
    python app.py  
    ```  

The application will be available at `http://127.0.0.1:5000/`.  

## Deliverables  

- **Database schema**: Defined through the `App` model in `app.py`.  
- **Sample data**: Example JSON data for testing the API.  
