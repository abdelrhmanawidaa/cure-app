pipeline {
    agent any

    stages {
        
        
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
