""" BookRecommender.py

This file generates bookmarks containing book recomendations based on user
input and using a Markov Chain.

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
    "mystery" : {
        "Karen McManus" : {
            "One of Us is Lying" : Book("mystery", "Karen McManus", "One of Us is Lying"),
            "Two Can Keep a Secret" : Book("mystery", "Karen McManus", "Two Can Keep a Secret"),
            "You'll be the Death of Me" : Book("mystery", "Karen McManus", "You'll be the Death of Me")},
        "Holly Jackson" : {
            "A Good Girl's Guide to Murder" : Book("mystery", "Holly Jackson", "A Good Girl's Guide to Murder"),
            "Five Survive" : Book("mystery", "Holly Jackson", "Five Survive"),
            "The Reappearance of Rachel Price" : Book("mystery", "Holly Jackson", "The Reappearance of Rachel Price")},
        "Jennifer Lynn Barnes" : {
            "The Inheritance Games" : Book("mystery", "Jennifer Lynn Barnes", "The Inheritance Games"),
            "The Naturals" : Book("mystery", "Jennifer Lynn Barnes", "The Naturals"),
            "Raised by Wolves" : Book("mystery", "Jennifer Lynn Barnes", "Raised by Wolves")},
    },
    "fantasy" : {
        "Sarah J Mass" : {
            "Throne of Glass" : Book("fantasy", "Sarah J Mass", "Throne of Glass"),
            "A Court of Thorns and Roses" : Book("fantasy", "Sarah J Mass", "A Court of Thorns and Roses"),
            "Crescent City" : Book("fantasy", "Sarah J Mass", "Crescent City")},
        "Rick Riordan" : {
            "Percy Jackson and the Olympians" : Book("fantasy", "Rick Riordan", "Percy Jackson and the Olympians"),
            "The Kane Chronicles" : Book("fantasy", "Rick Riordan", "The Kane Chronicles"),
            "The Heroes of Olympus" : Book("fantasy", "Rick Riordan", "The Heroes of Olympus")},
        "Veronica Roth" : {
            "Divergent" : Book("fantasy", "Veronica Roth", "Divergent"),
            "Chosen Ones" : Book("fantasy", "Veronica Roth", "Chosen Ones"),
            "When Amoung Crows" : Book("fantasy", "Veronica Roth", "When Amoung Crows")},
    },
    "romance" : {
        "Sarah Dessen" : {
            "Along for the Ride" : Book("romance", "Sarah Dessen", "Along for the Ride"),
            "The Truth About Forever" : Book("romance", "Sarah Dessen", "The Truth About Forever"),
            "Someone Like You" : Book("romance", "Sarah Dessen", "Someone Like You")},
        "Emily Henry" : {
            "Beach Read" : Book("romance", "Emily Henry", "Beach Read"),
            "Happy Place" : Book("romance", "Emily Henry", "Happy Place"),
            "Book Lovers" : Book("romance", "Emily Henry", "Book Lovers")},
        "Taylor Jenkins Reed" : {
            "Maybe in Another Life" : Book("romance", "Taylor Jenkins Reed", "Maybe in Another Life"),
            "One True Loves": Book("romance", "Taylor Jenkins Reed", "One True Loves"),
            "Forever Interrupted" : Book("romance", "Taylor Jenkins Reed", "Forever Interrupted")},
    }
}

GENRE_TRANSITION_MATRIX = {
    "mystery" : {"mystery": .6, "romance": .15, "fantasy" : .25},
    "romance" : {"mystery": .14, "romance": .76, "fantasy" : .1},
    "fantasy" : {"mystery": .2, "romance": .12, "fantasy" : .68}
}

class BookRecomender:
    """ This class contains the functionality to generate book recomendations
    using a Markov chain and display them in a bookmark """

    def __init__(self, start_book, num_recs):
        self.num_recs = num_recs
        self.start_book = start_book
    
    def generate_recs(self):
        """ Generate a sequence of books. """
        
        book_recs = [self.start_book] # to ensure start is not recommended
        current_book = self.start_book

        for i in range(self.num_recs):
            next_book = self.get_next_book(current_book)
            while (next_book in book_recs):
                next_book = self.get_next_book(current_book)
            book_recs.append(next_book)
            current_book = next_book
        
        book_recs.remove(self.start_book)
        
        print(book_recs)
        return book_recs
    
    def get_next_book(self, current_book):
        """ Decides whic book to recommend next based on the current book.

        Args: current_book (book) - the last book recommended 
        """

        next_genre = random.choices(list(GENRE_TRANSITION_MATRIX.keys()), GENRE_TRANSITION_MATRIX[current_book.genre].values())[0]
        
        author_mtx = dict()
        title_mtx = dict()
        
        if next_genre == current_book.genre:
            for author in list(BOOK_DICT[next_genre].keys()):
                author_mtx[author] = .5/(len(list(BOOK_DICT[next_genre]))-1)
            author_mtx[current_book.author] = .5
        else:
            for author in list(BOOK_DICT[next_genre].keys()):
                author_mtx[author] = 1/(len(list(BOOK_DICT[next_genre])))
            
        next_author = random.choices(list(author_mtx.keys()), list(author_mtx.values()))[0]
        
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
        """ Displays the book recommendations in a bookmark format
        
        Args: book_recs (list of books): The books to display
        """
        
        fig, axs = plt.subplots(1, len(book_recs), figsize=((len(book_recs)), 1.5))

        images = []
        for ax, book in zip(axs.flat, book_recs):
            images.append(ax.imshow(Image.open("assets/"+book.genre+"/"+book.author+"/"+book.title+".webp")))
            ax.set_axis_off()

        if self.start_book.genre == 'mystery':
            fig.patch.set_facecolor('xkcd:blood red')
        elif self.start_book.genre == 'romance':
            fig.patch.set_facecolor('xkcd:baby pink')
        else:
            fig.patch.set_facecolor('xkcd:mint green')
        
        plt.show()



def main():

    # Gather user input for initial recomendation
    genres = list(GENRE_TRANSITION_MATRIX.keys())
    genre = input("Enter your favorite genre (options: "+str(genres)+"): ").lower()
    while genre not in genres:
        genre = input("Enter your favorite genre (options: "+str(genres)+"): ").lower()
    
    authors = list(BOOK_DICT[genre].keys())
    author = input("Enter your favorite "+genre+" author (options: "+str(authors)+"): ")
    while author not in authors:
        author = input("Enter your favorite "+genre+" author (options: "+str(authors)+"): ")
    
    titles = list(BOOK_DICT[genre][author].keys())
    title = input("Enter your favorite "+author+" book (options: "+str(titles)+"): ")
    while title not in titles:
        title = input("Enter your favorite "+author+" book (options: "+str(titles)+"): ")
    
    num_recs = input("How many recommendations would you like? (options: 2-26): ")
    while not (num_recs.isdigit() and int(num_recs) >= 2 and int(num_recs) <= 26):
        num_recs = input("How many recommendations would you like? (options: 2-26): ")
    num_recs = int(num_recs)

    start_book = BOOK_DICT[genre][author][title]

    # Generate and display book recommendations
    book_recommender = BookRecomender(start_book, num_recs)
    book_recs = book_recommender.generate_recs()
    print("Download your bookmark and happy reading!")
    book_recommender.create_bookmark(book_recs)

if __name__ == "__main__":
    main()


