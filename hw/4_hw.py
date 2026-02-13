class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.duration}min)"

    def __add__(self, other):
        if type(other) == Movie:
            return self.duration + other.duration
        else:
            pass

    def __eq__(self, other):
        if type(other) == Movie and self.title == other.title and self.duration == other.duration:
            return True
        else:
            return False

class Library:
    def __init__(self, movies):
        self.movies = movies

    def __getitem__(self, index):
        return self.movies[index]

    def __len__(self):
        return len(self.movies)

    def __str__(self):
        return ", ".join(str(movie) for movie in self.movies)

class User:
    def __init__(self, name, library_):
        self.name = name
        self.library = library_

    def __call__(self):
        return f"User {self.name} is watching movies."

    def __str__(self):
        return f"User: {self.name} | Movies: {self.library}"


m1 = Movie("Matrix", 136)
m2 = Movie("Inception", 148)
m3 = Movie("Interstellar", 169)
library = Library([m1, m2, m3])
user = User("Alex", library)
print(m1)
print(m1 + m2)
print(m1 == m2)
print(library[1])
print(len(library))
print(library)
print(user)
user()

