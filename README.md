# Migration Script for Docker Registry
This script will help you migrate all the tags from a docker registry to registry. 
So for example if you want to migrate all the images and tags from MYREPO1/ to MYREPO2/ this script does it for you.

# BEFORE YOU START
1. You must set the env variable **DOCKER_USERNAME**, **DOCKER_PASSWORD** and **DOCKER_EMAIL** (N.B. Your username should have permission to pull images from the old repo and push image to new repo.)
2. You must create the new REPO_NAME Manually in the new docker registry if needed.
3. You must specify the list of the repo to be moved in the *repolist.txt* file
4. You must set the correct value as for *OLD_TEAM* and *NEW_TEAM* variable.

So for example lets suppose you have 3 repos. 
* **notcool/myubuntu**
* **notcool/myservice**
* **notcool/myserver**

Each of those images have many tags...and you want to move all the images and tag to this new repo:
* **supercool/myubuntu**
* **supercool/myservice**
* **supercool/myserver**

Then what you need to do is the following (beside setting the env variable to your docker username and passwd.)
1. Set the Env variable to your correct Docker username and password as in explained above
2. in the repolist.txt place this lines 
*<p>
notcool/myubuntu <br>
notcool/myservice <br>
notcool/myserver</p>*

3. in the main.py Set *OLD_TEAM="notcool"* and *NEW_TEAM="supercool"*
4. in supercool registry, create the three repo **myubuntu**, **myservice** and **myserver**
5. You can now run the script... After finished you will have ALL your old images and TAGS in the new repo. 

# INFO
By LordEvron
Glory to the great Evron Empire!

