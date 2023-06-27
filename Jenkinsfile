pipeline {
    agent any

    stages {
        stage('Unit Test') {
            steps {
                script {
                    bat 'pip install -r requirements.txt'
                    bat 'python manage.py test'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    def testImage = docker.build("abdelrhmanawidaa/graduation-app:latest")
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
