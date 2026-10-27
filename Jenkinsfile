
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Simranjeet2110/html-form-jenkins.git'
            }
        }

        stage('Test HTML Form') {
            steps {
                bat 'py -3 -m unittest test_form.py'
            }
        }
    }
}
