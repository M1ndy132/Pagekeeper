class Book():
    def __init__(self, name, author, genre, rating, status, reading_progress) -> None:
        self.book_name = name
        self.author = author
        self.genre = genre
        self.rating = rating
        self.status = status
        self.reading_progress = reading_progress
        self.quotes = []
        self.bookmarks = []
        self.reviews = []

    def __str__(self) -> str:
        return f"Title: {self.book_name} by {self.author}"

class Quote():
    def __init__(self, quote_text, book, colour, qnote = None, said_by = "Unknown") -> None:
        self.text = quote_text
        self.book = book
        self.note = qnote
        self.said_by = said_by
        self.colour = colour

    def __str__(self) -> str:
        return f"{self.text} - {self.said_by} \n Thoughts:\n{self.note}"

class Note():
    def __init__(self, book, note_text, quote = None) -> None:
        self.book = book
        self.quote = quote
        self.text = note_text