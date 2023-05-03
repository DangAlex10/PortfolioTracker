pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building"
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo "Testing"
                sh 'pip install pytest'
                sh '/Users/DG/Documents/GitHub/Clone/PortfolioTracker'
                sh 'pytest'
            }
        }
  }
}
