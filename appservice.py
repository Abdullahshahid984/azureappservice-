from azure.mgmt.web import WebSiteManagementClient
from azure.identity import DefaultAzureCredential

# Replace with your Azure credentials and parameters
subscription_id = "YOUR_SUBSCRIPTION_ID"
resource_group_name = "YOUR_RESOURCE_GROUP_NAME"
app_service_plan_name = "YOUR_APP_SERVICE_PLAN_NAME"
app_service_name = "YOUR_APP_SERVICE_NAME"

# Create the WebSiteManagementClient
credentials = DefaultAzureCredential()
client = WebSiteManagementClient(
    credential=credentials,
    subscription_id=subscription_id
)

# Create or Update the App Service Plan
app_service_plan_parameters = {
    "location": "eastus",
    "sku": {
        "name": "F1",
        "tier": "Free",
        "capacity": 1
    },
    "properties": {}
}

print("Creating App Service Plan...")
client.app_service_plans.begin_create_or_update(
    resource_group_name,
    app_service_plan_name,
    app_service_plan_parameters
).result()

# Create or Update the App Service
app_service_parameters = {
    "location": "eastus",
    "server_farm_id": f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{app_service_plan_name}",
    "site_config": {
        "always_on": True,
        "python_version": "3.8"
    },
    "kind": "app",
    "https_only": True
}

print("Creating App Service...")
client.web_apps.begin_create_or_update(
    resource_group_name,
    app_service_name,
    app_service_parameters
).result()

print("App Service created successfully.")
