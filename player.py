import random

class Player:

    name = None
    countries = []

    def __init__(self, name):
        self.name = name


def create_player_list(player_names: [], r):

    player_names_shuffled = player_names.copy()
    r.shuffle(player_names_shuffled)

    players = []

    for player_name in player_names_shuffled:

        new_player = Player(name= player_name)
        players = players + [new_player]

    return players


def assign_countries_to_players(players: [], countries: [], r):

    countries_shuffled = countries.copy()
    players_with_countries = players.copy()

    r.shuffle(countries_shuffled)

    out_of_countries = False

    while not out_of_countries:

        for player in players_with_countries:

            random_country = countries_shuffled.pop()
            player.countries = player.countries + [random_country]

            if countries_shuffled == []:
                out_of_countries = True
                break

    return players_with_countries


def print_players_countries(players: []):
    for i in range(100):
        print()
    for player in players:
        print(player.name, "has been assigned... ")
        print(*player.countries, sep = ", ")
        print()
    for i in range(20):
        print()
