file = open('world_series.txt','r')
win = 0
cont = 1
data = file.read()
list = data.replace('\n', '\t').split("\t")
team = input('What team do you want to search for: ')
for champ in list:
    if cont <= len(list)-2:
        cont += 1
    if champ == team:
        print(list[cont-3])
        win += 1
print(team,'won',win,'World Series')
file.close()