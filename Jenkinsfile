pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/abdelrhmanawidaa/grad-proj'
            }
        }
        
        stage('Build') {
            steps {
                script {
                    docker.build("abdelrhmanawidaa/graduation-app:latest")
                }
            }
        }
        
        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
