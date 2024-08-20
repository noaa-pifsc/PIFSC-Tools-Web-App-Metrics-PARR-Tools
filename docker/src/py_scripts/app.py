# include required libraries
import time

#specify the start timer for the entire test suite
test_suite_start_timer = time.time()


import os
import random
import string
from datetime import datetime, timedelta 

# include selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# import custom .py include files:
from lib import custom_functions     # defines custom functions used to 
from lib import app_config           # defines runtime application configuration values
from lib import login_credentials    # defines web login credentials
from lib import project_scenario_config

    
    
# set the variable to also print all log messages or not:
print_log_messages = True

# create the .csv file to capture the web performance metrics

# check if the .csv file exists
if os.path.isfile('/app/data/'+app_config.csv_output_file):
    # the .csv file exists

    # open the .csv file in append mode
    fp = open("/app/data/"+app_config.csv_output_file, "a")
else:
    # the .csv file does not exist

    # create the .csv file in write mode:
    fp = open("/app/data/"+app_config.csv_output_file, "x")

    # create the .csv header row
    fp.write('"App Name","Metrics App Location","Test App Location","Date/Time","Page Name","Action","# Files","Total File Size (KB)","Total Response Time (s)","Screenshot File"'+"\n")


# set the selenium options:
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--window-size=1920,1080")
# options.add_argument('--enable-javascript')
options.add_argument('ignore-certificate-errors')
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

prefs = {"download.default_directory" : "/app/data"};

options.add_experimental_option("prefs",prefs);

# create the chrome webdriver object
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# enable the network cache
driver.execute_cdp_cmd("Network.setCacheDisabled", {"cacheDisabled":False})

# custom_functions.log_value("load the page", print_log_messages)


"""
START - 1. Request the base_web_url defined in the application configuration
"""

# Login to web application:
custom_functions.log_value("1. Request the base_web_url defined in the application configuration", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)


# check the value of the app_location
if (project_scenario_config.app_location == "remote"):
    # this a remote application, use the remote_web_url

    custom_functions.log_value("This is a remote application: "+app_config.remote_web_url, print_log_messages)
    
    # load the URL in the web browser
    driver.get(app_config.remote_web_url) 
else:
    # this a local application, use the local_web_url

    custom_functions.log_value("This is a local application: "+app_config.local_web_url, print_log_messages)
    
    # load the URL in the web browser
    driver.get(app_config.local_web_url) 
    

# wait for the response from the page load until the second chart has rendered based on a dynamic label for the chart and log the standard metrics
return_value = custom_functions.wait_for_response (None, By.XPATH, "//div[@id='archival_chart_id']//*[name()='text'][text()='SOD']", start_timer, driver, print_log_messages, fp, None, "Page Load")

"""
END - 1. Request the base_web_url defined in the application configuration
"""



"""
START - 2. Data Set List page load
"""

custom_functions.log_value ("2. find and click the Data Set List link", print_log_messages)

# get the Data Set List link element
current_link = driver.find_element(By.XPATH, "//a[text()='Data Set List']")

# start the timer
start_timer=round(time.time()*1000)

# click the link
driver.execute_script("arguments[0].click()", current_link)


# wait for the response from the page load until the PIR Division/Program select element is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, By.ID, "P2_ORG_ALIASES", start_timer, driver, print_log_messages, fp, None, "Page Load")



"""
END - 2. Data Set List page load
"""


"""
START - 3. Open column popup for the filter Data Set List page load (by custom info exists column)
"""

custom_functions.log_value ("3. find and click the Custom Info Exists? header element", print_log_messages)


# filter the report on the custom info exists field
current_link = driver.find_element(By.XPATH, "//a[@class='a-IRR-headerLink'][text()='Custom Info Exists?']")

# custom_functions.log_value("the value of the innerHTML is: '"+filter_elem.get_attribute("innerHTML")+"'", True)

# custom_functions.log_value("click the filter custom info fields? table heading", True)

# start the timer
start_timer=round(time.time()*1000)

# click the link (will send ajax request for the filtering options dynamically)
driver.execute_script("arguments[0].click()", current_link)

# wait for the ajax response to be processed to display the sort widget
return_value = custom_functions.wait_for_response (None, By.XPATH, "//div[@class='a-IRR-sortWidget-rows']", start_timer, driver, print_log_messages, fp, "filter search popup", "Interactive Report Filter")


"""
END - 3. Open column popup for the filter Data Set List page load (by custom info exists column)
"""


"""
START - 4. Define filter for the Data Set List page (by custom info exists column)
"""

custom_functions.log_value ("4. Specify the 'No' filter to refresh the report records", print_log_messages)


# click the View button
current_element = driver.find_element(By.XPATH, "//a//i[contains(@class, 'fa-eye')]/..")

# find the link for filtering the records by "No"
current_link = driver.find_element(By.XPATH, "//div[@class='a-IRR-sortWidget-rows']/a[text()='No']")


# start the timer
start_timer=round(time.time()*1000)


# click the link to filter the data sets:
driver.execute_script("arguments[0].click()", current_link)



# wait for the response from the page load until the view links are reloaded
return_value = custom_functions.wait_for_response (current_element, By.XPATH, "//a//i[contains(@class, 'fa-eye')]", start_timer, driver, print_log_messages, fp, "filter", "Page Reload/Filter Report")


"""
END - 4. Define filter for the Data Set List page (by custom info exists column)
"""

"""
START - 5. Redirect to the data set info page by clicking on the view link for a data set record
"""

custom_functions.log_value ("5. find and click the first view link in the interactive report", print_log_messages)

# click the View button
current_link = driver.find_element(By.XPATH, "//a//i[contains(@class, 'fa-eye')]/..")


# start the timer
start_timer=round(time.time()*1000)

# click the link (will redirect to login page)
driver.execute_script("arguments[0].click()", current_link)


                
# wait for the response from the page load until the username field is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, By.ID, "P101_USERNAME", start_timer, driver, print_log_messages, fp, None, "Page Load")


"""
END - 5. Redirect to the data set info page by clicking on the view link for a data set record
"""

"""
START - 6. Login to the web app
"""


# Login to web application:
custom_functions.log_value("6. login to the application", print_log_messages)
    
# find the username/password fields
username_field = driver.find_element("id", "P101_USERNAME")
password_field = driver.find_element("id", "P101_PASSWORD")

# find the login button
login_button = driver.find_element(By.XPATH, "//button[contains(@class, 't-Button')]//span[contains(., 'Log In')]/..")
# click the login button
custom_functions.log_object(login_button, print_log_messages)

# specify the username/password for the web app (from lib/login_credentials.py)
username_field.send_keys(login_credentials.login_username)
password_field.send_keys(login_credentials.login_password)

# custom_functions.log_value("submit the login button", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)

# submit the login form
login_button.click()


# wait for the response from the page load until the InPort link element is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, By.ID, "P210_INPORT_LINK_URL", start_timer, driver, print_log_messages, fp, None, "Login/Page Load")


"""
END - 6. Login to the web app
"""


"""
START - 7. Redirect to the create custom data set fields page
"""

# Open the Create Custom Data Set Fields Page
custom_functions.log_value("7. Open the Create Custom Data Set Fields page", print_log_messages)

# start the timer
start_timer=round(time.time()*1000)

# click the create record button
driver.find_element(By.XPATH, "//button[contains(@class, 't-Button')]//span[contains(., 'Create')]/..").click()
                
# wait for the response from the page load until the first form field is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, By.ID, "P220_DS_MD_COMP_YN", start_timer, driver, print_log_messages, fp, 'create custom data set info', "Page Load")

"""
END - 7. Redirect to the create custom data set fields page
"""


"""
START - 8. Insert custom data set record 
"""

# create a new data set info record by filling out all the form fields with test values
custom_functions.log_value("8. Create a new record by specifying field values and submitting the form", print_log_messages)



current_field = driver.find_element("id", "P220_DS_MD_COMP_YN")
current_field.send_keys("Yes");


current_field = driver.find_element("id", "P220_DS_MD_APPR_YN")
current_field.send_keys("No");

current_field = driver.find_element("id", "P220_WAIV_REASON_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Other (Add comment why)")

current_field = driver.find_element("id", "P220_WAIV_REAS_EXPL")
current_field.send_keys("Test - Waiver Explanation");

current_field = driver.find_element("id", "P220_CURR_DATA_ACC_YN")
current_field.send_keys("No");

current_field = driver.find_element("id", "P220_CURR_DATA_ACC_URL")
current_field.send_keys("https://test.com/12345");

current_field = driver.find_element("id", "P220_DATA_QUALITY_CONF_YN")
current_field.send_keys("Yes");

current_field = driver.find_element("id", "P220_DISSEM_FORMAT_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Bulk Downloadable (tabular data, e.g., Excel, CSV, ASCII)")


current_field = driver.find_element("id", "P220_DISSEM_PLAN_YN")
current_field.send_keys("Yes");

current_field = driver.find_element("id", "P220_DISSEM_PLAN_URL")
current_field.send_keys("https://test.com/dissemination-plan");

current_field = driver.find_element("id", "P220_INT_IMP_CAPACITY")
current_field.send_keys("Test - Internal capacity is sufficient");

current_field = driver.find_element("id", "P220_DISSEM_IMP_TIMEFRAME")
current_field.send_keys("Test - Coming Soon");

current_field = driver.find_element("id", "P220_OBS_TYPES_LEFT")

# create action chain object
action = ActionChains(driver)

current_option = driver.find_element(By.XPATH, "//select[@id='P220_OBS_TYPES_LEFT']/option[text()='atlas']")

# double click the option element
action.double_click(on_element = current_option).perform()


current_option = driver.find_element(By.XPATH, "//select[@id='P220_OBS_TYPES_LEFT']/option[text()='daily maximum']")

# double click the option element
action.double_click(on_element = current_option).perform()





current_field = driver.find_element("id", "P220_NCEI_TITLE")
current_field.send_keys("Test Title");

current_field = driver.find_element("id", "P220_NCEI_ABSTRACT")
current_field.send_keys("Test Abstract");

current_field = driver.find_element("id", "P220_STUDY_LOC_EXISTS_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Yes")

current_field = driver.find_element("id", "P220_DATA_PKG_REV_APPR_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("No")

# start the timer
start_timer=round(time.time()*1000)


# click the create specimen button
driver.find_element(By.XPATH, "//button[contains(@class, 't-Button')]//span[contains(., 'Create')]/..").click()


# wait for the response from the page load until the InPort Link is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, By.ID, "P210_INPORT_LINK_URL", start_timer, driver, print_log_messages, fp, 'post record insert', "Record Insert/Page Load")


"""
END - 8. Insert custom data set record 
"""


"""
START - 9. Update the custom data set record that was just entered
"""

# Open the View/Edit Specimen Page - Begin
custom_functions.log_value("9. Open the Create Custom Data Set Fields page", print_log_messages)


# find the edit custom data set fields link
current_link = driver.find_element(By.XPATH, "//td[@class='t-Report-cell']/a/i[contains(@class, 'fa-pencil')]/..")


# start the timer
start_timer=round(time.time()*1000)


# click the link (will redirect to edit custom data set info page)
driver.execute_script("arguments[0].click()", current_link)


# wait for the response from the page load until the first form field is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, By.ID, "P220_DS_MD_COMP_YN", start_timer, driver, print_log_messages, fp, 'edit custom data set info', "Page Load/Post Record Insert")

"""
END - 9. Update the custom data set field that was just entered
"""


"""
START - 10. Update custom data set record 
"""

# update the custom data set info record by filling out all the form fields with test values and clicking the save button
custom_functions.log_value("10. Update an existing record by specifying field values and submitting the form", print_log_messages)

current_field = driver.find_element("id", "P220_DS_MD_COMP_YN")
current_field.clear()
current_field.send_keys("No");


current_field = driver.find_element("id", "P220_DS_MD_APPR_YN")
current_field.clear()
current_field.send_keys("Yes");

current_field = driver.find_element("id", "P220_WAIV_REASON_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Extreme Size - Photo")

current_field = driver.find_element("id", "P220_WAIV_REAS_EXPL")
current_field.clear()
current_field.send_keys("Test - No waiver needed");

current_field = driver.find_element("id", "P220_CURR_DATA_ACC_YN")
current_field.clear()
current_field.send_keys("Yes");

current_field = driver.find_element("id", "P220_CURR_DATA_ACC_URL")
current_field.clear()
current_field.send_keys("https://test.com/54321");

current_field = driver.find_element("id", "P220_DATA_QUALITY_CONF_YN")
current_field.clear()
current_field.send_keys("No");

current_field = driver.find_element("id", "P220_DISSEM_FORMAT_ID")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Queryable (relational databases, e.g., Oracle, MySQL)")


current_field = driver.find_element("id", "P220_DISSEM_PLAN_YN")
current_field.clear()
current_field.send_keys("No");

current_field = driver.find_element("id", "P220_DISSEM_PLAN_URL")
current_field.clear()
current_field.send_keys("https://test.com/dissemination-plan-test");

current_field = driver.find_element("id", "P220_INT_IMP_CAPACITY")
current_field.clear()
current_field.send_keys("Test - Internal capacity is NOT sufficient");

current_field = driver.find_element("id", "P220_DISSEM_IMP_TIMEFRAME")
current_field.clear()
current_field.send_keys("Test - 6 months");

# current_field = driver.find_element("id", "P220_OBS_TYPES_LEFT")

current_option = driver.find_element(By.XPATH, "//select[@id='P220_OBS_TYPES_LEFT']/option[text()='discrete sample']")

# double click the option element
action.double_click(on_element = current_option).perform()


current_option = driver.find_element(By.XPATH, "//select[@id='P220_OBS_TYPES_LEFT']/option[text()='profile']")

# double click the option element
action.double_click(on_element = current_option).perform()




current_field = driver.find_element("id", "P220_NCEI_TITLE")
current_field.clear()
current_field.send_keys("Test Title - Update");

current_field = driver.find_element("id", "P220_NCEI_ABSTRACT")
current_field.clear()
current_field.send_keys("Test Abstract - Update");

current_field = driver.find_element("id", "P220_STUDY_LOC_EXISTS_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("No")

current_field = driver.find_element("id", "P220_DATA_PKG_REV_APPR_YN")
current_select_field = Select(current_field)
current_select_field.select_by_visible_text("Yes")

# start the timer
start_timer=round(time.time()*1000)

# click the Save specimen button
driver.find_element(By.XPATH, "//button[contains(@class, 't-Button')]//span[contains(., 'Save')]/..").click()

# wait for the response from the page load until the InPort Link is clickable and log the standard metrics
return_value = custom_functions.wait_for_response (None, By.ID, "P210_INPORT_LINK_URL", start_timer, driver, print_log_messages, fp, 'post record update', "Record Update/Page Load")

"""
END - 10. Update custom data set record 
"""


custom_functions.log_value("All of the web actions in the test suite have completed", print_log_messages)

# calculate the elapsed time in minutes based on the test_suite_start_timer variable and the current time
total_time_min=round(((time.time()-test_suite_start_timer)/60), 2)

# log the elapsed time for the entire test suite
custom_functions.log_value('total elapsed time (min): '+str(total_time_min), print_log_messages)



# selenium driver session cleanup:

# close the selenium driver
driver.close()

# quit the selenium driver
driver.quit()


