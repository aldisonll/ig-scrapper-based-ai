import requests
import json


headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'cookie': 'ig_did=431D3A32-C9F5-4424-8179-74F7FEE87F0F; rur=FRC; mid=XkhIdAAEAAG6hcZgaaV60vZrLK4x; shbid=14488; shbts=1581795473.2900448; sessionid=11802641302%3ArBHvDrVySBcda6%3A4; csrftoken=oa8C9Aya0OxJxMiFDeQkVEaJSdQs6stO; ds_user_id=11802641302; urlgen="{\\"79.106.127.225\\": 42313}:1j33Wg:sUvg7AOLp86e7wXw_iHhhjbne4U"',
}

params = (
('__a', '1'),
)


def getMedia(hashtag):
    
    for i in range(len(hashtag)):
     url = 'https://www.instagram.com/explore/tags/{}/'.format(hashtag[i])
     response = requests.get(url, headers=headers, params=params)
     text = response.text
     json_text = json.loads(text)
     posts_length = len(json_text["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"])
    
     for i in range(posts_length - 1):
       posts.append(json_text["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"][i]["node"]["shortcode"])
     

def checkMedia(posts,target,show_pic):
   for j in range(len(posts)):
    url = 'https://www.instagram.com/p/{}/'.format(posts[j])   
    response = requests.get(url, headers=headers, params=params)
    text = response.text
    json_text = json.loads(text)
    try:
     if json_text["graphql"]["shortcode_media"]["__typename"] == "GraphImage":
      shortcode = str(json_text["graphql"]["shortcode_media"]["shortcode"])
      user = str(json_text["graphql"]["shortcode_media"]["owner"]["username"])
      pic_url = str(json_text["graphql"]["shortcode_media"]["owner"]["profile_pic_url"])      
      filter = json_text["graphql"]["shortcode_media"]["accessibility_caption"]
      filter = filter.replace("Image may contain:","")
      filter = filter.split(" ")
      if show_pic is True:
          pic = ", picture url : {}".format(pic_url)
      else:
          pic = ""
      for h in range(len(based)):
       if based[h] in filter:
          print(f"This media: {shortcode} contain {based[h]}, posted by: {user} {pic}")
     else:
         pass
    except:
        print("err")
        pass



    
def AIScrapper(based,target,show_pic):
    global posts
    posts = []
    getMedia(target)
    checkMedia(posts,based,show_pic)
    

based = ["text","outdoor","screen","computer"]
target = ["programming","python3","python","javascript"]
show_pic = False

AIScrapper(based,target,show_pic)
