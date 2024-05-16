#### *NLP1 (Natural Language Processing) Play/exmaples*
#### *Installation and runnining instructions.* 
###### IDE used = Virtual Studio, OP = Windows 11, Language = Python
###### 3.1 Clone repository with command below. Must have Git & Github installed.
###### git clone https://github.com/CrypticDG/NLP1
###### 3.2 Move to project root folder
###### cd nlp1
###### 3.3 Create a virtual environment
###### py -m pip install virtualenv (Instal virtual environment)
###### virtualenv 'env1' - (create virtual environment and give it a name)
###### env1\scripts\activate (activate virtual environment that stores all your modules for your project)
###### 3.4 Install requirements.txt, (this will install all the modules you will need to run this app)
###### py -m pip install -r requirements.txt
###### 3.5 run youre app  (not containerized before deploy, see Docker section 3.6)
###### run terminal
###### 3.6 Docker(Have Docker Hub and Docker desktop installed)
###### Run in terminal: docker build -t nlp1 .    
###### Run in terminal: docker run nlp1         

