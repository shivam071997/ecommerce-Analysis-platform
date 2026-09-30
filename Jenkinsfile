pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Backend Build') {
            steps {
                sh '''
                    docker build \
                    -t ecommerce-backend:${BUILD_NUMBER} \
                    ./backend
                '''
            }
        }

        stage('Frontend Build') {
            steps {
                sh '''
                    docker build \
                    -t ecommerce-frontend:${BUILD_NUMBER} \
                    ./frontend
                '''
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    docker run --rm \
                    ecommerce-backend:${BUILD_NUMBER} \
                    python -c "import flask; print('Backend dependencies OK')"
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage ready'
            }
        }
    }
}
