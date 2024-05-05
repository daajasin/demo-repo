# This is going to be a great year! 

There is more to come!


There will be a time when things work like magic...
How are you channelling your thughts and emotions...
How are you raising your frequency nd vibration..


##1 Scaffold

the folder with the code will have the following files in there
MakeFile
requirements.txt
source
test
DockerFile

create a python Environment
python3 - venv ~/.venv
virtualenv ~/.venv

edit the bashrc file and add the source ato the bottom of the page
source ~/.venv/bin/activate
everytime you open a terminal it open with the virtual env. so all the packages are in there

2. Create empty files
makefile
requirements.txt
main.py
Dockerfile
mylib/__init__.py

3. populate 'Makefile' so you can put these steps into the makefile
you can run on the command line by typing make all

commit all your code to your repo...

3 . adding to the requirements file
wikipedia using wikipedia tool
pytest      we are going to need to test our code
pytest-cov  coverage tool- which will give us how many lines of code are covered
pylint      linting tool
black       formatting tool
fire        you can uuse this to map a function into a command line tool

put all these into a makefile

4.  inside the make file put the following commands 
    
    pip install --upgrade pip &&\
		pip install -r requirements.txt

then on the command line run make install, which then install all the packages required for the build

5. Then we run a pip freeze | less
this will show all the packages with their version numbers and then we can then append those to the packages into the requirements.txt file

ensuring your versions always run is a big win

6. Go to github actions on the main github menu and setup 
  See github actions for the actions in there you want to make to the project
edit the github actions file and then push it to the commit and then it runs the build file.

This is from the status badge
[![Python application test with GitHub Actions](https://github.com/daajasin/demo-repo/actions/workflows/Devops.yml/badge.svg)](https://github.com/daajasin/demo-repo/actions/workflows/Devops.yml)


7. COntinue to follow the Makefile.
### Format the code

add the following lines under the #format code
black *.py mylib/*.py

8. git commit, pull and push all updates to the file.
check build process in the github actions tab to see how the build is going to make sure nothing is broken.

9. Add linting in to the Makefile
add this line into the file
pylint --disable=R,C *.py mylib/*.py

this can catch code bugs not necessarily 

edit your devops.yml file under the #make lint

this can show up in your build actions step showing the warning it will generate from the command to lint if there is a problemm with it.
If there is an error you can screen shot it and add it to this file as a record.

10. Go to the next step of the makefile
add a build step and add a container
#build container

11. Pytest in the makefile
python -m pytest -vv cov=mylib test_logic.py

