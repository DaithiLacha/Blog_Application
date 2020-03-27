pipeline {
    agent { dockerfile true }
        stages {
            stage('Clone Repository') {
                /* Cloning the repo to workspace */
                steps {
                    checkout scm
                }
            }
            stage ('Build Image') {
                steps {
                    sh 'docker build -t myflaskapp .'
                }
            }
            stage('Run Image') {
                steps {
                    sh 'docker run -d --name flaskapp myflaskapp'
                }
            }
            stage('Testing') {
                steps {
                    echo 'testing...'
                }
            }
        }
}
