pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building"
                sh 'pip install -r requirements.txt'
                sh 'python3 manage.py test'
            }
        }
        stage('Test') {
            steps {
                echo "Testing"
            }
        }
  }
}
