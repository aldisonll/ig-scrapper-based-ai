import requests
import json


def getMedia(hashtag):
    
    for i in range(len(hashtag)):
     url = 'https://www.instagram.com/explore/tags/{}/?__a=1'.format(hashtag[i])
     response = requests.get(url)
     text = response.text
     json_text = json.loads(text)
     posts_length = len(json_text["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"])
    
     for i in range(posts_length - 1):
       posts.append(json_text["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"][i]["node"]["shortcode"])
     

def checkMedia(posts,target,show_pic):
   for j in range(len(posts)):
    url = 'https://www.instagram.com/p/{}/?__a=1'.format(posts[j])   
    response = requests.get(url)
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
