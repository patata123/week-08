import streamlit as st
import pandas as pd
import json
from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# Load the JSON file
filepath = './data/courses-full.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)
    print(dict_of_courses)

# Extract the value of the `dict_of_courses` dictionary
# If you are not sure what the dictionary looks like, you can print it out
list_of_dict = []
for course_name, details_dict in dict_of_courses.items():
    list_of_dict.append(details_dict)

# display the `dict_of_course` as a Pandas DataFrame
df = pd.DataFrame(list_of_dict)
df