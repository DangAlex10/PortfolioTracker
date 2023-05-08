pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        sh 'docker build -t your-image-name .'
      }
    }

    stage('Test') {
      steps {
        sh 'docker run your-image-name python manage.py test'
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