pipeline {

    agent any 

    stages {

        stage('Build Images') {

            steps{

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_images.sh'

            }

        }

        stage('Build ') {

            steps{

                sh './scripts/build_swarm.sh'

            }

        }

          stage('Update ') {
            
            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/update_swarm.sh'
            }
            
        }

    }

}



