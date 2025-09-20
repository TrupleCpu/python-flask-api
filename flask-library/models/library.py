from . import db

class Library(db.Model):
    
    # kung library ang tablename sa mysql mag error
    __tablename__ = 'books_library'

    isbn = db.Column(db.String(13), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author
        }