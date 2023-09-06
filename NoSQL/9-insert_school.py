#!/usr/bin/env python3
"""task-9"""
import pymongo
import uuid


def insert_school(mongo_collection, **kwargs):
    """creates a list and inserts a new document"""
    the_dict = {}
    new_id = uuid.uuid4()
    for key, value in kwargs.items():
        the_dict[key] = value
    the_dict['_id'] = new_id
    mongo_collection.insert_one(the_dict)
    return new_id
