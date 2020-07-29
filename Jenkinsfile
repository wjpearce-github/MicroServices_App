pipeline{

    agent any

    stages {

        stage('Building') {
            
            steps {
                
                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_images.sh'
                sh './scripts/build_swarm.sh'
                sh './scripts/update_swarm.sh'
            }
            
        }

    }

}