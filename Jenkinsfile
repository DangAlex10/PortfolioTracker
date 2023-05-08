pipeline {
  agent any
  stages {
    stage('Build and Test') {
      agent {
        docker {
          image 'python:3.11.2'
          args '-p 8000:8000'
        }
      }
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python manage.py test'
      }
    }
    stage('Deploy') {
      when {
        branch 'master'
      }
      steps {
        sh './deploy.sh'
      }
    }
  }
}