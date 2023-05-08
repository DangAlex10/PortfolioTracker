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
                sh 'python3 test_file.py'
                sh 'python3 -m pytest'
            }
        }
    }
}
