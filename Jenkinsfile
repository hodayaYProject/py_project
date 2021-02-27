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
                bat 'python backend_testing.py'
                   }
        }
//          stage('run fronted server') {
//             steps {
//                 bat 'start /min python web_app.py'
//                 bat 'python fronted_testing.py'
//                    }
//         }
//          stage('run combined_testing') {
//               steps {
//                 bat 'python combined_testing.py'
//                    }
//         }
        stage('turn off servers') {
             steps {
                bat 'python clean_environment.py'
                   }
        }
    }
}