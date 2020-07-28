pipeline{

    agent any

    stages {

        stage('Building') {
            
            steps {
                
                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/pull_images.sh'
            }
            
        }

    }

}