import json
import requests

class Search_Image:
  def __init__(self,name):
      self.image_link = ""
      name = name.lower()
      api_key = "563492ad6f917000010000014b02ee3259ad4acc918cb303d0a48d65"
      url  = "https://api.pexels.com/v1/search?"
      search_param = {"query": name,"per_page": "1"}
      headers = {"Authorization": api_key}
      try:
          response = requests.get(url, params=search_param, headers=headers)
          data = response.json()
          self.image_link = data['photos'][0]['src']['large']

      except Exception as e:
          self.image_link = None
        #   print('there is err: ', e)
      
