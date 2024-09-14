""" Don't forget documentation! """

import random

class Book:
    def __init__(self, genre, author, title):
        self.genre = genre
        self.author = author
        self.title = title

    def __repr__(self):
        return self.title
    
    def __str__(self):
        return self.title

BOOK_DICT = {
    "mystery" : {
        "ma1" : {
            "ma1b1" : Book("mystery", "ma1", "ma1b1"),
            "ma1b2" : Book("mystery", "ma1", "ma1b2"),
            "ma1b3" : Book("mystery", "ma1", "ma1b3")},
        "ma2" : {
            "ma2b1" : Book("mystery", "ma2", "ma2b1"),
            "ma2b2" : Book("mystery", "ma2", "ma2b2"),
            "ma2b3" : Book("mystery", "ma2", "ma2b3")},
        "ma3" : {
            "ma3b1" : Book("mystery", "ma3", "ma3b1"),
            "ma3b2" : Book("mystery", "ma3", "ma3b2"),
            "ma3b3" : Book("mystery", "ma3", "ma3b3")},
    },
    "sci fi" : {
        "sa1" : {
            "sa1b1" : Book("sci fi", "sa1", "sa1b1"),
            "sa1b2" : Book("sci fi", "sa1", "sa1b2"),
            "sa1b3" : Book("sci fi", "sa1", "sa1b3")},
        "sa2" : {
            "sa2b1" : Book("sci fi", "sa2", "sa2b1"),
            "sa2b2" : Book("sci fi", "sa2", "sa2b2"),
            "sa2b3" : Book("sci fi", "sa2", "sa2b3")},
        "sa3" : {
            "sa3b1" : Book("sci fi", "sa3", "sa3b1"),
            "sa3b2" : Book("sci fi", "sa3", "sa3b2"),
            "sa3b3" : Book("sci fi", "sa3", "sa3b3")},
    },
    "romance" : {
        "ra1" : {
            "ra1b1" : Book("romance", "ra1", "ra1b1"),
            "ra1b2" : Book("romance", "ra1", "ra1b2"),
            "ra1b3" : Book("romance", "ra1", "ra1b3")},
        "ra2" : {
            "ra2b1" : Book("romance", "ra2", "ra2b1"),
            "ra2b2" : Book("romance", "ra2", "ra2b2"),
            "ra2b3" : Book("romance", "ra2", "ra2b3")},
        "ra3" : {
            "ra3b1" : Book("romance", "ra3", "ra3b1"),
            "ra3b2": Book("romance", "ra3", "ra3b2"),
            "ra3b3" : Book("romance", "ra3", "ra3b3")},
    }
}

GENRE_TRANSITION_MATRIX = {
    "mystery" : {"mystery": .6, "romance": .15, "sci fi" : .25},
    "romance" : {"mystery": .14, "romance": .76, "sci fi" : .1},
    "sci fi" : {"mystery": .2, "romance": .12, "sci fi" : .68}
}

class BookRecomender:
    def __init__(self):
        self.genres = list(GENRE_TRANSITION_MATRIX.keys())
        genre = input("Enter your favorite genre (options: "+str(self.genres)+"): ").lower()
        while genre not in self.genres:
            genre = input("Enter your favorite genre (options: "+str(self.genres)+"): ").lower()
        
        authors = list(BOOK_DICT[genre].keys())
        author = input("Enter your favorite "+genre+" author (options: "+str(authors)+"): ").lower()
        while author not in authors:
            author = input("Enter your favorite "+genre+" author (options: "+str(authors)+"): ").lower()
        
        titles = list(BOOK_DICT[genre][author].keys())
        title = input("Enter your favorite "+author+" book (options: "+str(titles)+"): ").lower()
        while title not in titles:
            title = input("Enter your favorite "+author+" book (options: "+str(titles)+"): ").lower()
        
        self.num_recs = input("How many recommendations would you like? (options: 1-26): ")
        while not (self.num_recs.isdigit() and int(self.num_recs) > 0 and int(self.num_recs) <= 26):
            self.num_recs = input("How many recommendations would you like? (options: 1-20): ")
        self.num_recs = int(self.num_recs)

        self.start_book = BOOK_DICT[genre][author][title]
        print(self.start_book)
        self.create_bookmark(self.generate_recs())
    
    def generate_recs(self):
        
        book_recs = [self.start_book] # to ensure start is not recommended
        current_book = self.start_book

        for i in range(self.num_recs):
            next_book = self.get_next_book(current_book)
            while (next_book in book_recs):
                next_book = self.get_next_book(current_book)
            book_recs.append(next_book)
            current_book = next_book
        
        book_recs.remove(self.start_book)
        
        return book_recs
    
    def get_next_book(self, current_book):

        next_genre = random.choices(self.genres, GENRE_TRANSITION_MATRIX[current_book.genre].values())[0]

        author_mtx = dict()
        title_mtx = dict()
        
        if next_genre == current_book.genre:
            for author in list(BOOK_DICT[next_genre].keys()):
                author_mtx[author] = .5/(len(list(BOOK_DICT[next_genre]))-1)
            author_mtx[current_book.author] = .5
        else:
            for author in list(BOOK_DICT[next_genre].keys()):
                author_mtx[author] = 1/(len(list(BOOK_DICT[next_genre])))
        print("author mtx", author_mtx)
            
        next_author = random.choices(list(author_mtx.keys()), list(author_mtx.values()))[0]

        print("books", list(BOOK_DICT[next_genre][next_author].keys()))
        
        if next_author == current_book.author:
            for book_title in list(BOOK_DICT[next_genre][next_author].keys()):
                title_mtx[book_title] = 1/(len(list(BOOK_DICT[next_genre][next_author]))-1)
            title_mtx[current_book.title] = 0
        else:
            for book_title in list(BOOK_DICT[next_genre][next_author].keys()):
                title_mtx[book_title] = 1/(len(list(BOOK_DICT[next_genre][next_author])))
        print("title mtx", title_mtx)

        next_title = random.choices(list(title_mtx.keys()), list(title_mtx.values()))[0]
        
        print(next_genre, next_author, next_title)
        return BOOK_DICT[next_genre][next_author][next_title]
    
    def create_bookmark(self, book_recs):
        print(book_recs)



def main():
    book_recommender = BookRecomender()

if __name__ == "__main__":
    main()


