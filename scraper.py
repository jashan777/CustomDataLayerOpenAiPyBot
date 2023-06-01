import requests
from bs4 import BeautifulSoup
import json

#gets the main data (scripts) from the URL , have been customized to access data from www.imsdb.com 
def Get_text(url):
    
    response = requests.get(url)
    content = response.content
    parser = BeautifulSoup(content, 'html.parser')
    textraw = parser.find("pre") 

    if (textraw):
        return textraw.text
    else:
        textraw = parser.find(class_="scrtext")

    return textraw.text


if __name__ == "__main__":
	
    print("starting...")

    all_episodes_scripts = {} #initalizing a dictionary 

    all_episodes_scripts["star-wars"] = {} #adding key to the dictionary

    #URL of (I-VI) starwar episodes
    links_list = ["http://www.imsdb.com/scripts/Star-Wars-The-Phantom-Menace.html",
                  "https://imsdb.com/scripts/Star-Wars-Attack-of-the-Clones.html",
                  "https://imsdb.com/scripts/Star-Wars-Revenge-of-the-Sith.html",
                  "https://imsdb.com/scripts/Star-Wars-Return-of-the-Jedi.html",
                  "https://sfy.ru/script/star_wars_empire_strikes_back_1980",
                  "https://imsdb.com/scripts/Star-Wars-Return-of-the-Jedi.html"
                  ]

    episode_names = ["episode-1","episode-2","episode-3","episode-4","episode-5","episode-6"]

    episode_script = {} # initializing a dictonary which will contain the episode as key and their script as value

    for i,link in enumerate(links_list):

        print("getting data for ",episode_names[i])
        text = Get_text(link) 
        episode_script[episode_names[i]] = text 
        print("got it")

    all_episodes_scripts["star-wars"] = episode_script #updating the star-wars key with its epsiodes as value

    print("Serialising data...")

    with open('data/all_episodes_starwars_raw.json', 'w') as data:
        json.dump(all_episodes_scripts, data) #jsonizing all the dictionary into a json format.

    print("Data saved.")

    print("finished")
