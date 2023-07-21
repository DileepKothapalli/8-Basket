import copy
import pandas as pd

first_team = [
    ["Bam Adebayo", "c", 17, 40.246429],
    ["Dewayne Dedmon", "c", 7, 16.174627],
    ["Gabe Vincent", "pg", 7.5, 17.370588],
    ["Jimmy Butler", "sf", 18.5, 40.915789],
    ["Max Strus", "sg", 8.5, 17.300000],
    ["Tyler Herro", "sg", 13.5, 32.398485],
    ["Kyle Lowry", "pg", 13.5, 31.387302],
    ["P.J. Tucker", "pf", 8.5, 19.435211],
    ["Caleb Martin", "pf", 7.5, 18.916667],
    ["Duncan Robinson", "sf", 9.5, 17.824051],
    ["Udonis Haslem", "sf", 5, 5.307692],
    ["Haywood Highsmith", "sf", 4.5, 5.010526],
    ["Omer Yurtseven", "c", 6, 14.201786],
    ["Markieff Morris", "c", 5.5, 12],
    ["Victor Oladipo", "sg", 5.5, 21.325000],
    ["Javonte Smart", "sg", 4.5, 9],
    ["Mychal Mulder", "pg", 5, 11.800000],
]

second_team = [
    ["Bogdan Bogdanovic", "sg", 12, 27.253968],
    ["Trae Young", "pg", 20, 46.517105],
    ["John Collins", "pf", 13.5, 32.155556],
    ["Kevin Huerter", "sg", 10.5, 22.341892],
    ["DeAndre Hunter", "sf", 10, 21.211321],
    ["Delon Wright", "pg", 8, 15.311688],
    ["Danilo Gallinari", "pf", 9.5, 20.819697],
    ["Onyeka Okongwu", "c", 9.5, 21.668750],
    ["Timothe Luwawu-Cabarrot", "sf", 6, 8.411538],
    ["Kevin Knox", "sf", 4.5, 5.288235],
    ["Gorgui Dieng", "c", 5.5, 9.140909],
]

cost = 100


# initial Allotment

total_list = []
for i in first_team:
    i.append(1)
    total_list.append(i)

for i in second_team:
    i.append(2)
    total_list.append(i)

sorted_list = copy.deepcopy(total_list)
sorted(sorted_list, key=lambda l: l[1])
sorted_list.sort(key=lambda l: l[3])


initial_allotment = []

# returns the first type of player


def first_type_player(player_list, pos):
    for i in player_list:
        if i[1] == pos:
            return i


pos_list = ["pg", "sg", "sf", "pf", "c"]
for i in range(5):
    initial_allotment.append(first_type_player(sorted_list, pos_list[i]))


def stats_of_team(curr_list):
    f = 0
    s = 0
    cost = 0
    value = 0
    for i in curr_list:
        cost += i[2]
        value += i[3]
        if i[4] == 1:
            f += 1
        else:
            s += 1
    return f, s, cost, value


# add other three players
def add_player_with_constraints(player_list, curr_list):
    first, sec, cost, value = stats_of_team(curr_list)
    for i in player_list:
        if i not in curr_list:
            if i[4] == 1 and first == 5:
                continue
            if i[4] == 2 and sec == 5:
                continue
            if cost + i[2] > 100:
                continue
            curr_list.append(i)
            break


add_player_with_constraints(sorted_list, initial_allotment)
add_player_with_constraints(sorted_list, initial_allotment)
add_player_with_constraints(sorted_list, initial_allotment)

print(initial_allotment)

print(stats_of_team(initial_allotment))


### swapping
