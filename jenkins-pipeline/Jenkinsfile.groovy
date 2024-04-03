pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'tot0ro/test_builder_gcc'
                    reuseNode true
                }
            }
            steps {
                echo "build"
                sh "gcc -o main.out main.c"
            }
        }
        stage('Test') {
            steps {
                echo "test"
                sh "./main.out"
                sh "pwd"
            }
        }
        stage('Deploy') {
            steps {
                echo "deploy"
                sh "git show -s --format=%H/%an/%ae/%ai/\\\"%s\\\"/\\\"%D\\\"/%b"
            }
        }
    }
    post {
      always {
        echo 'post1'
      }
      failure {
        echo 'fail!'
      }
    }
}
