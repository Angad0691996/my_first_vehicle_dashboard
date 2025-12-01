pipeline {
    agent any

    environment {
        GIT_CREDS       = 'github-credentials'
        REPO_URL        = 'https://github.com/Angad0691996/my_first_vehicle_dashboard.git'
        BRANCH          = 'feature/docker-compose-aws'

        // Hardcoded EC2 Public IP (update this when IP changes)
        EC2_IP          = '13.201.115.73'

        FRONTEND_IMAGE  = 'angad696/react-dashboard:latest'
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
                sh "ls -la"
                echo "Repository cloned successfully."
            }
        }

        stage('Update .env with new IP') {
            steps {
                echo "Updating .env → REACT_APP_BACKEND_URL=http://${EC2_IP}:5000"

                sh """
                    sed -i "s|REACT_APP_BACKEND_URL=.*|REACT_APP_BACKEND_URL=http://${EC2_IP}:5000|g" .env
                    echo 'Updated .env:'
                    cat .env
                """
            }
        }

        stage('Build Frontend Image') {
            steps {
                echo "Building frontend with backend URL http://${EC2_IP}:5000"
                sh """
                    docker build -t ${FRONTEND_IMAGE} \
                        --build-arg REACT_APP_BACKEND_URL=http://${EC2_IP}:5000 .
                """
            }
        }
    }

    post {
        success {
            echo "🎉 Frontend image built successfully AND .env updated."
        }
        failure {
            echo "❌ Pipeline failed — check logs."
        }
    }
}
