# Random User Connector

**Goal**: The goal of this application was to develop a connector (Job Scheduler) task that fetch user from https://randomuser.me/api and save into Database (PostgreSQl) periodically.

**Backend**: The tech-stack used to develop backend of this application is Python Django (Django Rest Framework), Celery, Celery-beat, PostgreSQl.

**Frontend**: The tech-stack used to develop frontend of this application is Vue.js.

**Containerization**: Also docker and docker-compose is used to containerize the whole application.

## To Run on Local Machine:

-   You should have docker and docker-compose installed on your machine.
-   Open `terminal` in the project folder and execute the following command: `docker-compose up -d --build`
-   The frontend will start running on **http://localhost:8080/** and backend api will be running on **http://127.0.0.1:8000/api/users**
-   The default port is set to be **8080**, you can change that in docker-compose fime.

**Note**: Detailed Documentation is available in frontend and backend appliation folders

Following are the Screenshots attached:
    ![01](/screenshots/01.png)
    ![02](/screenshots/02.png)
    ![03](/screenshots/03.png)
    ![04](/screenshots/04.png)

**Deployment**: 

Due to time shortage, I didn't deploy it on any platform. But we can deploy the basic application using AWS Infrastructure. i.e EC2/AWS Elastic Beanstalk for the backend, cdn of static webapp using Amazon CloudFront, Amazon RDS for Db and route53 for the url management. Also to scale the application as per traffic, we can use AWS Auto Scaling.
 
