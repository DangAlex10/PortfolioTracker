pipeline {
  agent {
    docker {
      image 'python:3.11.2'
      args '-p 8000:8000'
    }
  }
  stages {
    stage('Build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'python manage.py test'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker build -t myregistry/portfolio-tracker .'
        sh 'docker push myregistry/portfolio-tracker'
      }
    }
  }
}