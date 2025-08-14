pipeline {
  agent any

  options {
    timestamps()
    ansiColor('xterm')
    buildDiscarder(logRotator(numToKeepStr: '20'))
    disableConcurrentBuilds()
    timeout(time: 30, unit: 'MINUTES')
  }

  environment {
    // Adjust Python version as needed; if not using Docker, ensure python3/pip is installed on agent
    PYTHON_VERSION = '3.11'
    VENV_DIR = '.venv'
    PIP_CACHE_DIR = "${WORKSPACE}/.cache/pip"
    PYTEST_ADDOPTS = '--maxfail=1 -q'
  }

  triggers {
    // Uncomment if you want periodic builds
    // pollSCM('@daily')
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
        script {
          sh 'python3 --version || true'
          sh 'pip3 --version || true'
        }
      }
    }

    stage('Setup Python env') {
      steps {
        sh '''
          set -e
          mkdir -p .cache/pip .cache/pytest
          python3 -m venv "${VENV_DIR}" || python -m venv "${VENV_DIR}"
          . "${VENV_DIR}/bin/activate"
          python -m pip install --upgrade pip wheel
          if [ -f requirements.txt ]; then
            PIP_CACHE_DIR="${PIP_CACHE_DIR}" pip install -r requirements.txt
          else
            echo "requirements.txt not found, installing pytest only"
            PIP_CACHE_DIR="${PIP_CACHE_DIR}" pip install pytest pytest-html
          fi
        '''
      }
    }

    stage('Lint (optional)') {
      when { expression { return fileExists('requirements.txt') } }
      steps {
        sh '''
          set -e
          . "${VENV_DIR}/bin/activate"
          # Add flake8/ruff if you want linting; these are optional
          if grep -qiE 'flake8|ruff' requirements.txt; then
            echo "Running linters..."
            if python -c "import importlib; importlib.import_module('flake8')" 2>/dev/null; then
              flake8 || true
            fi
            if python -c "import importlib; importlib.import_module('ruff')" 2>/dev/null; then
              ruff check . || true
            fi
          else
            echo "No linter declared in requirements.txt; skipping."
          fi
        '''
      }
    }

    stage('Unit Tests') {
      steps {
        sh '''
          set -e
          . "${VENV_DIR}/bin/activate"
          mkdir -p reports htmlcov .cache/pytest
          # Pytest with JUnit + HTML reports
          pytest -q \
            --junitxml=reports/junit.xml \
            --html=reports/pytest-report.html --self-contained-html \
            || TEST_STATUS=$?
          # Ensure we exit with pytest status so Jenkins knows the build result
          exit ${TEST_STATUS:-0}
        '''
      }
      post {
        always {
          junit testResults: 'reports/junit.xml', allowEmptyResults: true
          archiveArtifacts artifacts: 'reports/**', fingerprint: true, allowEmptyArchive: true
        }
      }
    }

    stage('Build Docker image (optional)') {
      when {
        allOf {
          expression { return fileExists('Dockerfile') }
          expression { return env.BRANCH_NAME == 'main' || env.CHANGE_TARGET == 'main' }
        }
      }
      steps {
        sh '''
          set -e
          IMAGE="pytest-api:${BUILD_NUMBER}"
          echo "Building ${IMAGE}"
          docker build -t "${IMAGE}" .
          docker image ls "${IMAGE}"
        '''
      }
    }

    // Uncomment and configure to push to a registry
    // stage('Push Docker image (optional)') {
    //   when {
    //     allOf {
    //       expression { return fileExists('Dockerfile') }
    //       expression { return env.BRANCH_NAME == 'main' || env.CHANGE_TARGET == 'main' }
    //     }
    //   }
    //   environment {
    //     REGISTRY = 'your-registry.example.com'
    //     IMAGE_NAME = 'your-namespace/pytest-api'
    //   }
    //   steps {
    //     withCredentials([usernamePassword(credentialsId: 'dockerhub-or-registry-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
    //       sh '''
    //         set -e
    //         echo "${DOCKER_PASS}" | docker login -u "${DOCKER_USER}" --password-stdin ${REGISTRY}
    //         TAG="${REGISTRY}/${IMAGE_NAME}:${BUILD_NUMBER}"
    //         docker tag "pytest-api:${BUILD_NUMBER}" "${TAG}"
    //         docker push "${TAG}"
    //       '''
    //     }
    //   }
    // }

  }

  post {
    success {
      echo 'Build and tests succeeded.'
    }
    unstable {
      echo 'Build unstable (likely test failures).'
    }
    failure {
      echo 'Build failed.'
    }
    always {
      // Useful to clean up large caches on small agents; keep if disk is tight
      // deleteDir()
      echo 'Pipeline finished.'
    }
  }
}
