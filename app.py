from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, Book
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db.init_app(app)

# Add this function to create sample books
def create_sample_books():
    sample_books = [
        {
            "title": "Pukirat",
            "author": "Jesus Mocho",
            "genre": "Fiction",
            "publication_date": datetime(1960, 7, 11),
            "available": True
        },
        {
            "title": "Python Programming",
            "author": "Papa John",
            "genre": "Computer Science",
            "publication_date": datetime(1949, 6, 8),
            "available": False
        },
        {
            "title": "Data Science for Dummy",
            "author": "Satan",
            "genre": "Computer Science",
            "publication_date": datetime(1813, 1, 28),
            "available": True
        }
    ]

    for book_data in sample_books:
        book = Book(**book_data)
        db.session.add(book)
    
    db.session.commit()

@app.route('/api/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(
        title=data['title'],
        author=data['author'],
        genre=data['genre'],
        publication_date=datetime.fromisoformat(data['publicationDate']),
        available=data['available']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.json
    book.title = data['title']
    book.author = data['author']
    book.genre = data['genre']
    book.publication_date = datetime.fromisoformat(data['publicationDate'])
    book.available = data['available']
    db.session.commit()
    return jsonify(book.to_dict())

@app.route('/api/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '')
    genre = request.args.get('genre', '')
    availability = request.args.get('availability', '')

    books = Book.query

    if query:
        books = books.filter((Book.title.ilike(f'%{query}%')) | (Book.author.ilike(f'%{query}%')))
    
    if genre and genre != 'All':
        books = books.filter(Book.genre == genre)
    
    if availability == 'Available':
        books = books.filter(Book.available == True)
    elif availability == 'Unavailable':
        books = books.filter(Book.available == False)

    return jsonify([book.to_dict() for book in books.all()])

@app.route('/')
def home():
    return "Welcome to the Library API!"

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Check if there are any books in the database
        if Book.query.count() == 0:
            create_sample_books()
    app.run(debug=True)