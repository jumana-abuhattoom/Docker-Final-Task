pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker build -t jumanaah/docker_final_task:latest .'
			}
		}

		stage('Login') {

			steps {
            withCredentials([string(credentialsId: 'docker', , passwordVariable: 'DOCKER_REGISTRY_PWD')]) {
      sh "docker login -u jumanaah -p ${passwordVariable}"
            }			}
		}

		stage('Push') {

			steps {
				sh 'docker push jumanaah/docker_final_task:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
