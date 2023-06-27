pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    def testImage = docker.build("abdelrhmanawidaa/graduation-app:latest")
                }
            }
        }

        stage('Unit Test') {
            steps {
                script {
                    withDockerContainer(image: 'abdelrhmanawidaa/graduation-app:latest', args: '-v $(pwd):/app') {
                        sh 'python manage.py test'
                    }
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
