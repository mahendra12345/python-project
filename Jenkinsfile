pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/username/project.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                python manage.py migrate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                python manage.py test
                '''
            }
        }

        stage('Collect Static') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                python manage.py collectstatic --noinput
                '''
            }
        }

    }

}