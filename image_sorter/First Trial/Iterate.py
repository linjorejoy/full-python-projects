import json
import os
from GoogleImage import GoogleImage

all_json_obj = dict()


def get_json_data(path):
    with open(path) as json_file:
        json_data = json.load(json_file)
        return json_data


def iterate_through_each_json_file_in_folder(path):
    this_folder_all_json_obj = dict()
    for filename in os.listdir(path=path):
        if filename.endswith(".json"):
            file_absolute_name = os.path.join(path, filename)
            this_folder_all_json_obj[file_absolute_name] = GoogleImage.from_json(get_json_data(file_absolute_name))
    return this_folder_all_json_obj


def iterate_through_each_folder_in_google_photos_folder(path: str):
    """
    Description:
        Iterate Through the various forders in Google Photos Folder and run the iterate method
    Args:
        dir_name (str): path to the "Google Photos" folder
    Returns:
        json: return the json obj containing all the combined data of all json sub files
    """

    return path


if __name__ == "__main__":
    dir_name = input("What is the dir : ")
    with open(dir_name) as json_file:
        im = GoogleImage.from_json(json.load(json_file))
        print(im.toJSON())
    # GoogleImage.from_json(json.load(dir_name))
    # print(iterate_through_each_json_file_in_folder(dir_name))

    # with open("result.json", mode="w") as final_result:
    #     json.dump(obj=iterate_through_each_json_file_in_folder(dir_name), fp=final_result, indent=4)
