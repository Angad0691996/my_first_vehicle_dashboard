pipeline {
    agent any

    environment {
        GIT_CREDS     = 'github-credentials'
        DOCKER_CREDS  = 'docker-hub-credentials'
        EC2_KEY       = 'jenkins-2 ec2 key'
        REPO_URL      = 'https://github.com/Angad0691996/my_first_vehicle_dashboard.git'
        BRANCH        = 'feature/docker-compose-aws'
        APP_DIR       = '/home/ubuntu/vehicle-dashboard-app'
    }

    stages {

        /* -----------------------------
           1. Clone Repository
        ------------------------------ */
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

        /* -----------------------------
           2. Detect EC2 Public IP (NEW)
        ------------------------------ */
        stage('Detect EC2 Public IP') {
            steps {
                script {
                    def ip = sh(
                        script: "curl -s ifconfig.me",
                        returnStdout: true
                    ).trim()

                    echo "Detected EC2 Public IP: ${ip}"
                    env.EC2_IP = ip
                }
            }
        }

        /* -----------------------------
           3. Update .env with backend URL
        ------------------------------ */
        stage('Update .env with Backend URL') {
            steps {
                script {
                    sh """
                    sed -i 's|REACT_APP_BACKEND_URL=.*|REACT_APP_BACKEND_URL=http://${EC2_IP}:5000|g' .env
                    echo '.env updated with new backend URL'
                    """
                }
            }
        }

        /* -----------------------------
           4. Build Frontend Docker Image
        ------------------------------ */
        stage('Build Frontend Image') {
            steps {
                script {
                    sh """
                    docker build -t angad696/react-dashboard:latest \
                      --build-arg REACT_APP_BACKEND_URL=http://${EC2_IP}:5000 .
                    """
                }
            }
        }

        /* -----------------------------
           5. Push Frontend Image
        ------------------------------ */
        stage('Push Frontend Image') {
            steps {
                script {
                    withCredentials([usernamePassword(
                        credentialsId: "${DOCKER_CREDS}",
                        usernameVariable: 'USER',
                        passwordVariable: 'PASS'
                    )]) {
                        sh """
                        echo "$PASS" | docker login -u "$USER" --password-stdin
                        docker push angad696/react-dashboard:latest
                        """
                    }
                }
            }
        }

        /* -----------------------------
           6. Deploy on EC2
        ------------------------------ */
        stage('Deploy to EC2') {
            steps {
                sshagent([EC2_KEY]) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@${EC2_IP} '
                        mkdir -p ${APP_DIR}
                        cd ${APP_DIR}

                        # Copy fresh repo from Jenkins workspace
                        rm -rf ${APP_DIR}/*
                    '
                    
                    # Sync repo contents to EC2 app folder
                    rsync -avz --delete ./ ubuntu@${EC2_IP}:${APP_DIR}

                    ssh -o StrictHostKeyChecking=no ubuntu@${EC2_IP} '
                        cd ${APP_DIR}
                        docker compose -f docker-compose.prod.yml down || true
                        docker compose -f docker-compose.prod.yml pull
                        docker compose -f docker-compose.prod.yml up -d
                    '
                    """
                }
            }
        }
    }

    post {
        success {
            echo "🎉 Pipeline Successful"
        }
        failure {
            echo "❌ Pipeline Failed"
        }
    }
}
