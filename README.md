# CI/CD Pipeline with ServiceNow Integration

This repository demonstrates a CI/CD pipeline with ServiceNow integration using REST APIs to create and resolve incidents based on pipeline statuses.

## **Structure**
- `.github/workflows/pipeline.yml`: CI/CD pipeline definition using GitHub Actions.
- `scripts/`: Contains Python scripts for ServiceNow integration.
  - `create_incident.py`: Creates a ServiceNow incident when the pipeline fails.
  - `resolve_incident.py`: Resolves a ServiceNow incident when the pipeline succeeds.
- `app/build.py`: Simulated build process to trigger pipeline statuses.
- `requirements.txt`: Dependencies for the Python scripts.

## **Setup**
1. Clone the repository:
```
  git clone <repository-url>
   cd <repository-folder>
```
2.Install dependencies:
```
pip install -r requirements.txt
```
3.Configure ServiceNow credentials:

- Update USERNAME and PASSWORD in scripts/create_incident.py and scripts/resolve_incident.py.
- Alternatively, use environment variables for secure storage.

## Push to GitHub:
```
git add .
git commit -m "Initial setup with ServiceNow integration"
git push origin main
```

### Usage
- Trigger the pipeline by pushing changes to the main branch.
- On build failure, a ServiceNow incident will be created.
- On successful build, the incident will be resolved.
