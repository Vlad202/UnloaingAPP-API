
pipeline{
	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub')
	}

	stages {
		stage('Build') {
			steps {
				sh 'docker build -t jenneron/unloading-app:latest .'
			}
		}

		stage('Login to Docker Hub') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {
			steps {
				sh 'docker push jenneron/unloading-app:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}
}
