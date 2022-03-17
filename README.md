<h1 align="center">URL Shortener</h1>

---


## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Built Using](#built_using)
- [Running the tests](#tests)
- [API Documentation](#usage)
- [Deployment](#deployment)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

The URL Shortener is a program which takes a Long URL in input and provides a Short URL in output. 
This Program uses MongoDB to Store Data Permanently in Key value pairs. But also uses Memcached to Store Data in Cache Memory for Faster Access.
The Documentation of APIs will be found at [API Documentation](#usage)

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [Deployment](#deployment) for notes on how to deploy the project on a Local System or on a Kubernetes Server.

### Prerequisites

To run the URL Shortener on Local System, first we need to install following Software Dependencies.

- [Python 3](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)

Once above Dependencies are installed we can move with [further steps](#installing)

### Installing <a name = "installing"></a>

A step by step series of examples that tell you how to get a development env running.

#### Step 1: Install Project related Dependencies
```
pip3 install -r requirements.txt
```

#### Step 2: Running Memcached Server & MongoDB on Docker
```
docker-compose -f ./deployment-files/dependency-docker-compose.yml up
```

#### Step 3: Setting Up Environmental Variables

Set up the Environmental variables according to your needs. The Application will run with defaults as mentioned in the following table

| Environmental Variable | Usage                              | Default Values |
|------------------------|------------------------------------|----------------|
| APP_RELOAD             | Reload App on Changes              | True           |
| APP_HOST               | Host where Application Runs        | 0.0.0.0        |
| APP_PORT               | Port on which Application Runs     | 5000           |
| APP_WORKERS            | Number of Application Workers      | 1              |
| MEMCACHED_HOST         | Host where Memcached is Running    | localhost      |
| MEMCACHED_PORT         | Port on which Memcached is Running | 11211          |
| MONGODB_HOST           | Host where MongoDB is Running      | localhost      |
| MONGODB_PORT           | Host where MongoDB is Running      | 27017          |
| MONGODB_DB             | Database Name                      | infracloud_db  |
| MONGODB_COLLECTION     | Collection Name                    | url_shortner   |



#### Step 4: Run the Python Code
```
python3 run.py
```

## 🔧 Running the tests <a name = "tests"></a>

To Run the Test Cases, Open a terminal in the Project and run following command
```
pytest
```

## 📃 API Documentation <a name="usage"></a>

Here are the API Endpoint used in this Project

- To Get the Shortened URL for Long URL

```
ENDPOINT: /{short_url}
REQUEST TYPE: GET
PATH PARAMETERS: short_url
RESPONSES:
  200: 
    Redirect to the Long URL
  
  404:
    {
      "message": "No Long URL found for localhost:5000/tstng"
    }
```

```
ENDPOINT: /get-shortened-url
REQUEST TYPE: GET
QUERY PARAMETERS: long_url
RESPONSES:
  200: 
    {
      "message": "Short URL Found for www.testlongurl.com",
      "short_url": "if.cld/kj2bU1bWof"
    }
  
  404:
    {
      "message": "No Shortened URL found for www.testlongurl.com"
    }
```

- To Create Shortened URL
```
ENDPOINT: /create-shortened-url
REQUEST TYPE: POST
BODY:
  Example 1: With Preferred Short URL
    {
      "long_url": "http://www.testlongurl.com",
      "preferred_short_url": "tstng"
    }
  Example 2: Without Preferred Short URL
    {
      "long_url": "http://www.testlongurl.com"
    }
RESPONSES:
  201: 
    {
      "message": "Short URL created for www.testlongurl.com",
      "short_url": "if.cld/tstng"
    }
    OR
    {
      "message": "Short URL created for www.testlongurl.com",
      "short_url": "if.cld/kj2bU1bWof"
    }
    OR
    {
      "message": "Couldn't create Preferred Short URL for www.testlongurl.com as it already exists in our systems",
      "short_url": "if.cld/kj2bU1bWof"
    }
  409:
    {
      "message": "Short URL already there for www.testlongurl.com",
      "short_url": "if.cld/tstng"
    }
```
To check & Test the Supported Endpoints, and it's documentation, Run the Project and kindly use any of the methods mentioned below

#### For Swagger UI Documentation
```
localhost:5000/docs
```

#### For Redoc Documentation
```
localhost:5000/redoc
```

## 🚀 Deployment <a name = "deployment"></a>

[Note]: In Order to Deploy the Project, Docker must be running on the Local System, and if any project related pods are running previously, Stop/Remove them<br><br>
To Deploy whole Application with all Dependencies on Local System,  kindly run the below command

```
docker-compose -f ./deployment-files/deploy-project-localhost.yml up
```

In order to deploy the Project on a Kubernetes Server kindly follow below steps:
```
kubectl create -f ./deployment-files/mongodb-deployment.yaml
```
```
kubectl create -f ./deployment-files/memcached-deployment.yaml
```
```
kubectl create -f ./deployment-files/application-deployment.yaml
```

API Host will be exposed on the URL Provided by LoadBalancer of the Server

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Memcached](https://memcached.org/) - Caching
- [Python 3](https://www.python.org/) - Backend
- [Fast API](https://fastapi.tiangolo.com/) - API Framework
- [Docker](https://www.docker.com/) - Containers Solution

## ✍️ Authors <a name = "authors"></a>

- [@r4rajat](https://github.com/r4rajat) - Idea & Implementation

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- References
  - https://fastapi.tiangolo.com/tutorial/query-params/
  - https://fastapi.tiangolo.com/tutorial/body/
