pipeline {
    agent any

    stages {
        stage('Unit Test') {
            steps {
                script {
                    def testImage = docker.build("abdelrhmanawidaa/graduation-app:latest")
                    testImage.inside {
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
