pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Get the code from GitHub
                git 'https://github.com/tenn098/your-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t my-app:latest .'
                    sh 'docker tag my-app:latest my-app:1.0' // Tag with the version number
                }
            }
        }

        stage('Run Tests') {
            steps {
                // For this example, we'll just check for a file
                sh 'test -f app.py'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Stop any existing container and remove it
                    sh 'docker stop my-app-container || true'
                    sh 'docker rm my-app-container || true'
                    // Run the new container
                    sh 'docker run -d --name my-app-container -p 5000:5000 my-app:latest'
                }
            }
        }
    }
}
