pipeline {

    agent any

    stages {

        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Check Django') {
            steps {
                bat 'venv\\Scripts\\python manage.py check'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\python manage.py test'
            }
        }

        stage('Collect Static') {
            steps {
                bat 'venv\\Scripts\\python manage.py collectstatic --noinput'
            }
        }

    }

}
