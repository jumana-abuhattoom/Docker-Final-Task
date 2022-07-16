pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker')
	}

	stages {
        stage('Login') {

			steps {
				sh 'sudo echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
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