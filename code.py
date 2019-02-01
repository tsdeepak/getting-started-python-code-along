# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
    data = yaml.load(f)
# Find data type of the file
# print(data)
d_type = type(data)
print(d_type)
# In which city, and at which venue the match was played and where was it played ?
city = data['info']['city']
venue = data['info']['venue']
print(city,venue)
# Which are all the teams that played in the tournament ? How many teams participated in total?
teams = data['info']['teams']
print(teams,len(teams))
# Which team won the toss and what was the decision of toss winner ?
toss_won_by = data['info']['toss']['winner']
choose_to = data['info']['toss']['decision']
print(toss_won_by,choose_to)
# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
first_batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
print(first_bowler,first_batsman)
# How many deliveries were delivered in first inning ?
print(len(data['innings'][0]['1st innings']['deliveries']))
# How many deliveries were delivered in second inning ?
print(len(data['innings'][1]['2nd innings']['deliveries']))
# Which team won and how ?
team_won = data['info']['outcome']['winner']
by_how = data['info']['outcome']['by']['runs']
print(team_won,by_how)



