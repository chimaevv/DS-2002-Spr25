#!/bin/bash

apt update -y
apt upgrade -y

apt install -y python3 git python3-boto3

python3 --version > /tmp/bootstrap_verification.log 2>&1
git --version >> /tmp/bootstrap_verification.log 2>&1
python3 -c "import boto3; print('boto3 version:', boto3.__version__)" >> /tmp/bootstrap_verification.log 2>&1
