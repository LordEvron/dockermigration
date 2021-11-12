__author__ = 'LordEvron'
'''/////////////////////////////////////////////////////////////////////////////
//  name      dockermigration.py
//
//  brief     This script will help you with docker migration 
//
//  author    Lord Evron 
//
//  date      05.10.2020
//
//  Note: tested with python 3.8
//
//h-////////////////////////////////////////////////////////////////////////// '''

import requests
import docker
import os

########### CONFIG ###################
OLD_TEAM = "myoldteam"
NEW_TEAM = "mynewteam"
################ DO NOT FORGET TO SET THE ENV VARIABLES FOR DOCKER LOGIN #####################


################################################
USERNAME = os.environ.get("DOCKER_USERNAME")
PASSWORD = os.environ.get("DOCKER_PASSWORD")
EMAIL = os.environ.get("DOCKER_EMAIL")


def migrateimages():
    file1 = open('repolist.txt', 'r')
    repos = file1.readlines()
    print(f"Repo List loaded.Found {len(repos)} repos..Connecting to docker")
    client = docker.from_env()
    client.login(username=USERNAME, password=PASSWORD, email=EMAIL, registry='https://index.docker.io/v1/')
    for from_repo in repos:
        from_repo = from_repo.strip()
        to_repo = from_repo.replace(OLD_TEAM, NEW_TEAM)

        print(f"working with repo {from_repo} . moving to--> {to_repo}.. fetching tags")
        r = requests.get(f"https://registry.hub.docker.com/v1/repositories/{from_repo}/tags")
        r = r.json()
        tag_list=[]
        for i in r:
            tag_list.append(i["name"])
        print(f"Listing TAG founds for {from_repo}:")
        print(tag_list)

        for tag in tag_list:
            old_image = from_repo+":"+tag
            new_image = to_repo+":"+tag
            print(f"moving {old_image} TO--> {new_image} ... Pulling..")
            client.images.pull(old_image)
            client.images.get(old_image).tag(new_image)
            print(f"moving {old_image} TO--> {new_image} ... Pushing..")
            client.images.push(new_image)
            client.images.remove(old_image)
            client.images.remove(new_image)
            print("Image successfully migrated!")

        print(f"Repo {from_repo} Migrated!")

if __name__ == '__main__':
    migrateimages()
    print("Done")
