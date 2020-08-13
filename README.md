# SFIA2 Project
William Pearce


### App Link: Manager
http://35.214.71.19/

### App Link: Worker 
http://35.214.29.79/

### Trello:
https://trello.com/b/TBMVwmEY/generator

### Documentation Contents
*	Brief
*	 Minimum Requirements 
*	Application Summary 
*	Planning 
*	 MoSCow 
*	 Trello Boards 
*	 Persistent Data
*	Tech Stack 
*	CI Pipeline
*	Design
*	 Front-End Design 
*	Risk Assessment
*	Reflection 
*	Bugs & Current Issues


### Brief
Create an application utilising service-oriented architecture comprising of four micro-services working together. Using a containerisation tool, deploying the entire application through a continuous integration server and ultimately pushing into a correctly configured production environment.  

### Minimum Requirements
*	Documentation of the source code, planning stage, risk assessment and project tracking.
*	Full integration with a VCS (Version Control System). 
*	The use of CI Server: Jenkins 
*	Taking the application and containerising it with Docker making using of Docker Swarm as the orchestration tool. 
*	Hosted on a google cloud platform Linux Virtual machine
*	For user access, implementation of a reverse proxy: NGINX
*	The configuration of a production environment created using Ansible Playbook



### Functionality 

The application I have created generates random names to use in RPG games as the main character. As stated in the project brief, two versions of the application exist: One simple black and white version and one with extra exclamation marks after the title. 
The application is comprised of four different micro-services written in Python each relying on the other to generate the final result:
* Service one: Is a basic Flask Application with a HTML template. 
* Service Two: Contains a function with a list of eight possible choices for a first name, one of which will be selected at random.
* Service Three: Contains a function with a list of eight possible choices for the last name, one of which will be selected at random.
* Service Four: Receives the outputs from service two and three, concatenates them together and pushes the result back to service one to be displayed to the user.

<p align="center">
    <img width="750" height="400" src="https://i.imgur.com/30wx6Os.png"
    </p>



### Trello 

Trello : Splitting up Must Have, Should Have and Could Have for functionality. Followed by the breaking down of my sprints/Todo


<p align="center">
    <img width="750" height="400" src="https://i.imgur.com/JXpBKNG.png"
    </p>


### Data: ERD Diagram 

Hosted on a Google Cloud MySQL Server, similar to the Crud application I created a database and table to hold the generated names: Setting the id to autoincrement  as the primary key. 

<p align="center">
    <img width="600" height="300" src="https://i.imgur.com/JxYtxKC.png"
    </p>


### Feature Branch Model 

Here you can see my project hasfully implemented version control using Git and GitHub, making you use of the feature branch model. 

<p align="center">
    <img width="600" height="300" src="https://i.imgur.com/jXkh7KN.png"
    </p>
    
<p align="center">
    <img width="475" height="300" src="https://i.imgur.com/TReNIMl.png"
    </p>

### Tech Stack

*	Trello for Project tracking and management.
*	Google Cloud Platform for Hosting SQL Server.
*	Python for app development with HTML for front-end webpages.
*	Flask for Web App Framework.
*	Git & and GitHub for version control
*	NGINX as a reverse proxy, for user access.
*	Jenkins for the CI Server
*	Docker used within VCS for containerising services and overall application. Additionally, making use of Docker-Compose for efficiency   
*	Finally, Ansible was used with the Ansible playbook file to configure a working environment in which the app could successfully run.  



### CI Pipeline 

<p align="center">
    <img width="650" height="600" src="https://i.imgur.com/0QpD811.png"
    </p>
    
As with any DevOps focused project an informative, clear CI pipeline was an integral part once the application design had been completed. 
The CI Pipeline in this project centred around the following technologies and is displayed below.

*	The source code is created in Python, Flask and HTML.
*	When changes are made, they are pushed pushing up to my ‘Second_App’ repository on GitHub.
*	Referencing Trello and deciding the next task in the app development.
*	Jenkins has been configured to look for changes on the GitHub repository as and when they are pushed up from Visual Studio Code.
*	Once a change is detected, Jenkins has been configured to automatically update and replace the current build with the new version hosted on my repository 
    – For a successful build to take place here Jenkins will run the Ansible playbook and Docker Compose to compile a new image. 
*	These changes are hosted on Docker-Hub (Holding the new images) and an Ubuntu 18.04 cloud virtual machine where the app is ruining. 

### DockerHub  

Wehre the images are updataed


<p align="center">
    <img width="650" height="600" src="https://i.imgur.com/jmfP3zg.png"
    </p>

    

### Jenkins Pipeline   

Runnning the scripts and presenting error logs or successful builds


<p align="center">
    <img width="650" height="500" src="https://i.imgur.com/9WQl5MI.png"
    </p>


<p align="center">
    <img width="550" height="300" src="https://i.imgur.com/cStssmk.png"
    </p>

### V1.0 Front-end Design

The application had two implementations:
One basic one that randomly generated an RPG Name and a second that had made use of persistent data via MySQL. 
This data is then passed back to be displayed for the user to access previous names generated. 


<p align="center">
    <img width="325" height="275" src="https://i.imgur.com/LDHnkpH.png"
    </p>



<p align="center">
    <img width="400" height="400" src="https://i.imgur.com/HMj1KYn.png"
    </p>


### Risk Assessment 

<p align="center">
    <img width="750" height="600" src="https://i.imgur.com/IcFv5MR.png"
    </p>

### Retrospective & future improvements 

Originally, I had planned for the app to take some sort of user input and for the result of the generator to be based on what the user input was.  In terms of configurations, I found the hardest part was creating the scripts for my Jenkinsfile to run. Again, similar to the last project was somewhat comfortable with using python and found that my knowledge has increased since week one. Possibly in the future even adding some Javascript for extended functionality. Additionally, adding even more automation if I decided to add in more user features and aesthetics. 

### Issues 

At the moment I am dealing with an issue where even if entries are deleted the auto-incremented feature of the ID in the SQL Table does not reset to 0 and will instead present the first entry at whatever the entry last was: Entry 0 becomes entry 22. 



### Author

##### William Pearce
