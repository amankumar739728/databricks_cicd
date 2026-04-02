# 🏗️ 1. FULL ARCHITECTURE

Using:

1.Databricks
2.Unity Catalog
3.GitHub Actions

🔷 Architecture Diagram (Logical Flow):

        Developer
            ↓
        GitHub Repo
            ↓ (push)
   GitHub Actions (CI/CD)
            ↓
   ┌───────────────┐
   │ Dev Deployment│ → Run DLT → Validate
   └───────────────┘
            ↓
   ┌───────────────┐
   │ Stg Deployment│ → Test
   └───────────────┘
            ↓
        🛑 Approval Gate
            ↓
   ┌───────────────┐
   │ Prod Deployment│ → Live Data
   └───────────────┘
            ↓
   Monitoring + Alerts
            ↓
        Rollback (Git)


## 🔁 2. END-TO-END FLOW

1. Write DLT code
2. Push to GitHub
3. CI/CD triggers
4. Deploy → Dev → Run pipeline
5. Deploy → Staging
6. Manual approval
7. Deploy → Production
8. Monitor pipeline
9. Rollback if failure

### 🧱 3. STEP-BY-STEP IMPLEMENTATION

✅ STEP 1: Install & Setup
## Installation commands
pip install databricks-cli
curl -fsSL https://raw.githubusercontent.com/databricks/cli/main/install.sh | sh

## Configuration commands
databricks configure

### 🏗️ 4. UNITY CATALOG SETUP:

<!-- ## SQL commands

-- cicd req:

CREATE CATALOG dev_catalog;
CREATE CATALOG stg_catalog;
CREATE CATALOG prod_catalog;

-- DEV
CREATE SCHEMA dev_catalog.bronze;
CREATE SCHEMA dev_catalog.silver;
CREATE SCHEMA dev_catalog.gold;

-- STAGING
CREATE SCHEMA stg_catalog.bronze;
CREATE SCHEMA stg_catalog.silver;
CREATE SCHEMA stg_catalog.gold;

-- PROD
CREATE SCHEMA prod_catalog.bronze;
CREATE SCHEMA prod_catalog.silver;
CREATE SCHEMA prod_catalog.gold; -->


### 🌐 5. PUSH TO GITHUB

## Command to push the code

git init
git add .
git commit -m "DLT project"
git branch -M main
git remote add origin https://github.com/amankumar739728/databricks_cicd.git
git push -u origin main

### 🧠 FINAL FLOW (VERY IMPORTANT)

Code Change
   ↓
Git Push
   ↓
CI/CD Triggered
   ↓
Dev Deploy + Run
   ↓
Staging Deploy
   ↓
🛑 Approval Required
   ↓
Production Deploy
   ↓
Monitoring
   ↓
Rollback (if needed)

### 6. Final Implementation Overview

“We implemented a CI/CD pipeline using Databricks Asset Bundles and GitHub Actions. The pipeline deploys DLT pipelines across dev, staging, and production using Unity Catalog. Data quality is enforced using DLT expectations, production deployments require manual approval, monitoring is done via pipeline events, and rollback is handled using Git versioning.”


#steps to configure token in pipeline for Databricks Asset Bundles (DAB)
# 1. How to get the token from Databricks

# Go to Databricks workspace → top right avatar → Settings
# Click Developer → Access Tokens
# Click Generate New Token
# Give it a name (e.g., github-cicd) and set expiry
# Copy the token (shown only once)


# 2. How to store it in GitHub

# Go to your repo: amankumar739728/databricks_cicd
# Settings → Secrets and variables → Actions
# Click New repository secret
# Name it: DATABRICKS_TOKEN (or anything you want)
# Paste the token value
# 
# Then in your deploy.yml reference it as:
#         DATABRICKS_TOKEN: ${{ secrets.DATABRICKS_TOKEN }}


<!-- ALternative(Recommended):
==>Use OAuth via Service Principal instead of PAT
Step 1: Create a Service Principal in Databricks

Go to Databricks → Settings → Identity and Access → Service Principals
Click Add Service Principal
Name it github-cicd-sp
Grant it Admin role on the workspace

Step 2: Generate OAuth secret

Click on the service principal
Go to Secrets tab → Generate secret
Copy the Client ID and Client Secret

Step 3: Add to GitHub Secrets

DATABRICKS_CLIENT_ID = Client ID
DATABRICKS_CLIENT_SECRET = Client Secret
Keep DATABRICKS_HOST as is

Step 4: Update deploy.yml
env:
  DATABRICKS_HOST: https://dbc-ccb24871-81f0.cloud.databricks.com
  DATABRICKS_CLIENT_ID: ${{ secrets.DATABRICKS_CLIENT_ID }}
  DATABRICKS_CLIENT_SECRET: ${{ secrets.DATABRICKS_CLIENT_SECRET }} -->


#Final Working Flow:

<!-- Push to main
      ↓
   dev job  ✅
   ├── Deploy dlt_dev pipeline
   ├── Run pipeline → 3 tables in dev_catalog.dev_schema
   └── Wait 60s
      ↓
   stg job  ✅
   ├── Deploy dlt_stg pipeline
   ├── Run pipeline → 3 tables in stg_catalog.stg_schema
   └── Wait 60s
      ↓
   prod job ✅ (manual approval)
   ├── Deploy dlt_prod pipeline
   └── Run pipeline → 3 tables in prod_catalog.prod_schema -->
