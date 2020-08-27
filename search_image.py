import json
import requests

class Search_Image:
  def __init__(self,name):
      self.image_links = []

      name = name.lower()
      api_key = "563492ad6f917000010000014b02ee3259ad4acc918cb303d0a48d65"
      url  = "https://api.pexels.com/v1/search?"
      search_param = {"query": name,"per_page": "12"}
      headers = {"Authorization": api_key}
      try:
          response = requests.get(url, params=search_param, headers=headers)
          data = response.json()
          for photo in data["photos"]:
            photo_url = photo["src"]["large"]
            self.image_links.append(photo_url)

      except Exception as e:
          self.image_links = []
          print('there is err: ', e)

  def __str__(self):
    return f"this is the gallery: {self.image_links}"
      
