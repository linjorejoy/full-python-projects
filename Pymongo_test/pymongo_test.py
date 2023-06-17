from pymongo import MongoClient

client = MongoClient()

db = client.test_database
image_doc = db.image_obj
people = db.people


class ImageObj:
    def __init__(self):
        self.title = ""
        self.hash_hex = ""
        self.people = []


class Person:
    def __init__(self):
        self.name = ""
        self.photos = []


image = ImageObj()
image.title = "Some Title"
image.hash_hex = "wfsdsys8sd88dssd8sd79sd"
print(image.__dict__)
image_id = image_doc.insert_one(image.__dict__).inserted_id
print(image_id)

person = Person()
person.name = "Linjo"
person.photos.append(image_id)
person_id = people.insert_one(person.__dict__).inserted_id

image_from_db = image_doc.find_one({"_id": image_id})
print(image_from_db)
image_from_db["people"] = [person_id]
# image_from_db.people.append(person_id)
print(image_from_db)

image_doc.insert_one(image_from_db)