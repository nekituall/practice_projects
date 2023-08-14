import re
import subprocess
import sys

import docker

client = docker.from_env()
lst = client.images.list(all=True)


def sorting(item):
    return item.attrs["Created"]


def clear_duplicate(items, arg):
    """clear images except first one in a list
    first supposed to be the newest image
    USE CAUTION!
    """
    if len(items) > 1:
        for item in items[1:]:
            clear_image(item, arg)


def clear_image(item, arg):
    """clear exactly one image with a tag
    PASSED!
    """
    subprocess.run(args=f"{arg} docker image rm --force {item}", shell=True)


def find_duplicates(items: list, pattern: str):
    """find duplicates of image within items searching for pattern"""
    duplicates = []
    # print("Pattern:", pattern)
    for item in sorted(items, key=sorting, reverse=True):
        if len(item.tags) > 0:
            m = re.search(f"^{pattern}", item.tags[0])
            if m is not None:
                # print(m.string)
                duplicates.append(m.string)
    return duplicates


def main(arg=""):
    for i in sorted(lst, key=sorting, reverse=True):
        if len(i.tags) > 0:
            image = i.tags[0].split(":")
            repo, tag = image[0], image[1]
            if "events/backend" in repo:
                if "dev" in tag:
                    reg = repo + ":.*" + str(tag.split("-")[1])
                    image_set = find_duplicates(lst, reg)
                    clear_duplicate(image_set, arg)
                elif "php" in tag:
                    reg = repo + ":.*" + str(tag.split("-")[1])
                    image_set = find_duplicates(lst, reg)
                    clear_duplicate(image_set, arg)
                else:
                    reg = repo + ":" + "((?!php|dev).)*$"
                    image_set = find_duplicates(lst, reg)
                    clear_duplicate(image_set, arg)
            else:
                reg = repo + ":" + "((?!php|dev).)*$"
                image_set = find_duplicates(lst, reg)
                clear_duplicate(image_set, arg)


if __name__ == "__main__":
    if sys.argv[1:]:
        arg = "echo"
        main(arg)
    else:
        print("else")
        main()
