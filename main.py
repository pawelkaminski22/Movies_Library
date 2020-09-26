import random

library = [{'title': 'Rick', 'year': 1994, 'kind': 'Action', 'plays': 0},
           {'title': 'Mask', 'year': 1998, 'kind': 'Comedy', 'plays': 0},
           {'title': 'Matrix', 'year': 2001, 'kind': 'SF', 'plays': 0},
           {'title': 'Friends', 'year': 1999, 'kind': 'Series', 'season': 1, 'episode': 2, 'plays': 0},
           {'title': 'Monk', 'year': 1988, 'kind': 'Series', 'season': 9, 'episode': 4, 'plays': 0},
           {'title': 'Alternatywy', 'year': 1965, 'kind': 'Series', 'season': 3, 'episode': 5, 'plays': 0},
           ]


class Movie:
    def __init__(self, title, year, kind, plays):
        self.title = title
        self.year = year
        self.kind = kind
        self.plays = plays

    def play(self):
        self.plays += 1
        print(f'Movie: {self.title} ({self.year})')
        return


class Series(Movie):
    def __init__(self, title, year, kind, season, episode, plays):
        super().__init__(title, year, kind, plays)
        self.season = season
        self.episode = episode

    def play(self):
        super().play()
        print(f'It is S0{self.episode}E0{self.season}')


def search(value):
    for i in library:
        if i['title'] == value:
            print(f'We have position {value} in our library')


def get_movies():
    movies = []
    print('_____________')
    print('Available Movies:')
    for i in library:
        if i['kind'] != 'Series':
            movies.append({'title': i['title'], 'year': i['year']})
    sorted_movies = sorted(movies, key=lambda k: k['title'])
    for i in sorted_movies:
        print(i['title'], i['year'])


def get_series():
    series = []
    print('_____________')
    print(f'Available Series:')
    for i in library:
        if i['kind'] == 'Series':
            series.append({'title': i['title'], 'year': i['year']})
    sorted_series = sorted(series, key=lambda k: k['title'])
    for i in sorted_series:
        print(i['title'], i['year'])


def generate_views():
    result = random.choice(library)
    views = random.randint(1, 100)
    for i in library:
        if i['title'] == result['title']:
            i['plays'] = views


def run_generate_views(value):
    for i in range(value):
        generate_views()


def top_titles(value):
    top_views = sorted(library, key=lambda k: k['plays'], reverse=True)[:value]
    print(f'-----------------')
    print(f'Top viewed positions are:')
    for i in top_views:
        print(i['title'], f'seen', i['plays'], f'times')


if __name__ == '__main__':
    print('Welcome to Movies Library')
    get_movies()
    get_series()
    run_generate_views(10)
    top_titles(3)





