pipeline {
    agent any

    environment {
        IMAGE_NAME = 'myproject:latest'
        CONTAINER_NAME = 'myproject'
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pipenv'
                sh 'pipenv install --dev'
                sh 'pipenv run python manage.py test'
            }
        }
        stage("Deploy") {
            steps {
                sh 'docker build -t my-django-app .'
                sh 'docker tag my-django-app my-docker-registry/my-django-app:latest'
                sh 'docker login -u my-docker-registry-username -p my-docker-registry-password'
                sh 'docker push my-docker-registry/my-django-app:latest'
            }
        }
  }
}
