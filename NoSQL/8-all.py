#!/usr/bin/env python3
"""task-8"""
import pymongo


def list_all(mongo_collection):
    """list all the items in a collection"""
    the_collection = mongo_collection.find()
    the_list = []
    for i in the_collection:
        the_list.append(i)
    return the_list
