# Library Management System Backend

This is the backend component of the Library Management System, built with Flask and SQLAlchemy.

## Setup and Installation

1. Ensure you have Python 3.7+ installed on your system.

2. Clone the repository and navigate to the backend directory:
   ```bash
   cd backend
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. With the virtual environment activated, start the Flask server:
   ```bash
   flask run
   ```

2. The API will be available at `http://localhost:5000`.

## API Endpoints

- `GET /api/books`: Fetch all books
- `POST /api/books`: Add a new book
- `PUT /api/books/<id>`: Update a book
- `DELETE /api/books/<id>`: Delete a book
- `GET /api/books/search`: Search and filter books

## Database

The application uses SQLite as the database. The database file (`library.db`) will be created automatically when you run the application for the first time.

## Development

- The main application logic is in `app.py`
- Database models are defined in `models.py`
- To add new endpoints, update `app.py` and create corresponding functions

## Troubleshooting

If you encounter any issues:
1. Ensure your virtual environment is activated
2. Verify that all dependencies are installed correctly
3. Check the console output for any error messages

For any additional questions or support, please open an issue in the main repository.