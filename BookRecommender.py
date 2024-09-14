""" Don't forget documentation! """

class Book:
    def __init__(self, genre, author, title):
        self.genre = genre
        self.author = author
        self.title = title

    def __repr__(self):
        return self.title

BOOK_DICT = {
    "mystery" : {
        "ma1" : {
            Book("mystery", "ma1", "ma1b1"),
            Book("mystery", "ma1", "ma1b2"),
            Book("mystery", "ma1", "ma1b2")},
        "ma2" : {
            Book("mystery", "ma2", "ma2b1"),
            Book("mystery", "ma2", "ma2b2"),
            Book("mystery", "ma2", "ma2b2")},
        "ma3" : {
            Book("mystery", "ma3", "ma3b1"),
            Book("mystery", "ma3", "ma3b2"),
            Book("mystery", "ma3", "ma3b2")},
    },
    "sci fi" : {
        "sa1" : {
            Book("sci fi", "sa1", "sa1b1"),
            Book("sci fi", "sa1", "sa1b2"),
            Book("sci fi", "sa1", "sa1b2")},
        "sa2" : {
            Book("sci fi", "sa2", "sa2b1"),
            Book("sci fi", "sa2", "sa2b2"),
            Book("sci fi", "sa2", "sa2b2")},
        "sa3" : {
            Book("sci fi", "sa3", "sa3b1"),
            Book("sci fi", "sa3", "sa3b2"),
            Book("sci fi", "sa3", "sa3b2")},
    },
    "romance" : {
        "ra1" : {
            Book("romance", "ra1", "ra1b1"),
            Book("romance", "ra1", "ra1b2"),
            Book("romance", "ra1", "ra1b2")},
        "ra2" : {
            Book("romance", "ra2", "ra2b1"),
            Book("romance", "ra2", "ra2b2"),
            Book("romance", "ra2", "ra2b2")},
        "ra3" : {
            Book("romance", "ra3", "ra3b1"),
            Book("romance", "ra3", "ra3b2"),
            Book("romance", "ra3", "ra3b2")},
    }
}

GENRE_TRANSITION_MATRIX = {
    "mystery" : {"mystery": .6, "romance": .15, "sci fi" : .25},
    "romance" : {"mystery": .14, "romance": .76, "sci fi" : .1},
    "sci fi" : {"mystery": .2, "romance": .12, "sci fi" : .68}
}

class BookRecomender:
    def __init__(self):
        genres = list(GENRE_TRANSITION_MATRIX.keys())
        genre = input("Enter your favorite genre (options: "+str(genres)+"): ").lower()
        while genre not in genres:
            genre = input("Enter youre favorite genre (options: "+str(genres)+"): ").lower()
        
        authors = list(BOOK_DICT[genre].keys())
        author = input("Enter your favorite "+genre+" author (options: "+str(authors)+"): ").lower()
        while author not in authors:
            author = input("Enter your favorite "+genre+" author (options: "+str(authors)+"): ").lower()
        
        books = list(BOOK_DICT[genre][author])
        titles = []
        for book in books:
            titles.append(book.title)
        title = input("Enter your favorite "+author+" book options: "+str(titles)+"): ").lower()
        while title not in titles:
            title = input("Enter your favorite "+author+" book options: "+str(titles)+"): ").lower()
        
        self.num_recs = input("How many recommendations would you like? (options: 1-20): ")
        while not (self.num_recs.isdigit() and int(self.num_recs) > 0 and int(self.num_recs) <= 20):
            self.num_recs = input("How many recommendations would you like? (options: 1-20): ")
        self.num_recs = int(self.num_recs)

        self.start_book = Book(genre, author, title)
        self.generate_recs()
    
    def generate_recs(self):
        print("generating ", self.num_recs)


def main():
    book_recommender = BookRecomender()

if __name__ == "__main__":
    main()


