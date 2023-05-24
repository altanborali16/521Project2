from django.db import connection
def returnMysteryActionShows(user):
    shows = []
    if(user == "oyku"):
        shows.append({"name": "Bones" , "score": "8"})
        shows.append({"name": "Criminal Minds" , "score": "8"})
        shows.append({"name": "How to get away with murder" , "score": "10"})
        shows.append({"name": "NCIS" , "score": "6"})
        shows.append({"name": "The Sinner" , "score": "6"})
        shows.append({"name": "The Stranger" , "score": "9"})
        shows.append({"name": "Sahsiyet" , "score": "9"})
        shows.append({"name": "Safe" , "score": "8"})
        shows.append({"name": "Quantico" , "score": "6"})
        shows.append({"name": "Nikita" , "score": "7"})
        shows.append({"name": "Alias" , "score": "7"})
        shows.append({"name": "Vikings" , "score": "7"})
        shows.append({"name": "iZombie" , "score": "8"})
        shows.append({"name": "Teen Wolf" , "score": "6"})
        return shows
    elif(user == "selen"):
        shows.append({"name": "Person Of Interest" , "score": "7"})
        shows.append({"name": "Breaking Bad" , "score": "9"})
        shows.append({"name": "Prison Break" , "score": "9"})
        return shows
    else:
        return False

def returnDramaDistopianShows(user):
    shows = []
    if(user == "oyku"):
        shows.append({"name": "Borgen" , "score": "8"})
        shows.append({"name": "Kirmizi Oda" , "score": "8"})
        shows.append({"name": "The Man in the High Castle" , "score": "9"})
        shows.append({"name": "See" , "score": "6"})
        shows.append({"name": "Khalifat" , "score": "8"})
        shows.append({"name": "Bodyguard" , "score": "9"})
        shows.append({"name": "Unorthadox" , "score": "9"})
        shows.append({"name": "The Handmaid's Tale" , "score": "9"})
        shows.append({"name": "Pretty Little Liars" , "score": "7"})
        shows.append({"name": "Scream(The Series)" , "score": "6"})
        shows.append({"name": "3%" , "score": "7"})
        shows.append({"name": "Merlin" , "score": "7"})
        shows.append({"name": "Daredevil" , "score": "9"})
        return shows

    elif(user == "selen"):
        shows.append({"name": "Altered Carbon" , "score": "6"})
        shows.append({"name": "Yaprak Dokumu" , "score": "9"})
        shows.append({"name": "Peaky Blinders" , "score": "8"})
        shows.append({"name": "Suits" , "score": "9"})
        return shows
    else:
        return False

def returnComedyShows(user):
    shows = []
    if(user == "oyku"):
        return shows
    elif(user == "selen"):
        shows.append({"name": "Friends" , "score": "9"})
        shows.append({"name": "Modern Family" , "score": "8"})
        shows.append({"name": "Scrubs" , "score": "8"})
        shows.append({"name": "The Office" , "score": "10"})
        shows.append({"name": "Brooklyn 9 9" , "score": "8"})
        shows.append({"name": "HIMYM" , "score": "9"})
        shows.append({"name": "Arrested Development" , "score": "7"})
        shows.append({"name": "Community" , "score": "9"})
        return shows
    else:
        return False 

def returnPopularShows():
    stmt = "SELECT name,score FROM shows WHERE score > 7;"
    cursor = connection.cursor()
    cursor.execute(stmt)
    tmp = cursor.fetchall()
    shows = []
    for s in tmp:
        x = {"name":s[0], "score":s[1]}
        shows.append(x)    
    return shows