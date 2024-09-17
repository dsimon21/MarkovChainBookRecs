""" BookRecommender.py

This file contains the Book class and BookRecommender classes which provide
functionality to create bookmarks containing book recomendations based on user
input using a Markov Chain.

Danielle Simon
"""

import random
import matplotlib.pyplot as plt
from PIL import Image

class Book:
    """ This class represents a book object with string attributes genre, author, and title """
    def __init__(self, genre, author, title):
        self.genre = genre
        self.author = author
        self.title = title

    def __repr__(self):
        return self.title
    
    def __str__(self):
        return self.title

BOOK_DICT = {
    "Mystery" : {
        "Karen Mcmanus" : {
            "One Of Us Is Lying" : Book("Mystery", "Karen Mcmanus", "One Of Us Is Lying"),
            "Two Can Keep A Secret" : Book("Mystery", "Karen Mcmanus", "Two Can Keep A Secret"),
            "You'Ll Be The Death Of Me" : Book("Mystery", "Karen Mcmanus", "You'Ll Be The Death Of Me")},
        "Holly Jackson" : {
            "A Good Girl'S Guide To Murder" : Book("Mystery", "Holly Jackson", "A Good Girl'S Guide To Murder"),
            "Five Survive" : Book("Mystery", "Holly Jackson", "Five Survive"),
            "The Reappearance Of Rachel Price" : Book("Mystery", "Holly Jackson", "The Reappearance Of Rachel Price")},
        "Jennifer Lynn Barnes" : {
            "The Inheritance Games" : Book("Mystery", "Jennifer Lynn Barnes", "The Inheritance Games"),
            "The Naturals" : Book("Mystery", "Jennifer Lynn Barnes", "The Naturals"),
            "Raised By Wolves" : Book("Mystery", "Jennifer Lynn Barnes", "Raised By Wolves")},
    },
    "Fantasy" : {
        "Sarah J Mass" : {
            "Throne Of Glass" : Book("Fantasy", "Sarah J Mass", "Throne Of Glass"),
            "A Court Of Thorns And Roses" : Book("Fantasy", "Sarah J Mass", "A Court Of Thorns And Roses"),
            "Crescent City" : Book("Fantasy", "Sarah J Mass", "Crescent City")},
        "Rick Riordan" : {
            "Percy Jackson And The Olympians" : Book("Fantasy", "Rick Riordan", "Percy Jackson And The Olympians"),
            "The Kane Chronicles" : Book("Fantasy", "Rick Riordan", "The Kane Chronicles"),
            "The Heroes Of Olympus" : Book("Fantasy", "Rick Riordan", "The Heroes Of Olympus")},
        "Veronica Roth" : {
            "Divergent" : Book("Fantasy", "Veronica Roth", "Divergent"),
            "Chosen Ones" : Book("Fantasy", "Veronica Roth", "Chosen Ones"),
            "When Among Crows" : Book("Fantasy", "Veronica Roth", "When Among Crows")},
    },
    "Romance" : {
        "Sarah Dessen" : {
            "Along For The Ride" : Book("Romance", "Sarah Dessen", "Along For The Ride"),
            "The Truth About Forever" : Book("Romance", "Sarah Dessen", "The Truth About Forever"),
            "Someone Like You" : Book("Romance", "Sarah Dessen", "Someone Like You")},
        "Emily Henry" : {
            "Beach Read" : Book("Romance", "Emily Henry", "Beach Read"),
            "Happy Place" : Book("Romance", "Emily Henry", "Happy Place"),
            "Book Lovers" : Book("Romance", "Emily Henry", "Book Lovers")},
        "Taylor Jenkins Reed" : {
            "Maybe In Another Life" : Book("Romance", "Taylor Jenkins Reed", "Maybe In Another Life"),
            "One True Loves": Book("Romance", "Taylor Jenkins Reed", "One True Loves"),
            "Forever Interrupted" : Book("Romance", "Taylor Jenkins Reed", "Forever Interrupted")},
    }
}

GENRE_TRANSITION_MATRIX = {
    "Mystery" : {"Mystery": .6, "Romance": .15, "Fantasy" : .25},
    "Romance" : {"Mystery": .14, "Romance": .76, "Fantasy" : .1},
    "Fantasy" : {"Mystery": .2, "Romance": .12, "Fantasy" : .68}
}

class BookRecomender:
    """ This class contains the functionality to generate book recomendations
    using a Markov chain and display them in a bookmark """

    def __init__(self, start_book, num_recs):
        self.num_recs = num_recs
        self.start_book = start_book
    
    def generate_recs(self):
        """ Generate a sequence of books. """
        
        # Ensure starting book is not recommended
        book_recs = [self.start_book]
        current_book = self.start_book

        for i in range(self.num_recs):
            next_book = self.get_next_book(current_book)
            while (next_book in book_recs):
                next_book = self.get_next_book(current_book)
            book_recs.append(next_book)
            current_book = next_book
        
        # Ensure starting book is not recommended
        book_recs.remove(self.start_book)
        
        return book_recs
    
    def get_next_book(self, current_book):
        """ Decides which book to recommend next based on the current book.

        Args: current_book (book) - the last book recommended 
        """

        next_genre = random.choices(list(GENRE_TRANSITION_MATRIX.keys()), GENRE_TRANSITION_MATRIX[current_book.genre].values())[0]
        
        author_mtx = dict()
        title_mtx = dict()
        
        # Create author transition matrix
        if next_genre == current_book.genre:
            for author in list(BOOK_DICT[next_genre].keys()):
                author_mtx[author] = .5/(len(list(BOOK_DICT[next_genre]))-1)
            author_mtx[current_book.author] = .5
        else:
            for author in list(BOOK_DICT[next_genre].keys()):
                author_mtx[author] = 1/(len(list(BOOK_DICT[next_genre])))
            
        next_author = random.choices(list(author_mtx.keys()), list(author_mtx.values()))[0]
        
        # Create title transition matrix
        if next_author == current_book.author:
            for book_title in list(BOOK_DICT[next_genre][next_author].keys()):
                title_mtx[book_title] = 1/(len(list(BOOK_DICT[next_genre][next_author]))-1)
            title_mtx[current_book.title] = 0
        else:
            for book_title in list(BOOK_DICT[next_genre][next_author].keys()):
                title_mtx[book_title] = 1/(len(list(BOOK_DICT[next_genre][next_author])))

        next_title = random.choices(list(title_mtx.keys()), list(title_mtx.values()))[0]
        
        return BOOK_DICT[next_genre][next_author][next_title]

    
    def create_bookmark(self, book_recs):
        """ Displays the book recommendations in a bookmark format.
        
        Args: book_recs (list of books): The books to display
        """
        
        fig, axs = plt.subplots(1, len(book_recs), figsize=((len(book_recs)), 1.5))

        images = []
        for ax, book in zip(axs.flat, book_recs):
            images.append(ax.imshow(Image.open("assets/"+book.genre+"/"+book.author+"/"+book.title+".webp")))
            ax.set_axis_off()

        # Set background color based on the starting genre
        if self.start_book.genre == 'Mystery':
            fig.patch.set_facecolor('xkcd:blood red')
        elif self.start_book.genre == 'Romance':
            fig.patch.set_facecolor('xkcd:baby pink')
        else:
            fig.patch.set_facecolor('xkcd:mint green')
        
        plt.show()



def main():

    # Gather user input for initial recomendation
    genres = list(GENRE_TRANSITION_MATRIX.keys())
    genre = input("Enter your favorite genre (options: "+str(genres)+"): ").title()
    while genre not in genres:
        genre = input("Enter your favorite genre (options: "+str(genres)+"): ").title()
    
    authors = list(BOOK_DICT[genre].keys())
    author = input("Enter your favorite "+genre+" author (options: "+str(authors)+"): ").title()
    while author not in authors:
        author = input("Enter your favorite "+genre+" author (options: "+str(authors)+"): ").title()
    
    titles = list(BOOK_DICT[genre][author].keys())
    title = input("Enter your favorite "+author+" book (options: "+str(titles)+"): ").title()
    while title not in titles:
        title = input("Enter your favorite "+author+" book (options: "+str(titles)+"): ").title()
    
    num_recs = input("How many recommendations would you like? (options: 2-26): ").title()
    while not (num_recs.isdigit() and int(num_recs) >= 2 and int(num_recs) <= 26):
        num_recs = input("How many recommendations would you like? (options: 2-26): ").title()
    num_recs = int(num_recs)

    start_book = BOOK_DICT[genre][author][title]

    # Generate and display book recommendations
    book_recommender = BookRecomender(start_book, num_recs)
    book_recs = book_recommender.generate_recs()
    print("Recommendations:", book_recs)
    print("Download your bookmark and happy reading!")
    book_recommender.create_bookmark(book_recs)

if __name__ == "__main__":
    main()


