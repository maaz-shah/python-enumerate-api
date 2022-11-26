## Overview

A super simple RESTful api created using Flask. The app will list all the contents in the S3 bucket parsed via env variable.

## Create .env file
```
ACCESS_KEY=XXXXXX
SECRET_KEY=XXXXX
S3_BUCKET_NAME=XXXX
```
## Build Docker image using Dockerfile
Build the docker image using

```sh
docker build -t python-sample-api:0.1.0 .
```
## Run the container 
```sh
docker run --env-file .env -it --rm  -p 5000:5000 python-enumrate-api:0.1.0
```
## Non Docker method 

Requirements:

```sh
python -m venv ./venv
source .venv/bin/activate
```

Next, run

```sh
pip install -r requirements.txt
```

to get the dependencies.

Finally run the api with

```sh
python api.py
```

## Example

Flask will run on http://127.0.0.1:5000/.
