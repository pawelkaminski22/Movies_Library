from random import random
import random

library = []


class Movie:
    def __init__(self, title, year, kind, plays):
        self.title = title
        self.year = year
        self.kind = kind
        self.plays = plays

    def __str__(self):
        return f'{self.title} ({self.year})'

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_kind(self):
        return self.year

    def get_plays(self):
        return self.plays

    def play(self):
        self.plays += 1
        print(f'{self.title} {self.year}')


class Series(Movie):
    def __init__(self, title, year, kind, season, episode, plays):
        super().__init__(title, year, kind, plays)
        self.season = season
        self.episode = episode

    def get_season(self):
        return self.season

    def get_episode(self):
        return self.episode

    def play(self):
        super().play()
        print(f'It is S0{self.season}E0{self.episode}')


def search(value):
    for i in library:
        if i.title == value:
            print(f'We have position {value} in our library')


def get_movies():
    movies = []
    print('_____________')
    print('Available Movies:')
    for i in library:
        if i.kind != 'Series':
            movies.append({'title': i.title, 'year': i.year})
    sorted_movies = sorted(movies, key=lambda k: k['title'])
    for i in sorted_movies:
        print(i['title'], i['year'])


def get_series():
    series = []
    print('_____________')
    print(f'Available Series:')
    for i in library:
        if i.kind == 'Series':
            series.append({'title': i.title, 'year': i.year})
    sorted_series = sorted(series, key=lambda k: k['title'])
    for i in sorted_series:
        print(i['title'], i['year'])


def generate_views():
    result = random.choice(library)
    views = random.randint(1, 100)
    for i in library:
        if i.title == result.title:
            i.plays = views


def run_generate_views(value):
    for i in range(value):
        generate_views()


def top_titles(value):
    top_views = sorted(library, key=lambda k: k.plays, reverse=True)[:value]
    print(f'-----------------')
    print(f'Top viewed positions are:')
    for i in top_views:
        print(i.title, f'seen', i.plays, f'times')


if __name__ == '__main__':
    movie = Movie
    series = Series

    library.append(movie('Rick', 1994, 'Action', 0))
    library.append(movie('Mask', 1998, 'Comedy', 0))
    library.append(movie('Matrix', 2001, 'SF', 0))
    library.append(series('Friends', 2001, 'Series', 1, 2, 0))
    library.append(series('Monk', 1989, 'Series', 2, 4, 0))
    library.append(series('Lego', 1800, 'Series', 8, 6, 0))
    run_generate_views(10)

    print('Welcome to Movies Library')
    print(*library, sep='\n')
    top_titles(3)

    #get_movies()
    #get_series()
    #search('Rick')





