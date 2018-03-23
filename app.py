
from flask import Flask
import sys
import os
import boto3

os.environ['aws_access_key_id'] = 'bla'
os.environ['aws_secret_access_key'] = 'bla2'

app = Flask(__name__)


ddb = boto3.client('dynamodb',
                    endpoint_url='http://localhost:8000',
                    region_name='blabla',
                    aws_access_key_id='wow',
                    aws_secret_access_key='wow2',
                    aws_session_token='wow3'
                    )


@app.route("/")
def hello():

    print("hello Gabriel", file=sys.stderr)
    return "Hi Gabriel!"


@app.route("/peek")
def peek():

    tables = list(ddb.list_tables())

    print('tables:' ,tables, file=sys.stderr)

    return "peeking"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
