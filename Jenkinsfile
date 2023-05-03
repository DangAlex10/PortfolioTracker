pipeline {
    agent any

    environment {
        PATH = "$PATH:\Users\DG\Documents\GitHub\Clone\PortfolioTracker"
    }

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
                sh 'pytest'
            }
        }
  }
}
