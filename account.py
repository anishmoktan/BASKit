#Will have the class for each accounts

import time
import json

class Account():
    def __init__(self, username, saved_images = []):
        self.username = username
        self.saved_images = saved_images

    def __str__(self):
        return(f"This is username: {self.username}"
                "This is your saved images: {self.saved_images}")


    @classmethod
    def from_json(cls, data):
        username, saved_images = data["username"], []
        for item in data["saved_images"]:
            tuple_item = tuple(item)
            saved_images.append(tuple_item)
        return cls(username=username,
                   saved_images=saved_images)


    def add_image(self, new_image):
        (new_image_name, new_image_count) = new_image
        for i in range(len(self.saved_images)):
            image = self.saved_images[i]
            (image_name, image_count) = image
            if image_name ==new_image_name:
                image_count += new_image_count
                self.saved_images.pop(i)
                self.saved_images.append((image_name, image_count))
                break
        else:
            self.saved_images.append(new_image)
        print(f"this is your all saved images: {self.saved_images}\n")



    def remove_image(self, target_image):
        for i in range(len(self.saved_images)):
            image = self.saved_images[i]
            image_name = image[0]
            if image_name == target_image:
                self.saved_images.pop(i)
                break
        else:
            print(f"\"{target_image}\" doesn't exist in your saved images.")
        print(f"this is your all saved images: {self.saved_images}\n")

        time.sleep(2)