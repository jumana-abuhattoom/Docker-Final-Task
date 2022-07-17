pipeline{

	agent any


	stages {

		stage('Build') {

			steps {
				sh 'docker build -t jumanaah/docker_final_task:latest .'
			}
		}

		stage('Login') {

			steps {
            withCredentials([string(credentialsId: 'jumanadocker', variable: 'passwordVariable')]) {
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
