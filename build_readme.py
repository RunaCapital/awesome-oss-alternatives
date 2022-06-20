"""
This file builds README from YAML
"""
import yaml
import os
from add_company import add_new_company


def parse_all_yamls():
    arr = []
    for filename in os.listdir("submissions"):
        if filename.endswith(".yaml"):
            with open(f"submissions/{filename}", "r") as file:
                obj = yaml.load(file, yaml.Loader)
            arr.append(obj)
    return arr


def build_list():
    arr = parse_all_yamls()
    for obj in arr:
        add_new_company(**obj)


if __name__ == "__main__":
    build_list()
