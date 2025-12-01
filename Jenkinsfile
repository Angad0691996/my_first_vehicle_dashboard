pipeline {
    agent any

    environment {
        GIT_CREDS       = 'github-credentials'
        REPO_URL        = 'https://github.com/Angad0691996/my_first_vehicle_dashboard.git'
        BRANCH          = 'feature/docker-compose-aws'

        EC2_IP          = '13.201.115.73'

        FRONTEND_IMAGE  = 'angad696/react-dashboard:latest'
        BACKEND_IMAGE   = 'angad696/backend-subscriber:latest'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git(
                    branch: "${BRANCH}",
                    credentialsId: "${GIT_CREDS}",
                    url: "${REPO_URL}"
                )
            }
        }

        stage('Update .env with new IP') {
            steps {
                sh """
                    sed -i "s|REACT_APP_BACKEND_URL=.*|REACT_APP_BACKEND_URL=http://${EC2_IP}:5000|g" .env
                """
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh """
                    docker build -t ${FRONTEND_IMAGE} \
                        --build-arg REACT_APP_BACKEND_URL=http://${EC2_IP}:5000 .
                """
            }
        }

        stage('Push Frontend Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                    sh """
                        echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin
                        docker push ${FRONTEND_IMAGE}
                    """
                }
            }
        }

        stage('Build Backend Image') {
            steps {
                sh """
                    docker build -t ${BACKEND_IMAGE} ./backend
                """
            }
        }

        stage('Push Backend Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                    sh """
                        echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin
                        docker push ${BACKEND_IMAGE}
                    """
                }
            }
        }

        stage('Deploy Locally (Same EC2)') {
            steps {
                sh """
                    cd /home/ubuntu/vehicle-dashboard-app &&
                    docker compose -f docker-compose.prod.yml down || true &&
                    docker compose -f docker-compose.prod.yml pull &&
                    docker compose -f docker-compose.prod.yml up -d
                """
            }
        }
    }

    post {
        success {
            echo "🎉 Deployment Complete!"
        }
        failure {
            echo "❌ Pipeline Failed"
        }
    }
}
