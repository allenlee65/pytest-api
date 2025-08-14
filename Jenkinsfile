pipeline {
  agent any

  options {
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '20'))
    disableConcurrentBuilds()
    timeout(time: 30, unit: 'MINUTES')
    ansiColor('xterm') // modern, supported usage for colorized console[14][8]
  }

  environment {
    PYTHON_VERSION = '3.11'
    VENV_DIR = '.venv'
    PIP_CACHE_DIR = "${WORKSPACE}/.cache/pip"
    PYTEST_ADDOPTS = '--maxfail=1 -q'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
        sh 'python3 --version || true'
        sh 'pip3 --version || true'
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
          if grep -qiE 'flake8|ruff' requirements.txt; then
            echo "Running linters..."
            if python - <<'PY'
                import importlib, sys
                try:
                  importlib.import_module('flake8')
                  sys.exit(0)
                except ImportError:
                  sys.exit(1)
                PY
            then
              flake8 || true
            fi
            if python - <<'PY'
              import importlib, sys
              try:
                importlib.import_module('ruff')
                sys.exit(0)
              except ImportError:
                sys.exit(1)
              PY
            then
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
          # Run pytest and capture exit code without aborting the shell early
          set +e
          pytest -q \
            --junitxml=reports/junit.xml \
            --html=reports/pytest-report.html --self-contained-html
          TEST_STATUS=$?
          set -e

          # Helpful diagnostics: show what reports exist before publishing
          echo "Workspace: $(pwd)"
          ls -lah
          echo "Listing reports directory (if any):"
          ls -lah reports || true

          exit ${TEST_STATUS}
        '''
      }
      post {
        always {
          // Keep build green/flowing even if reports are missing, per plugin docs[2][4]
          junit testResults: 'reports/junit.xml', allowEmptyResults: true
          // If reports may land in subfolders or under different names, consider:
          // junit testResults: '**/reports/*.xml', allowEmptyResults: true  // Ant glob, workspace-rooted[4][2]

          archiveArtifacts artifacts: 'reports/**', fingerprint: true, allowEmptyArchive: true
        }
      }
    }
  }

  post {
    success { echo 'Build and tests succeeded.' }
    unstable { echo 'Build unstable (likely test failures).' }
    failure { echo 'Build failed.' }
    always  { echo 'Pipeline finished.' }
  }
}
