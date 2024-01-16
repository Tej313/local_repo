import json

# Assuming you have a list or dictionary containing job post data
job_posts = [
    {
        "company name": "IvanInfotechPvt.Ltd.",
        "skills": "rest,python,security,debugging",
        "more info": "https://www.timesjobs.com/job-detail/python-developer-ivan-infotech-pvt-ltd-kolkata-2-to-5-yrs-jobid-1h6sLaqbaBZzpSvf__PLUS__uAgZw==&source=srp"
    },
    {
        "company name": "eastindiasecuritiesltd.",
        "skills": "python,hadoop,machinelearning",
        "more info": "https://www.timesjobs.com/job-detail/python-engineer-east-india-securities-ltd-kolkata-2-to-5-yrs-jobid-KEkE19WqPbFzpSvf__PLUS__uAgZw==&source=srp"
    },
    {
        "company name": "WingGlobalITServices",
        "skills": "springboot,python,java,django,jpa,hibernate",
        "more info": "https://www.timesjobs.com/job-detail/python-developer-wing-global-it-services-panchkula-2-to-5-yrs-jobid-__PLUS__fePw2G3HHZzpSvf__PLUS__uAgZw==&source=srp"
    },
    {
        "company name": "arttechnologyandsoftwareindiapvtltd",
        "skills": "rest,python,database,django,api",
        "more info": "https://www.timesjobs.com/job-detail/python-developer-art-technology-and-software-india-pvt-ltd-cochin-kochi-ernakulam-2-to-3-yrs-jobid-M26lxDEd__PLUS__qtzpSvf__PLUS__uAgZw==&source=srp"
    },
    {
        "company name": "RootInfoSolutions",
        "skills": "python2,python3,django,javascript,html,postgresql/mysql,restapi,celeryrabbitmq,redis.,css,oop",
        "more info": "https://www.timesjobs.com/job-detail/python-developer-root-info-solutions-delhi-delhi-ncr-2-to-3-yrs-jobid-fny4oGqOeQZzpSvf__PLUS__uAgZw==&source=srp"
    },
    {
        "company name": "DREAMAJAXTECHNOLOGIES",
        "skills": "python,django,api,sql,nosql",
        "more info": "https://www.timesjobs.com/job-detail/python-developer-dreamajax-technologies-bengaluru-bangalore-4-to-7-yrs-jobid-EWIVCDzRLKBzpSvf__PLUS__uAgZw==&source=srp"
    },
    {
        "company name": "destinyhrgroupservices",
        "skills": "fundamentals,python,css,javascript,jquery,database,django,java,json,html",
        "more info": "https://www.timesjobs.com/job-detail/python-developer-destiny-hr-group-services-gurgaon-0-to-1-yrs-jobid-ZBPXkQ5iEPBzpSvf__PLUS__uAgZw==&source=srp"
    },
    {
        "company name": "day1technologies",
        "skills": "rest,python,django,git,postgresql,sql,docker",
        "more info": "https://www.timesjobs.com/job-detail/python-developer-day1-technologies-bengaluru-bangalore-2-to-3-yrs-jobid-wnkkahyN0x9zpSvf__PLUS__uAgZw==&source=srp"
    },
    {
        "company name": "xoniertechnologiespvtltd",
        "skills": "python,django,testingtools,debugging,storage",
        "more info": "https://www.timesjobs.com/job-detail/python-developer-xonier-technologies-pvt-ltd-noida-greater-noida-2-to-5-yrs-jobid-VZ3nXzqL2FNzpSvf__PLUS__uAgZw==&source=srp"
    },
    

    # Add more job posts as needed
]

# Specify the path where you want to save the .json file
json_file_path = "json1.json"

# Write the job posts to the .json file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(job_posts, json_file, indent=2)  # indent for pretty formatting (optional)
