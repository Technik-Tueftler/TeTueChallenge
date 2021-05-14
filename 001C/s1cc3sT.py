from uuid import uuid4


class player:
    def __init__(self, name, secrets=0, playtime_s=0, kills=0):
        self.gameid = uuid4()  # create unique id
        self.name = name
        self.secrets = secrets
        self.playtime_s = playtime_s  # playing time in seconds
        self.kills = kills


def sort_player(player_list):
    player_list.sort(key=lambda x: (x.secrets, -x.playtime_s, x.kills), reverse=True)
