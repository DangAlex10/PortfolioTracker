pipeline {
    agent any

    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t PortfolioTracker .'
            }
        }

        stage('Run tests') {
            steps {
                sh 'docker run PortfolioTracker python manage.py test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        success {
            sh 'echo "Build successful - deploying to production"'
        }
        failure {
            sh 'echo "Build failed - deployment aborted"'
        }
    }
}