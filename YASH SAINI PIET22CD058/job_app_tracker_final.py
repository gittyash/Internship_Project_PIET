#!/usr/bin/env python
# coding: utf-8

# In[1]:


##we are going create a system that sorts out jobs for you depending upon your qualifications and personal information

#1.libraries import
import simple_colors as color
import pandas as pd
import webbrowser
import time
from plyer import notification
import numpy as py
from tkinter import filedialog

#2.Creating a DataFrame
data={"S.No":[1,2,3,4,5,6,7,8,9,10],
      "Company Name":["Atlassian","Indie MicroTech","Cent Media","TCS","Wipro","Amazon","Cognizant","JP Morgan","HCL","Byjus"],
       "Job Role":["SDE","Tech Lead","Front End Developer","Executive","SDE","FullStack Lead","Data Analyst","Data Analyst","Junior Engineer","Sales Executive"],
        "Exp. Required (in yrs)":["0-5","4-10","2-5","2-5","0-5","5-10","3-10","5-10","0-3","2-5"],
       "Salary (per annum)":[800000,1500000,600000,400000,450000,2000000,600000,2200000,400000,1200000],
     "Job Location":["Bangalore","Noida","Pune","Noida","Mumbai","Gurugram","Bangalore","Pune","Mumbai","Noida"],
     "Links":["https://www.atlassian.com/company/careers/all-jobs","https://www.microtekdirect.com/","https://centsmedialtd.com/about-us/","https://www.tcs.com/careers","https://careers.wipro.com/careers-home/","https://www.amazon.jobs/","https://careers.cognizant.com/global/en","https://careers.jpmorgan.com/in/en/home","https://www.hcltech.com/careers","https://byjus.com/careers-at-byjus/"]}
db=pd.DataFrame(data)
#.We have created a database acc. to which we will sort our users' information.

# 3.We create a  form to access user's information.
import tkinter as tk
from tkinter import ttk

def capture_data():
    data = {
        "Name": name_var.get(),
        "Experience": experience_combobox.get(),
        "Skills": [entry.get() for entry in skill_entries],
        "Job Profile": job_profile_combobox.get(),
        "Company Name": company_name_combobox.get(),
        "Expected Salary": expected_salary_var.get(),
        "Cities": [city for city, var in zip(cities, city_vars) if var.get()]
    }

    captured_data.append(data)
    print("Data captured:", data)
    data_app.destroy()

def add_skill_entry():
    skill_entry = ttk.Entry(skills_frame)
    skill_entry.pack(fill=tk.X, padx=10, pady=5)
    skill_entries.append(skill_entry)
def upload_resume():
    resume_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if resume_path:
        print("Resume uploaded:", resume_path)

# 3.1 Create empty lists to store captured data
captured_data = []

# 3.2 Create a basic GUI for capturing data
data_app = tk.Tk()
data_app.title("Data Capture")

# 3.3 Styling the form
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TCombobox", font=("Helvetica", 12))
style.configure("TCheckbutton", font=("Helvetica", 12))

# 3.4 Create widgets for each field
labels = ["Name", "Experience (in years)", "Skills", "Job Profile", "Company Name", "Expected Salary", "City"]
entries = []
city_vars = []

for label_text in labels:
    label = ttk.Label(data_app, text=label_text + ":")
    label.pack(pady=5, padx=10, anchor="w")
    
    if label_text == "Name":
        name_var = tk.StringVar()  # 3.5 Create StringVar for Name field
        entry = ttk.Entry(data_app, textvariable=name_var)
        entry.pack(fill=tk.X, padx=10, pady=5)
        entries.append(entry)
    elif label_text == "Experience (in years)":
        experience_values = list(range(0, 11))  # 3.6 Years of experience from 0 to 10
        experience_combobox = ttk.Combobox(data_app, values=experience_values)
        experience_combobox.pack(fill=tk.X, padx=10)
        entries.append(experience_combobox)
    elif label_text == "Skills":
        skills_frame = ttk.Frame(data_app)
        skills_frame.pack(pady=5, padx=10, anchor="w")
        skill_entries = []

        add_button = ttk.Button(skills_frame, text="+ Add Skill", command=add_skill_entry)
        add_button.pack(side=tk.LEFT)

        entries.append(skills_frame)
    elif label_text == "Job Profile":
        job_profile_values = [
            "SDE", "Tech Lead", "Senior Manager", "Executive",
            "Java Lead", "Full Stack Lead", "Front End Developer",
            "Junior Engineer", "Data Analyst", "Executive"
        ]
        job_profile_combobox = ttk.Combobox(data_app, values=job_profile_values)
        job_profile_combobox.pack(fill=tk.X, padx=10)
        entries.append(job_profile_combobox)
    elif label_text == "Company Name":
        company_name_values = [
            "Amazon", "TCS", "HCL", "Wipro", "Cognizant",
            "Capgemini", "Byjus", "Atlassian", "Indie Micro Tech",
            "Cent Media", "JP Morgan", "Byjuds", "McKinsey"
        ]
        company_name_combobox = ttk.Combobox(data_app, values=company_name_values)
        company_name_combobox.pack(fill=tk.X, padx=10)
        entries.append(company_name_combobox)
    elif label_text == "Expected Salary":
        expected_salary_var = tk.StringVar()  # 3.7 Create StringVar for Expected Salary field
        entry = ttk.Entry(data_app, textvariable=expected_salary_var)
        entry.pack(fill=tk.X, padx=10, pady=5)
        entries.append(entry)
    elif label_text == "City":
        cities = ["Bangalore", "Mumbai", "Pune", "Gurugram", "Noida"]
        city_vars = []
        
        for city in cities:
            city_var = tk.BooleanVar(value=False)
            city_vars.append(city_var)
            city_checkbutton = ttk.Checkbutton(data_app, text=city, variable=city_var)
            city_checkbutton.pack(anchor="w", padx=15)
        #3.8 Adding the Resume Upload Button
        resume_upload_button = ttk.Button(data_app, text="Upload Resume (PDF)", command=upload_resume)
        resume_upload_button.pack(pady=10)

# 3.9 Create and place the "Capture Data" button
capture_button = ttk.Button(data_app, text="Capture Data", command=capture_data)
capture_button.pack(pady=10)

data_app.mainloop()

# 3.10 After the GUI closes, you can access the captured data in the captured_data list
print("Captured Data:", captured_data)

#3.11 notification alert

notification_title = 'Your application has been accepted!'  
notification_message ='Searching jobs for you 🔃...'
  
notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = "C:\\Users\\Yash\\OneDrive\\Desktop\\training\\owl.ico",  
    timeout = 10,  
    toast = False  
    )
# 4.Now we Display Results
time.sleep(3)
print("\n\nHEY", captured_data[0]["Name"],"! \n")
print(color.blue(f''' 
        EXPERIENCE: {captured_data[0]["Experience"]}
        SKILLS: {captured_data[0]["Skills"]}
        JOB PROFILE: {captured_data[0]["Job Profile"]}
        COMPANY NAME : {captured_data[0]["Company Name"]}
        EXPECTED SALARY: {captured_data[0]["Expected Salary"]}
        CITIES: {captured_data[0]["Cities"]}\n\n'''))


print(color.black("We found these jobs for you: \n\n",['underlined']))
time.sleep(2)
if captured_data[0]["Job Profile"]=="SDE":
    print(f"\n{db.iloc[0:1]}\n{db.iloc[4:5]}")
elif captured_data[0]["Job Profile"]=="Tech Lead":
    print(f"\n{db.iloc[1:2]}\n{db.iloc[5:6]}")
elif captured_data[0]["Job Profile"]=="Front End Developer":
    print(f"\n{db.iloc[2:3]}\n{db.iloc[5:6]}")
elif captured_data[0]["Job Profile"]=="Executive":
    print(f"\n{db.iloc[3:4]}\n{db.iloc[9:10]}")
elif captured_data[0]["Job Profile"]=="Full Stack Lead":
    print(f"\n{db.iloc[2:3]}\n{db.iloc[5:6]}")
elif captured_data[0]["Job Profile"]=="Data Analyst":
    print(f"\n{db.iloc[7:8]}\n{db.iloc[8:9]}")
elif captured_data[0]["Job Profile"]=="Junior Engineer":
    print(f"\n{db.iloc[8:9]}")
elif captured_data[0]["Job Profile"]=="Sales Executive":
    print(f"\n{db.iloc[3:4]}\n{db.iloc[9:10]}")
else:
    print("\n")





# In[ ]:




