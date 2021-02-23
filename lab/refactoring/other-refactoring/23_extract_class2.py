# by Kami Bigdely
# Extract class

class Person:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email
    
    def born_after_1985(self):
        return self.birth_year > 1985
    
    def movies_watched(self):
        print('Movies Played: ', end='')
        for m in self.movies:
            print(m, end=', ')
    
    def send_hiring_email(self):
        print("email sent to:", self.email)


elizabeth_movies = ['Tenet', 'Vita & Virgina',
                    'Guardians of the Galaxy', 'The Great Gatsby']
elizabeth = Person("Elizabeth", "Debicki", 1990,
                   elizabeth_movies, "deb@makeschool.com")

if elizabeth.born_after_1985():
    elizabeth.movies_watched()
    elizabeth.send_hiring_email()

jim_movies = ['Ace Ventura', 'The Mask',
              'Dumb and Dumber', 'The Truman Show', 'Yes Man']
jim = Person("Jim", "Carrey", 1962, jim_movies, "jim@makeschool.com")

if jim.born_after_1985():
    jim.movies_watched()
    jim.send_hiring_email()

# first_names = ['elizabeth', 'Jim']
# last_names = ['debicki', 'Carrey']
# birth_year = [1990, 1962]
# movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galaxy', 'The Great Gatsby'],\
#      ['Ace Ventura', 'The Mask', 'Dumb and Dumber', 'The Truman Show', 'Yes Man']]
# emails = ['deb@makeschool.com', 'jim@makeschool.com']

# def send_hiring_email(email):
#     print("email sent to: ", email)
    
# for i, value in enumerate(emails):
#     if birth_year[i] > 1985:
#         print(first_names[i], last_names[i])
#         print('Movies Played: ', end='')
#         for m in movies[i]:
#             print(m, end=', ')
#         print()
#         send_hiring_email(value)
