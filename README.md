# basic_automation

#################################################
#Author : Deepak Rai                            #
#Copyright (c) 2022                             #
#Contact : deepak.rai.linux@gmail.com           #
#################################################

# In this branch you will find steps to install Jenkins

Definition : Jenkins is a powerfull open source JAVA based application that allows continuous integration and continuous delivery.

# Installation guide
Pre-requisite:
    1. JDK 1.5 or above
    2. Memory 2GB recommended

Step 1: Install Java on your ubuntu system
Run commands: 
    sudo apt install default-jre
    sudo apt install default-jdk

Step 2: Downloads the LTS (long term supported) Jenkins war file (in our case we are using version 2.346.1 [June, 2022] LTS)
Run commands:
    wget https://get.jenkins.io/war-stable/2.346.1/jenkins.war

# Note: If you want to install other LTS versions of Jenkins, please go to https://get.jenkins.io/war-stable/ and select the version of your choice.

Step 3: Installing Jenkins by running the .war file
Run commands:
    java -jar jenkins.war
Output: on succesfull compilation you will below output on your terminal.
    [ 2022-11-22 17:48:53.165+0000 [id=23]	INFO	hudson.lifecycle.Lifecycle#onReady: Jenkins is fully up and running ]

Step 4: Access the jenkins GUI. Using your web browser go to the ## localhost:8080 ## 