# BookMark(ov) Maker
Danielle Simon

## Description
BookMark(ov) Maker creates bookmarks decorated with book covers of recommended books. To generate
recommendations, BookMark(ov) Maker uses a first-order Markov chain that considers the genre, author,
and title of the previously recommended (or initially entered) book to determine the next
recommendation. BookMark(ov) Maker stores the transition matrix for selecting the genre, but
dynamically creates the transition matrixes for selecting the next author and title depending on
the previous choices. First, BookMark(ov) Maker uses the transition matrix to select the genre of
the next recommedation, based on the last recommendation. If the genre is the same, then the
transition matrix for the author gives the last author a weight of .5 and divides the remaining .5
evenly amoung the remaining authors. If the genre is different, all authors are weighted equally.
In the case where the author is the same, the last recommended title is given a weight of 0 and the
rest are weighted evenly. Otherwise, all titles are weighted equally. However, Bookmark(ov) maker
also ensures that the same book is not recommended multiple times on the same bookmark by repeating the process to get a recommedation until an unseen book is given. After selecting the amount
of requested book recommendations, Bookmark(ov) Maker displays the covers of the books in a line
creating an excellent bookmark.

## How to Run
To run the program enter `python3 BookRecommender.py`
You will then be prompted to enter a genre, followed by an author, and then a title.
Note: currenly the author and title prompts are case sensitive.

## Personal Meaning
As an avid reader (when school is not in session), I am constantly asking friends and family for book
recommendations. I often find myself disappointed when I finish a great book and eager to find a similar one. Thus, I would personally find a system that provides book recommendations based on book similarity incredibly helpful. Additionally, I prefer paper books to online books because I believe holding a paper book and turning pages is part of the experience. Therefore, I can never have too many bookmarks and am excited about every bookmark my system produces.

## Challenges

## Creativity
Bookmark(ov) maker is creative because it has aspects that have value and novelty. Bookmark(ov) Maker
produces book recommendations which are useful to readers. These recommendations take into account the genre and author of a book that the reader previously enjoyed, making the recommendations helpful and personalized. Bookmark(ov) Maker also produces bookmarks with novelty because it is highly
unlikely that the exact bookmark has been created before.

## Sources
All book cover images were taken from amazon.com.