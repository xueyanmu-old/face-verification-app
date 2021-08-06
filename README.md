# deep-face-api overview
Full stack data-science project
includes docker container for a face verification (and emotion, age, race)
model, and instructions for how to deploy on heroku

the heroku branch will help compose the heroku aspect of the project //
the master branch is the part that contains the entire DS model 
dockerfile may require additional command "--fix-missing" in the installs

## Medium
Story about building the web application and deploying it.

## How to actually deploy it on heroku  without breaking everything
1. master branch: to build everything, use command docker-compose up --build
2. heroku branch: to build everything, use command docker-compose up --build
   you may need to deploy repo on heroku.com for it to show up on the website though
3. check out the website deepface-poatek.herokuapp.com/docs to see if it works
4. debug ^^ errors using heroku logs --tail -a deepface-poatek

## next steps: 
1. possibly try to make heroku deployment of project work on another computer 
2. if fails, find another web server deployer for this project (AWS, etc)

## helpful advice
-all dockerfiles should be configured correctly, so dont change them yet
-folders may have redundant files, but they work currently- key is to find which 
     exact files are causing the error (might happen in a different directory than expected)
-use to_RGB for all photos, and enforce-detection=False in each Deepface model call
-autocrlf error requires notepad++ installation, and then replace all \r\n with \n in repo


The below things are dumb as fuck but they kind of work
### [part1](https://medium.com/@sdamoosavi/deploy-deepface-model-fastapi-develop-2e33374db6f2)
### [part2](https://medium.com/@sdamoosavi/deploy-deepface-model-fastapi-heroku-deployment-8e007e72c455)
