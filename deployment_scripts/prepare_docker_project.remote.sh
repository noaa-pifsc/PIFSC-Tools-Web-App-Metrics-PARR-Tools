#! /bin/sh

# load the project configuration script to set the runtime variable values
. ../docker/src/sh_scripts/config/project_deploy_config.sh

#deployment script for remote scenario

echo "running remote scenario deployment script"

root_directory="/c"

# construct the project folder name:
project_folder_name=$project_path"-remote"

# construct the full project path
full_project_path=$root_directory"/docker/"$project_folder_name"/docker/src"

mkdir $root_directory/docker
rm -rf $root_directory/docker/$project_folder_name
mkdir $root_directory/docker/$project_folder_name

echo "clone the project repository"

#checkout the git projects into the same temporary docker directory
git clone  $git_url $root_directory/docker/$project_folder_name

echo "rename configuration files"

#rename the project_scenario_config.remote.py to project_scenario_config.py so it can be used as the active configuration file
mv $full_project_path/py_scripts/lib/project_scenario_config.remote.py $full_project_path/py_scripts/lib/project_scenario_config.py

# remove the local and hybrid scripts
rm $full_project_path/py_scripts/lib/project_scenario_config.local.py

rm $full_project_path/py_scripts/lib/project_scenario_config.hybrid.py


#rename the project_scenario_config.remote.sh to project_scenario_config.sh so it can be 
echo ""
echo "the remote docker project files are now ready for configuration and image building/deployment"

read
