pipeline {

    agent any 

    stages {

        stage('Ansible') {

                steps {
                    sh 'chmod +x ./scripts/*.sh'
                    sh './scripts/ansible.sh'
                }
        }

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



