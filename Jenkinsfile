pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker')
	}

	stages {


		stage('Build') {

			steps {
				sh 'dockerImage = sudo docker.build -t jumanaah/docker_final_task:latest .'
			}
		}
        stage('Login') {

			steps {
				script{
					docker.withRegistry('', 'jumanaah/docker_final_task'){
					dockerImage.push()
					}
				}
			}
		}

	}

	post {
		always {
			sh 'sudo docker logout'
		}
	}

}
