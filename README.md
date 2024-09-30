# KlimraTask
 Assigment for Klimra
This is a simple fullstack web application that allows users to insert and retrieve records using a Flask backend and a React frontend. The Flask API provides two endpoints for inserting and fetching records, while the React app provides an interface for interacting with the backend.

# Features
Insert a Record: Users can input a record (e.g., a name or message) and submit it to the Flask backend.
Fetch Last Record: Users can retrieve and display the last record inserted into the system.

# Prerequisites:
Before running the application, ensure you have the following installed:
->Python 3.x
->Node.js (includes npm)

# Project structure:
backend--> App.py
frontend -->src--->App.js
Frontend dependencies-->package.json


# Backend (Flask) Setup:

->Navigate to the backend folder

->Installed the required Python packages:

 pip install flask, pip install flask-cors

->Start the Flask server:
 python app.py

 The Flask server will run on http://127.0.0.1:5000.



# Frontend (React) Setup:

->Navigate to the frontend folder

->Install the required npm dependencies:npm install

->Start the React development server:npm start

The React frontend will be available at http://localhost:3000.


# API Endpoints:

POST /record: Inserts a new record into the system.
Response: A success message indicating that the record was inserted.

GET /record: Retrieves the last inserted record.
Response: A JSON object containing the last inserted record:


# Running the Application
Start the Backend: Make sure the Flask backend is running by executing: python app.py
Start the Frontend: Open a new terminal, navigate to the frontend folder, and
run:npm start

Interact with the App:
Open your browser and go to http://localhost:3000/.

# You will see an interface with two sections:
->Insert a Record: Type a record and click "Add Record".
->Fetch Last Record: Click "Fetch Record" to retrieve the last inserted record.


Note: If you get any errors like below try below instructions:
ModuleNotFoundError: Ensure you've installed Flask using pip install flask.
CORS errors: Make sure flask-cors is installed and enabled in the Flask app.
React not working: Check that Node.js and npm are properly installed, and ensure you're running the React server with npm start.
