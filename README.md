#### *NLP1 (Natural Language Processing) Play/exmaples*
##### Python spacy module is imported, which provides natural language 
###### processing capabilities. 1. Word objects are defined and their similarity is calculated using both sm & md language models. 
###### 2. The Code demonstrates how to work with word vectors. It creates word objects for the words "human," "alien," "shoe," and "sock" 
###### and measures the similarity between all pairs of words. 
###### 3. The third set of code compares the similarity between a given sentence
###### and a list of other sentences. It uses the loaded model to
###### calculate the similarity and prints the sentences along with
###### their respective similarity scores.

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
###### 3.5 run you app  (not containerized before deploy, see Docker section 3.6)
###### run terminal
###### 3.6 Docker(Have Docker Hub and Docker desktop installed)
###### Run in terminal: docker build -t nlp1 .    
###### Run in terminal: docker run nlp1         

