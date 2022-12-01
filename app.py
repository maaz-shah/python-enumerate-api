
from xml.etree.ElementTree import tostring
from flask import Flask, jsonify, abort
from flask_httpauth import HTTPBasicAuth
import boto3
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sys
import json

class MissingEnvironmentVariable(Exception):
    pass

try:
    access_key =os.environ['ACCESS_KEY']
except KeyError:
    raise MissingEnvironmentVariable(f"{ACCESS_KEY} does not exist")

try:
    secret_key = os.environ['SECRET_KEY']
except KeyError:
    raise MissingEnvironmentVariable(f"{SECRET_KEY} does not exist")

try:
    bucket_name = os.environ['S3_BUCKET_NAME']
except KeyError:
    raise MissingEnvironmentVariable(f"{S3_BUCKET_NAME} does not exist")

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("password"),
    "demo": generate_password_hash("demo")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
def get_s3():
  list = []
  session = boto3.Session(
         aws_access_key_id=access_key,
         aws_secret_access_key=secret_key)
#Then use the session to get the resource
  s3 = session.resource('s3')
  my_bucket = s3.Bucket(bucket_name)
  for my_bucket_object in my_bucket.objects.all():
      list.append(my_bucket_object.key)
  return jsonify(list)

#@app.route('/count')
#@auth.login_required
#def get_s3_count():
#  list = []
#  session = boto3.Session(
#         aws_access_key_id=access_key,
#         aws_secret_access_key=secret_key)
##Then use the session to get the resource
#  count = 0
#  s3 = session.resource('s3')
#  my_bucket = s3.Bucket(bucket_name)
#  for my_bucket_object in my_bucket.objects.all():
#      count = count + 1
#  return jsonify(count)


if __name__ == "__main__":
    app.run(debug=True)
    