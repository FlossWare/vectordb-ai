# Code Quality Tools

VectorDB AI uses comprehensive code quality tools (Python equivalents of Java's FindBugs, Checkstyle, etc.).

## Automated Checks

Every PR and commit automatically runs:

| Tool | Purpose | Java Equivalent | Status |
|------|---------|-----------------|--------|
| **black** | Code formatting | Google Java Format | ✅ Required |
| **isort** | Import sorting | - | ✅ Required |
| **flake8** | Style + errors | Checkstyle | ✅ Required |
| **pylint** | Code analysis | FindBugs/SpotBugs | ⚠️ Warning |
| **mypy** | Type checking | Checker Framework | ⚠️ Warning |
| **bandit** | Security scan | FindSecBugs | ✅ Required |
| **safety** | Dependency vulnerabilities | OWASP Dependency Check | ⚠️ Warning |
| **pytest** | Unit tests | JUnit | ⚠️ Warning |

**Legend:**
- ✅ Required: Must pass or build fails
- ⚠️ Warning: Issues reported but don't fail build

---

## Running Locally

### Install Tools

```bash
cd python
pip install pylint flake8 mypy bandit safety black isort pytest pytest-cov
```

### Run All Checks

```bash
# Format code (auto-fix)
black vectordb_ai/
isort vectordb_ai/

# Check style
flake8 vectordb_ai/

# Analyze code (like FindBugs)
pylint vectordb_ai/

# Type check
mypy vectordb_ai/

# Security scan
bandit -r vectordb_ai/

# Dependency vulnerabilities
safety check

# Run tests
pytest tests/ -v --cov=vectordb_ai
```

### Quick Pre-Commit Check

```bash
# Run everything at once
black vectordb_ai/ && \
isort vectordb_ai/ && \
flake8 vectordb_ai/ && \
bandit -r vectordb_ai/ -ll && \
pytest tests/ -v
```

---

## Tool Details

### 1. Black (Code Formatting)

**Purpose:** Automatic code formatting (like Google Java Format)

**Config:** `pyproject.toml`

```bash
# Format all code
black vectordb_ai/

# Check without modifying
black --check vectordb_ai/
```

**Settings:**
- Line length: 120
- Target: Python 3.8+

---

### 2. isort (Import Sorting)

**Purpose:** Alphabetize and organize imports

**Config:** `pyproject.toml`

```bash
# Sort imports
isort vectordb_ai/

# Check without modifying
isort --check-only vectordb_ai/
```

---

### 3. Flake8 (Style + Error Detection)

**Purpose:** Enforce PEP 8 style guide + detect errors (like Checkstyle)

**Config:** `.flake8`

```bash
# Check code
flake8 vectordb_ai/
```

**Checks:**
- PEP 8 style violations
- Unused imports
- Undefined names
- Syntax errors

---

### 4. Pylint (Code Analysis)

**Purpose:** Deep code analysis (like FindBugs/SpotBugs)

**Config:** `.pylintrc`

```bash
# Analyze code
pylint vectordb_ai/
```

**Detects:**
- Code smells
- Unused variables
- Potential bugs
- Code complexity
- Best practice violations

**Warning only** - doesn't fail build (too strict for initial development)

---

### 5. Mypy (Type Checking)

**Purpose:** Static type checking (like Checker Framework)

**Config:** `pyproject.toml`

```bash
# Type check
mypy vectordb_ai/
```

**Checks:**
- Type annotations
- Type mismatches
- Optional types
- Return types

**Warning only** - Python is gradually typed

---

### 6. Bandit (Security Scanner)

**Purpose:** Find security issues (like FindSecBugs)

**Config:** `.bandit`

```bash
# Security scan
bandit -r vectordb_ai/

# High severity only
bandit -r vectordb_ai/ -ll
```

**Detects:**
- SQL injection
- Command injection
- Hardcoded passwords
- Insecure random
- Weak crypto
- Path traversal

**Required** - security issues fail the build

---

### 7. Safety (Dependency Vulnerabilities)

**Purpose:** Check for known vulnerabilities (like OWASP Dependency Check)

```bash
# Check dependencies
safety check

# JSON output
safety check --json
```

**Checks:**
- Known CVEs in dependencies
- Security advisories
- Outdated packages with vulnerabilities

**Warning only** - may have false positives

---

### 8. Pytest (Unit Tests)

**Purpose:** Run unit tests (like JUnit)

**Config:** `pyproject.toml`

```bash
# Run tests
pytest tests/ -v

# With coverage
pytest tests/ -v --cov=vectordb_ai --cov-report=term-missing
```

**Features:**
- Automatic test discovery
- Coverage reporting
- Parallel execution
- Fixtures

---

## Pre-Commit Hook

Install pre-commit hooks to run checks automatically:

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.9.1
    hooks:
      - id: black
        args: [--line-length=120]

  - repo: https://github.com/PyCQA/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: [--profile=black]

  - repo: https://github.com/PyCQA/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        args: [--max-line-length=120]

  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: [-ll, -r, vectordb_ai/]
```

---

## CI/CD Integration

### GitHub Actions

Automatically runs on:
- ✅ Every pull request to `main`
- ✅ Every push to `main`
- ✅ Manual trigger

**Workflow:** `.github/workflows/code-quality.yml`

**View results:**
- https://github.com/FlossWare/vectordb-ai/actions

---

## Configuration Files

| File | Purpose |
|------|---------|
| `.flake8` | Flake8 configuration |
| `.pylintrc` | Pylint configuration |
| `.bandit` | Bandit configuration |
| `pyproject.toml` | Black, isort, mypy, pytest config |

---

## Fail vs Warn

### ✅ Must Pass (Fail Build)

- **black** - Code must be formatted
- **isort** - Imports must be sorted
- **flake8** - Style must be correct
- **bandit** - No security issues

### ⚠️ Warning Only

- **pylint** - Too strict for initial dev
- **mypy** - Python is gradually typed
- **safety** - May have false positives
- **pytest** - Tests may not exist yet

---

## Best Practices

### Before Committing

```bash
# 1. Format code
black vectordb_ai/
isort vectordb_ai/

# 2. Check style
flake8 vectordb_ai/

# 3. Security scan
bandit -r vectordb_ai/ -ll

# 4. Run tests
pytest tests/ -v
```

### Writing Code

1. ✅ Use type hints
2. ✅ Write docstrings
3. ✅ No hardcoded secrets
4. ✅ Validate input
5. ✅ Handle errors
6. ✅ Write tests

### Handling Issues

**If flake8 fails:**
- Fix style violations
- Or add `# noqa` comment with reason

**If bandit fails:**
- **Never ignore security issues**
- Fix the vulnerability
- Or provide justification

**If pylint warns:**
- Try to fix
- Or add `# pylint: disable=rule-name` with reason

---

## Badges

Add to README.md:

```markdown
![Code Quality](https://github.com/FlossWare/vectordb-ai/actions/workflows/code-quality.yml/badge.svg)
![Coverage](https://codecov.io/gh/FlossWare/vectordb-ai/branch/main/graph/badge.svg)
```

---

## Summary

**VectorDB AI uses industry-standard Python code quality tools:**

- ✅ Automated formatting (black, isort)
- ✅ Style checking (flake8)
- ✅ Code analysis (pylint - like FindBugs)
- ✅ Type checking (mypy)
- ✅ **Security scanning (bandit - like FindSecBugs)**
- ✅ Dependency vulnerabilities (safety - like OWASP)
- ✅ Unit tests (pytest - like JUnit)

**Every commit is automatically checked!** 🚀
