pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker')
		dockerImage = ''
	}

	stages {


		stage('Build') {

			steps {
				script{
				dockerImage = sudo docker.build jumanaah/docker_final_task:latest

				}
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
