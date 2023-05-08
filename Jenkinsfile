pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        sh 'docker build -t upbeat_mendel .'
      }
    }

    stage('Test') {
      steps {
        sh 'docker run upbeat_mendel python manage.py test'
      }
    }

    stage('Staging') {
      steps {
        sh 'docker-compose -f docker-compose.staging.yml up -d'
      }
    }

    stage('Deploy') {
      steps {
        sh 'docker-compose -f docker-compose.prod.yml up -d'
      }
    }
  }
}