Chat App Backend (MongoDB Connection)

This project is a simple backend setup for a chat application using Python and MongoDB. It demonstrates how to establish a database connection and verify it.

📁 Project Structure
backend/
│── __pycache__/auth.cpython-310.pyc/database.cpython-310.pyc
│── auth.py
│── database.py
│── test_connection.py
│── .env
│── requirements.txt
│── readme.md
⚙️ Requirements

Make sure you have the following installed:

Python 3.x
MongoDB (local or cloud - MongoDB Atlas)

Install dependencies:

pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the backend folder and add your MongoDB connection string:

MONGO_URI=your_mongodb_connection_string

Example:

MONGO_URI=mongodb://localhost:27017/chatdb
🚀 How to Run

Navigate to the backend folder:

cd backend

Run the connection test:

python test_connection.py
✅ Expected Output

If everything is set up correctly, you will see:

MongoDB connected successfully
📌 Description of Files
auth.py → Handles authentication logic (login/register)
database.py → MongoDB connection setup
test_connection.py → Script to test database connection
.env → Stores environment variables
requirements.txt → Python dependencies
pycache/ → Auto-generated Python bytecode (ignore)
