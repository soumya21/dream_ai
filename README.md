# AILA
This project is for creating a generative AI-powered Leave Assistant chatbot for the CBA office contest 

AILA is a AI driven Leave assistant which can do below assistance.

1. Understand Leave Policies: Offer comprehensive explanations of the organization’s leave policies, including types of leaves available (e.g., annual leave, sick leave, parental leave), accrual rates, and eligibility criteria.

2. Track Available Leaves: Display the current leave balance, including a breakdown of leave types, ensuring employees are always informed about their leave status.

3. Automated Leave Application: Allow employees to apply for leaves seamlessly through natural language commands, without the need to log into the Workday/HCM application. The AI assistant will interface with the underlying HR systems to submit leave requests automatically, enhancing user experience and reducing administrative overhead.

4. Other HR-related tasks: retrieve leave balance, draw summary of individual span/size by various levels.


Technology Stack
 

Storage : S3

DB : RDS

Programming languages : Python, html , CSS

AWS services : Lambda , Bedrock, S3, IAM, RDS, Cloud watch
1. pip install fastapi uvicorn
2. pip install python-multipart
3. pip install pydantic-settings
4. pip install python-jose[cryptography]
5. pip install passlib[bcrypt]
6. pip install pydantic-settings
7. pip install python-multipart
8. pip install boto3
9. pip install jinja2
10. pip install sqlalchemy
11. pip install pymysql
12. pip install pydantic[email]

****command to run the service****
```uvicorn app.main:app --reload``` 
