


# Solution 1

def greetings(first_name, last_name):
    print("{last_name}, {first_name} {last_name}")

greetings("James", "Bond")

# ***************************************************************************************************************************

# Solution 2

def KDA(kills, deaths, assists):
    if deaths == 0:
        return (kills + assists) / 1
    
    else:
        return (kills + assists) / deaths if deaths != 0 else 0
    

kills = 10
deaths = 2
assists = 5

kd_ratio = KDA(kills, deaths, assists)
print('KD_RATIO:', kd_ratio)