pipeline{

    agent any

    stages {

        stage('Build and Push') {
            
            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_images.sh'
            }
            
        }

        stage('Build Stack') {
            
            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_swarm.sh'
            }
            
        }

        stage('Update Stack') {
            
            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/update_swarm.sh'
            }
            
        }

    }

}