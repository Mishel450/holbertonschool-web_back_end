#!/usr/bin/env python3
"""task-12"""
import pymongo


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mongo_collection = client.logs.nginx
    the_list = mongo_collection.find()
    method_GET = 0
    method_POST = 0
    method_PUT = 0
    method_PATCH = 0
    method_DELETE = 0
    status_count = 0
    for i in the_list:
        the_method = i['method']
        if the_method == 'GET':
            method_GET += 1
        if the_method == 'POST':
            method_POST += 1
        if the_method == 'PUT':
            method_PUT += 1
        if the_method == 'PATCH':
            method_PATCH += 1
        if the_method == 'DELETE':
            method_DELETE += 1
    the_list_of_GETS = mongo_collection.find({"method": "GET"})
    for i in the_list_of_GETS:
        if i['path'] == '/status':
            status_count += 1
    print("{} logs".format(len(the_list)))
    print("Methods:")
    print("\tmethod GET:{}".format(method_GET))
    print("\tmethod POST:{}".format(method_POST))
    print("\tmethod PUT:{}".format(method_PUT))
    print("\tmethod PATCH:{}".format(method_PATCH))
    print("\tmethod DELETE:{}".format(method_DELETE))
    print("{} status check".format(status_count))
