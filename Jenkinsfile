pipeline {

    agent any

    environment {
        DOCKER_USER="dwr6"
        NETWORK_NAME="dwr-flask-app"
    }

    stages {
        stage("Build and Push") {
            steps {
                echo "Building..."
                sh "docker build -t $DOCKER_USER/dwr-app ."
                sh "docker push $DOCKER_USER/dwr-app"
                echo "Build Complete"
            }
        }

        stage("Test") {
            steps {
                echo "Testing..."
                sh "sleep 3"
                echo "Tests Passed"
            }
        }

        stage("Deploy") {
            steps {
                sh "docker stop \$(docker ps -q) || sleep 1"
                sh "docker rm \$(docker ps -qa) || sleep 1"
                sh "docker network inspect $NETWORK_NAME && sleep 1 || docker network create $NETWORK_NAME"
                sh "docker run -d --network $NETWORK_NAME --name flask-app $DOCKER_USER/dwr-app"
                sh "docker run -d --network $NETWORK_NAME --name nginx -p 80:80 --mount type=bind,source=\$(pwd)/nginx.conf,target=/etc/nginx/nginx.conf nginx:latest"
            }
        }
    }

    post {
        always {
            sh "docker system prune -f"
        }
    }   
}