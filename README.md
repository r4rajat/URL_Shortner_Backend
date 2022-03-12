<h1 align="center">URL Shortener</h1>

---

<p align="center"> URL Shortener for InfraCloud Round 1.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

The URL Shortener is a program which takes a Long URL in input and provides a Short URL in output. 

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

To run the URL Shortener on Local System, first we need to install following Software Dependencies.

- [Python 3](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)
- [MongoDB](https://www.mongodb.com/try/download/community)

Once above Dependencies are installed we can move with [further steps](#installing)

### Installing <a name = "installing"></a>

A step by step series of examples that tell you how to get a development env running.

#### Step 1: Install Project related Dependencies
```
pip3 install -r requirements.txt
```

#### Step 2: Running Memcached Server on Docker
```
docker-compose -f memcached-docker-compose.yml up
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

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 📃 API Documentation <a name="usage"></a>
#### For OpenAPI Documentation
```
<host>:<port>/docs
Ex: localhost:5000/docs
```


## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

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
