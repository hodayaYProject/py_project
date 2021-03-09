pipeline {
    agent any
    options {buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20'))}
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('30 * * * *')])])
                }
                git 'https://github.com/hodayaYProject/py_project.git'
            }
        }
        stage('run server') {
            steps {
                bat 'start /min python rest_app.py'
                bat 'python backend_testing.py'
                bat 'start /min python web_app.py'
                bat 'python fronted_testing.py'
                bat 'python combined_testing.py'
                bat 'python clean_environment.py'
                   }
        }
    }
}