#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import boto3

client = boto3.client("s3")
client.download_file("rrf-factory-log", "README.md", "README2.md")
