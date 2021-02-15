pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('30 * * * *')])])
                }
                git 'https://github.com/hodayaYProject/py_project.git'
            }
        }
        stage('run backend server') {
            steps {
                bat 'start /min python rest_app.py'
                   }
        }
    }
}