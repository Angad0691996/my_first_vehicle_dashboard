pipeline {
    agent any

    environment {
        GIT_CREDS = 'github-credentials'
        REPO_URL  = 'https://github.com/Angad0691996/my_first_vehicle_dashboard.git'
        BRANCH    = 'feature/docker-compose-aws'
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo "Cloning branch: ${BRANCH}"
                git(
                    branch: "${BRANCH}",
                    credentialsId: "${GIT_CREDS}",
                    url: "${REPO_URL}"
                )
            }
        }

        stage('Verify Files') {
            steps {
                sh 'ls -la'
                echo "Repository cloned successfully."
            }
        }

    }
}
