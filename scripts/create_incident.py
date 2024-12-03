import requests
from requests.auth import HTTPBasicAuth
import sys

# ServiceNow details
BASE_URL = "https://<your_instance>.service-now.com"
CREATE_INCIDENT_API = f"{BASE_URL}/api/now/table/incident"
USERNAME = "your_username"
PASSWORD = "your_password"

def create_incident(description, pipeline_name):
    payload = {
        "short_description": f"Pipeline Failed: {pipeline_name}",
        "description": description,
        "urgency": "1",  # High urgency
        "impact": "1"   # High impact
    }
    response = requests.post(
        CREATE_INCIDENT_API,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        headers={"Content-Type": "application/json"},
        json=payload
    )
    if response.status_code == 201:
        print("Incident Created Successfully:", response.json())
    else:
        print("Error Creating Incident:", response.text)
        sys.exit(1)

if __name__ == "__main__":
    pipeline_name = sys.argv[1] if len(sys.argv) > 1 else "Unknown Pipeline"
    description = sys.argv[2] if len(sys.argv) > 2 else "No description provided."
    create_incident(description, pipeline_name)
