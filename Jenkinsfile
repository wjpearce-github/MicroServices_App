pipeline{

    agent any

    stages {

        stage('Build build image & deploy stack') {
            
            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_images.sh'
                sh './scripts/build_stack.sh'
                sh './scripts/update_stack.sh'
            }
            
        }

    }

}