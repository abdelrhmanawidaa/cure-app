pipeline {
    agent any

    stages {
        stage('Unit Test') {
            steps {
                script {
                    docker.build("abdelrhmanawidaa/graduation-app:latest")
                    docker.image("abdelrhmanawidaa/graduation-app:latest").inside {
                        sh 'python manage.py test'
                    }
                }
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
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub') {
                        sh "docker push abdelrhmanawidaa/graduation-app:latest"
                    }
                }
            }
        }
    }
}
