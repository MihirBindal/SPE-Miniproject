pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'scientific-calculator'
        DOCKER_HUB_USERNAME = 'mihirbindal'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'pip install -r requirements.txt --break-system-packages'
                sh 'pytest test.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE_NAME} ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // This uses your 'dockerhubcredentials' global ID
                    docker.withRegistry('', 'dockerhubcredentials') {
                        sh "docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest"
                        sh "docker push ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest"
                    }
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                    )
                }
            }
        }
    }

    post {
        always {
            emailext (
                to: 'mihirbindal3@gmail.com',
                subject: "SPE Build Status: ${currentBuild.fullDisplayName}",
                body: "Build ${currentBuild.result} for project ${env.JOB_NAME}. Check console: ${env.BUILD_URL}"
            )
        }
    }
}