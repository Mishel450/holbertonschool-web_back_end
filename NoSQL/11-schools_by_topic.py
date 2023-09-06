#!/usr/bin/env python3
"""task-10"""
import pymongo
import uuid


def schools_by_topic(mongo_collection, topic):
    """finds documents and returns it with the topic"""
    the_collection = mongo_collection.find({"topics": topic})
    the_list = []
    for i in the_collection:
        the_list.append(i)
    return the_list
