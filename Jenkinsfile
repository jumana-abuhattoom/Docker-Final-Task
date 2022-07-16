pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker')
		dockerImage = ''
	}

	stages {

			withCredentials([usernamePassword(credentialsId: 'docker', passwordVariable: 'DOCKER_REGISTRY_PWD', usernameVariable: 'DOCKER_REGISTRY_USER')]) {
            sh 'docker login -u jumanaah -p ${passwordVariable}'
        }

		}

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
