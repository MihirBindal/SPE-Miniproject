pipeline {
    agent any
    
    environment {
        DEVELOPER_EMAIL = 'mihirbindal3@gmail.com' // UPDATE THIS TO YOUR EMAIL!
    }

    // TA REQUIREMENT: Poll SCM as a backup to the webhook
    triggers {
        pollSCM('* * * * *') 
    }

    stages {
        stage('Clone Git') {
            steps {
                // checkout scm automatically uses the repo configured in the Jenkins job
                checkout scm
            }
        }

        stage('Install Dependencies & Test') {
            steps {
                sh 'pip install -r requirements.txt'
                // TA REQUIREMENT: Generate an XML test report
                sh 'pytest test.py --junitxml=test-results.xml'
            }
            post {
                always {
                    // Tell Jenkins to display the test results graph on the dashboard
                    junit 'test-results.xml' 
                }
            }
        }
    }
    
    // TA REQUIREMENT: Email Notifications
    post {
        success {
            mail to: "${DEVELOPER_EMAIL}",
                 subject: "SUCCESS: Jenkins Webhook Test #${env.BUILD_NUMBER}",
                 body: "Great job! The GitHub Webhook, Ngrok, and Email plumbing work perfectly!"
        }
        failure {
            mail to: "${DEVELOPER_EMAIL}",
                 subject: "FAILED: Jenkins Build #${env.BUILD_NUMBER}",
                 body: "Alert! The pipeline failed. Please check the Jenkins console logs."
        }
        always {
            // Clean up the workspace to save hard drive space
            cleanWs()
        }
    }
}
