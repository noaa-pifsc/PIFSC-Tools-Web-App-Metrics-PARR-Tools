# PARR Tools - Web Application Metrics

## Overview
The Public Access to Research Results (PARR) Tools Web Application Metrics (WAM) project was developed to provide an automated method to capture performance metrics from the user perspective for a suite of web actions on the PARR Tools web app.  The PARR Tools WAM project can be executed in a variety of scenarios for flexibility.  This project is forked from the [Web App Metrics](https://picgitlab.nmfs.local/centralized-data-tools/web-app-metrics) and customized for the PARR Tools web app.  

## Resources
-   PARR Tools WAM Version Control Information:
    -   URL: https://picgitlab.nmfs.local/web-app-metrics/parr-tools-web-app-metrics
    -   Version: 1.0 (Git tag: parr_tools_web_app_metrics_v1.0)
    -   Forked repository (upstream)
        -   [Web App Metrics README](https://picgitlab.nmfs.local/centralized-data-tools/web-app-metrics/-/blob/main/README.md?ref_type=heads)
        -   WAM Version Control Information:
    -   URL: git@picgitlab.nmfs.local:centralized-data-tools/web-app-metrics.git
    -   Version: 1.4 (Git tag: web_app_metrics_v1.4)

## Scenarios
-   There are three different scenarios implemented by the docker project:
    -   Local - this scenario deploys the docker container to a local docker host and connects to a local Oracle database
    -   Remote - this scenario deploys the docker container to a remote docker host and connects to a remote Oracle database
    -   Hybrid - this scenario deploys the docker container to a local docker host and connects to a remote Oracle database

## Setup Procedure
-   Execute the appropriate docker preparation script stored in the [deployment_scripts](./deployment_scripts) folder to prepare the docker container for deployment in a new working directory
    -   For example use the [prepare_docker_project.local.sh](./deployment_scripts/prepare_docker_project.local.sh) bash script to prepare the Local docker container for deployment in the c:/docker/parr-tools-web-app-metrics-local folder
-   Update the login_credentials.py file in the appropriate new working directory to specify the web login credentials for the (e.g. c:/docker/parr-tools-web-app-metrics-local/docker/src/login_credentials.py) for the local scenario
-   \*Note: more information about the setup procedure for this forked project is available in the [Web App Metrics README](https://picgitlab.nmfs.local/centralized-data-tools/web-app-metrics/-/blob/main/README.md?ref_type=heads#forked-repository-implementation)

## Building/Running Container
-   Execute the appropriate build and deploy script for the given scenario (e.g. [build_deploy_project.remote.sh](./deployment_scripts/build_deploy_project.remote.sh) for the remote scenario)

## Docker Application Processing
-   \*Note: more information about the docker application processing for this forked project is available in the [Web App Metrics README](https://picgitlab.nmfs.local/centralized-data-tools/web-app-metrics/-/blob/main/README.md?ref_type=heads#docker-application-processing)

## Checking Results
-   Open the docker volume parr-tools-web-app-metrics-logs to view the log files for the different executions of the docker container
-   Open the docker volume parr-tools-web-app-metrics-data to view the exported data files for the different queries
    -   Open the parr_tools_web_performance_metrics.csv to view the metrics that were captured for each query execution

## Standard Metrics/Information Logging
-   The following metrics and information is captured for each web action in a .csv file:
    -   Date/Time - The Date/Time the given web action was started in MM/DD/YYYY HH:MI:SS AM/PM format
    -   Page Name - The page the web action was executed on
    -   Action - The type of web action
    -   # Files - The total number of web resource files (e.g. image, css, JavaScript file, etc.) downloaded for the given web action
    -   Total File Size (KB) - The total size in kilobytes of the web resource files downloaded for the given web action
    -   Total Response Time (s) - The total number of seconds for the web action to complete and the app is ready to accept user interactions
    -   Screenshot file name - the name of the screenshot file saved in the data volume for the given web action

## Implemented Web Actions
1.  Load Data Set Dashboard page
2.  Load Data Set List page
3.  Data Set List page - popup interactive report filter
4.  Data Set List page - define interactive report filter (dynamically refresh data in page)
5.  Load Login page (click on view data set link)
6.  Login to app (load Data Set Information page for selected record)
7.  Load Custom Data Set Info record (click on Create button)
8.  Load Data Set Information Page (specify field values and submit form)
9.  Load Custom Data Set Info record (click on Update link)
10. Load Data Set Information Page (specify updated field values and submit form)
