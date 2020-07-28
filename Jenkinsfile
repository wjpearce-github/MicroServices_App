pipeline {
    agent any 
    stages {
        stage('Build: Docker') {  
            steps {
                sh "bash ./jenkins/build.sh"
            }

        stage('Deploy: Ansible') { 
            steps {
                sh "bash ./jenkins/deploy.sh"
            }
        }
    }