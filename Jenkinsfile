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
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub') {
                        sh "docker push abdelrhmanawidaa/graduation-app:latest"
                    }
                }
            }
        }
    }
}
