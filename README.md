
![bitcoin2](https://user-images.githubusercontent.com/57894655/179397164-6db4dbe0-ee5b-4bab-87e4-bfd236943f50.jpg)

# Docker-Final-Task : BitCoin

- This project is a  Python Web APP that Presents the Current BitCoin Price in localhost:8000 and Presents the Average Price for the last 10 minutes in localhost:8000/avg

** Dockerizing the applications was done by Dockerfile and docker-compose.yml 
** Using Jenkinsfile for CI/CD that creates and pushes the generated Web application Docker image to Docker Hub

## Run Locally

Clone the project
```bash
  git clone https://github.com/jumana-abuhattoom/Docker-Final-Task.git
```

Go to the project directory

```bash
  cd Docker-Final-Task
```

Build

```bash
  docker compose up
```

Call the API from your browser or using curl at  [http://localhost:8000](http://localhost:8000) in order to See the Current BitCoin Price and   [http://localhost:8000/avg](http://localhost:8000/avg) to see the  Average Price in the last 10 minutes.


---------------------
in order to stop the application run the command:  
```bash 
docker compose down
```

