# CI-CD



## Getting started
This project is being developed as part of a master's degree course focused on microservices. For this project, I have been instructed to create multiple microservices with a server and a database, which will later be deployed to a self-hosted platform such as Coolify or Cloudron.

Along the way, a CI/CD pipeline will also be implemented, along with multiple technical features such as documentation (Swagger), security (HTTPS), and tests (unit tests, container tests, load tests).

I will continue to update this README to provide better visibility and understanding of the project.

## Set Up 
Now to get the project up and running you can either clone the repo and set up run the docker compose locally and build the docker compose, or you can simply get the images from the docker hub (registry) and run them on the same network
with the following command 

``` docker pull hannachiyou/myapp:latest ``` 

``` docker pull hannachiyou/mybd:latest ``` 

You can also find them here in the registry
[Docker hub images](https://hub.docker.com/repositories/hannachiyou)

## CI/CD  
On the .github/workflows now we can see a pipeline that we created with two jobs one for the tests , one for the build and push docker images --> this will be updated later on. 
Now as required and for testing purposes we used the **act** command to simulate this locally before triggering the workflow , you can see it in action bellow: 
![Act in action 1](screens/act 1.PNG)
![Act in action 2](screens/act 2.PNG)
![Act in action 3](screens/act 3.PNG)
![Act in action 4](screens/act 4.PNG)


