pipeline{

    agent any

    stages {

        stage('Build image & deploy swarm with updates') {
            
            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_images.sh'
                sh './scripts/build_swarm.sh'
                sh './scripts/update_swarm.sh'
            }
            
        }

    }

}