pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Clone the GitHub repository
                git 'https://github.com/DangAlex10/PortfolioTracker.git'

                // Build the Docker image
                sh 'docker build -t portfolio_tracker .'

                // Push the Docker image to Docker Hub or another registry
                sh 'docker push admin/portfolio_tracker'
            }
        }

        stage('Deploy') {
            steps {
                // Stop and remove the existing container
                sh 'docker stop portfolio_tracker || true'
                sh 'docker rm portfolio_tracker || true'

                // Run the Docker container
                sh 'docker run -d -p 8000:8000 --name portfolio_tracker portfolio_tracker'
            }
        }
    }
}