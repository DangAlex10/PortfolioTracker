pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building"
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {z
            steps {
                echo "Testing"
                sh 'pip install pytest'
            }
        }
  }
}
