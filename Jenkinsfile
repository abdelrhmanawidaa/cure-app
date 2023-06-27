pipeline {
    agent any

    stages {
        stage('Unit Test') {
            steps {
                script {
                    def testImage = docker.build("abdelrhmanawidaa/graduation-app:latest")
                    bat 'docker run -t -v %WORKSPACE%:/app abdelrhmanawidaa/graduation-app:latest python manage.py test'
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
