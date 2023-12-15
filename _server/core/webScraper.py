import requests
from bs4 import BeautifulSoup
import re

def createURL(gamertag):
    gamertag = gamertag.replace(' ', '%20')
    url = f'https://halodatahive.com/Player/Infinite/{gamertag}?route=Search'
    return url

def getNums(str):
    return re.findall('\d+', str)

def getStats(gamertag):
    url = createURL(gamertag)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    rankDiv = soup.find(id="csr-container")

    try:
        #print(rankDiv.text.split())
        rankDiv.text.split()
    except:
        #likley no user found.
        return False

    gamertag = soup.find(id='infinite-player-appearance-container')

    gamertag = gamertag.text.split()

    data = [] 


    for stat in soup.find_all('div', class_="card"):
        try:
            data.append(stat.text)
        except:
            print("whoops")

    for i in range(0, len(data[248])):
        try:
            data[i] = data[i].replace('\n', '')
            data[i] = data[i].replace('   ', '')
            
        except:
            print("nothing to remove")

        if i < 300:
            print(f"id {i}: {data[i]}")

    stats = {}

    stats['gamertag'] = gamertag[0]

    #id 7 53,875 kills
    kills = data[7].split()
    stats['kills'] = kills[0]

    #id 15:  54,712 Deaths
    deaths = data[15].split()
    stats['deaths'] = kills[0]

    #id 8 1.05 K?D
    kd = data[8].split()
    stats['K/D'] = kd[0]

    #id 11 24,000 assists
    assists = data[11].split()
    stats['assists'] = assists[0]

    #id 3.15 avg kda
    avgKDA = data[12].split()
    stats['avgKDA'] = avgKDA[0]

    #id 12 12,000 headshots
    headshots = data[13].split()
    stats["headshots"] = headshots[0]

    #id 16:  49.3% Accuracy
    accuracy = data[16].split()
    stats["accuracy"] = accuracy[0]

    #id 19:  17,525,571 Damage Dealt
    damageDealt = data[19].split()
    stats["damageDealt"] = damageDealt[0]
    
    #id 20:  17,161,176 Damage Taken
    damageTaken = data[19].split()
    stats["damageTaken"] = damageTaken[0]


    return stats

print(getStats("jadogg22"))

