# ---------------------------------------------------
# Courtesy of Om Patil- AHS FBLA Secretary 2023-2024
# FBLA Points System Automated in Python
# ---------------------------------------------------

# INSTRUCTIONS!!!
# First, open the full member points system for the entire year
# Paste all the First and Last Names into the First and Last name Task on Hand
# Next, click on 'File' and hover over 'Download' and click on 'Comma Separated Values (.csv)'
# Do this step for each of the grade levels
# Open Visual Studio Code IDE
# Open this script and all 4 csv files of each grade level
# Run script for one csv file
# After you run it, your data with the points should save in the csv file you downloaded. 
# Follow these directions- https://blog.golayer.io/google-sheets/import-csv-to-google-sheets 
# After you have done this, go ahead and copy-paste your data into the master google sheets.
# Repeat the run process and transformation into the master sheets for all grade level csv's.


import pandas as pd
import string

alphabet = list(string.ascii_lowercase)

# SWITCH CSV FILE FOR EACH GRADE LEVEL FOR EACH RUN
name_of_file = 'Test11.csv'

df = pd.read_csv(name_of_file)

num_of_attendees = 0
task = df["First Name: Task on Hand:"].isnull()

while task[num_of_attendees] != True:
    num_of_attendees+=1

total_members = len(df["Last Name"])

points_added = 5


for att in range(num_of_attendees):
    for member in range(total_members):
        if df.loc[att].at["Last Name: Task on Hand"].lower().strip() == df.loc[member].at["Last Name"].lower().strip():
            if df.loc[att].at["First Name: Task on Hand:"].lower().strip() == df.loc[member].at["First Name"].lower().strip():
                points = df.loc[member].at["Points"]
                df.at[member, "Points"] = points + points_added
                df.to_csv(name_of_file, index=False)
                print("y")

print(df)
