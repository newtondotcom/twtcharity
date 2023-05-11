from bs4 import BeautifulSoup  
import requests
from datetime import datetime
import json

user = "twtcharity"
url = "https://socialblade.com/twitter/user/"+user

#Add agent to avoid 403 error
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def update_numbers():
    stats = []
    html_content = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html_content, "html.parser")
    followers_element = soup.find('span',{"class": "YouTubeUserTopInfo"})
    followers_element = soup.find_all("div", {"class": "YouTubeUserTopInfo"})
    for element in followers_element:
        stats.append(element.text.replace("\n"," ").strip().replace(" ",":"))
    nb_followers = stats[0].split(":")[1]
    nb_followings = stats[1].split(":")[1]
    nb_likes = stats[2].split(":")[1]
    nb_tweets = stats[3].split(":")[1]

    #read json file
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
    
        data.append({
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "followers": nb_followers,
            "followings": nb_followings,
            "likes": nb_likes,
            "tweets": nb_tweets
        })
        
    #write json file
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

update_numbers()