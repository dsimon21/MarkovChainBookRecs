# BookMark(ov) Maker
Danielle Simon

## Description
BookMark(ov) Maker creates bookmarks decorated with book covers of recommended books. To generate
recommendations, BookMark(ov) Maker uses a first-order Markov chain that considers the genre, author,
and title of the previously recommended (or initially entered) book to determine the next
recommendation. BookMark(ov) Maker stores the transition matrix for selecting the genre, but
dynamically creates the transition matrices for selecting the next author and title depending on
the previous choice. First, BookMark(ov) Maker uses the transition matrix to select the genre of
the next recommendation, based on the last recommendation. If the genre is the same, then the
transition matrix for the author gives the last author a weight of .5 and divides the remaining .5
evenly amoung the remaining authors of the genre. If the genre is different, all authors of the genre
are weighted equally. In the case where the author is the same, the last recommended title is given a
weight of 0 and the rest are weighted evenly. Otherwise, all titles are weighted equally. However,
Bookmark(ov) maker also ensures that the same book is not recommended multiple times on the same
bookmark by repeatedly calling the function to get the next recommendation until an unseen book is
returned. After selecting the amount of requested book recommendations, Bookmark(ov) Maker displays
the covers of the books in a line creating an excellent bookmark.

## How to Run
To run the program enter `python3 BookRecommender.py` \
You will then be prompted to enter a genre, followed by an author, and then a title. \
Note: currently the author and title prompts are case sensitive (since they are dictionary keys).

## Personal Meaning
As an avid reader (when school is not in session), I am constantly asking friends and family for book
recommendations. I often find myself disappointed when I finish a great book and eager to find a similar
one. Thus, I would personally find a system that provides book recommendations based on book similarity
incredibly helpful. Additionally, I prefer paper books to online books because I believe there is something
special about holding a paper book and turning pages. Therefore, I can never have too many bookmarks and am
excited about every bookmark my system produces.

## Challenges
I challenged myself to use a language that I am not yet comfortable with, work independently, and to add
complexity. I had used Python before for simple projects years ago but was not very familiar with
object-oriented Python or many Python libraries. However, I decided to challenge myself to use Python to
take advantage of the mathplotlib library to display images in a neat plot. I learned how to implement the
`__str__`  and `__repr__` methods which helped me test my program. I also learned that I can implement the
`__eq__` method to then be able to use the `in` keyword to check if an equal object is in a list or set.
However, since I was storing all the known books in a dictionary, I was able to use dictionary keys to always
pass the exact object and avoid using extra space. Using Python was valuable because it taught me more about
the specifics of the language but more importantly, it taught me about how to learn a language and how to find
the methods and tools I needed. I also challenged myself to work independently. This was the first project I
completed in several years where I wrote all of my code and made all of my design decisions without consulting
a classmate or seeking approval from a mentor. Though I could have talked the project through with a classmate,
I wanted to push myself outside of my comfort zone and gain the confidence that I could work through my
confusions on my own. I also challenged myself by adding complexity in my Markov Chain implementation. I wanted
to use dynamically created transition matrices to be able to generate logical recommendations for a variety of
books without having to hardcode each one. This required me to think beyond the simple Markov Chains I had made
in class, but allowed me to create a program I am proud of. I hope to continue to learn how to add complexity
and master new tools that will allow me to do so. For example, I could make my project better by scraping the web
to populate my dictionary of books and taking into account that some books can be classified as multiple genres
and thus should also dynamically create genre transition matrices.

## Creativity
Bookmark(ov) maker is creative because it has aspects that have value and novelty. Bookmark(ov) Maker produces
book recommendations which are useful to readers. These recommendations take into account the genre and author
of a book that the reader previously enjoyed, making the recommendations helpful and personalized. Bookmark(ov)
Maker also produces bookmarks with novelty because it is highly unlikely that the exact bookmark has been created
before.

## Sources
All book cover images were taken from amazon.com.
