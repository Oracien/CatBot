import urllib.request
#Now replaced with using OAuth2 for direct imgur access
#import json
import io
import random
from imgurpython import ImgurClient

client_id = #YourClientID
client_secret = #YourClientSecret
access_token = #YourAccessToken
refresh_token = #YourRefreshToken

client = ImgurClient(client_id, client_secret, access_token, refresh_token)



class Champion:

    def __init__(self, name, link):
        self.name = name
        self.link = link
        self.pictures = []

    '''def update(self):
        url = self.link + ".json"
        text = requests.get(url)
        data = json.loads(r.text)
        print (data)'''
    
    def update(self):
        if self.link == "":
            print ("Error: No album link available")
            return False
        '''url = self.link + ".json"
        try:
            encoded = urllib.request.urlopen(url).read()
        except:
            print("Error: Retrieval of link failed")
            return False
        parsed = json.loads(encoded.decode("utf-8"))
        images = parsed["data"]["image"]["album_images"]["images"]
        '''
        album_pictures = client.get_album_images(self.link)
        pictures = []
        for i in album_pictures:
            self.pictures.append(i.link)
        print (self.name + " was updated succesfully")
        return True
            
    def album(self):
        album_link = "http://imgur.com/a/" + self.link
        return album_link

    def random_picture(self):
        return random.choice(self.pictures)

    def list_of_pictures(self):
        return list(self.pictures)

list_of_champion_objects = {}

dictionary_champions = {
                        "ahri":"Ls8ih",
                        "akali":"",
                        "ashe":"",
                        "anivia":"",
                        "braum":"4nWho",
                        "caitlyn":"",
                        "cassiopeia":"",
                        "elise":"",
                        "evelynn":"",
                        "fiora":"",
                        "illaoi":"",
                        "irelia":"",
                        "janna":"",
                        "jinx":"",
                        "kalista":"",
                        "karma":"",
                        "katarina":"",
                        "leblanc":"",
                        "leona":"",
                        "lissandra":"",
                        "lulu":"",
                        "lux":"",
                        "missfortune":"",
                        "morgana":"",
                        "nami":"",
                        "nidalee":"",
                        "orianna":"",
                        "poppy":"",
                        "quinn":"",
                        "riven":"",
                        "sejuani":"",
                        "shyvana":"",
                        "sivir":"",
                        "sona":"",
                        "soraka":"",
                        "syndra":"IIXKd",
                        "taliyah":"",
                        "tristana":"",
                        "vayne":"",
                        "vi":"",
                        "zyra":"",
                        }

def create_all():
    for x in dictionary_champions:
        list_of_champion_objects[x] = Champion(x, dictionary_champions[x])
        print ("Created the " + str(list_of_champion_objects[x].name) + " object")

def update_all():
    for x, y in list_of_champion_objects.items():
        y.update()


