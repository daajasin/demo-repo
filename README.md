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