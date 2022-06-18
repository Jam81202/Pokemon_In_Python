from starter_town import *
from route_one import *
from route_two import *
from village import *
from city_one import *

global location
location = 1
player_spawn_w = 30
player_spawn_h = 144

while True:
    if location == 1:
        location, player_spawn_w, player_spawn_h = starter_town(player_spawn_w, player_spawn_h)

    elif location == 2:
        location, player_spawn_w, player_spawn_h = route_one(player_spawn_w, player_spawn_h)

    elif location == 3:
        location, player_spawn_w, player_spawn_h = route_two(player_spawn_w, player_spawn_h)

    elif location == 4:
        location, player_spawn_w, player_spawn_h = village(player_spawn_w, player_spawn_h)

    elif location == 5:
        location, player_spawn_w, player_spawn_h = city_one(player_spawn_w, player_spawn_h)