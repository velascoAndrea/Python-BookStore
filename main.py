from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Velazco2018$@localhost/bookstore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definición de la tabla de libros
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    genre = db.Column(db.String(50))
    price = db.Column(db.Numeric(10, 2))
    quantity = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'genre': self.genre,
            'price': float(self.price),
            'quantity': self.quantity
        }

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    book = Book(
        title=new_book['title'],
        author=new_book['author'],
        isbn=new_book['isbn'],
        genre=new_book['genre'],
        price=new_book['price'],
        quantity=new_book['quantity']
    )
    db.session.add(book)
    db.session.commit()
    return '', 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    updated_book = request.json
    book = Book.query.get_or_404(id)
    book.title = updated_book['title']
    book.author = updated_book['author']
    book.isbn = updated_book['isbn']
    book.genre = updated_book['genre']
    book.price = updated_book['price']
    book.quantity = updated_book['quantity']
    db.session.commit()
    return '', 204

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query')
    books = Book.query.filter(
        (Book.title.like(f'%{query}%')) |
        (Book.author.like(f'%{query}%')) |
        (Book.genre.like(f'%{query}%')) |
        (Book.isbn.like(f'%{query}%'))
    ).all()
    return jsonify([book.to_dict() for book in books])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
