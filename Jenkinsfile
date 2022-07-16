pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker')
	}

	stages {
        stage('Login') {

			withCredentials([usernamePassword(credentialsId: 'docker', passwordVariable: 'DOCKER_REGISTRY_PWD', usernameVariable: 'DOCKER_REGISTRY_USER')]) {
            sh 'docker login -u jumanaah -p ${passwordVariable}'
        }

		}

		stage('Build') {

			steps {
				sh 'sudo docker build -t jumanaah/docker_final_task:latest .'
			}
		}

		stage('Push') {

			steps {
				sh 'sudo docker push jumanaah/docker_final_task:latest'
			}
		}
	}

	post {
		always {
			sh 'sudo docker logout'
		}
	}

}
