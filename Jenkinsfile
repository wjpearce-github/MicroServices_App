pipeline {

    agent any 

    stages {

        stage('Build Images') {

            steps{

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_images.sh'

            }

        }

        stage('Engage Swarm ') {

            steps{
                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_swarm.sh'

            }

        }

          stage('Update Swarm') {
            
            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/update_swarm.sh'
            }
            
        }

    }

}



