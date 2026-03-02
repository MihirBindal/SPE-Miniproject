pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'scientific-calculator'
        DOCKER_HUB_USERNAME = 'mihirbindal'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // This tells Jenkins to pull the code using the GitHub credentials you will select in the UI
                checkout scm
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Installs pytest and tests your calculator logic
                sh '''
                    python3 -m venv myenv
                    ./myenv/bin/pip install pytest
                    ./myenv/bin/pytest test_calculator.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                // Builds the image using your Dockerfile
                sh "docker build -t ${DOCKER_IMAGE_NAME} ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Jenkins uses your newly set up credentials to log in and push
                    docker.withRegistry('', 'dockerhubcredentials') {
                        sh "docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest"
                        sh "docker push ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest"
                    }
                }
            }
        }
    }
}