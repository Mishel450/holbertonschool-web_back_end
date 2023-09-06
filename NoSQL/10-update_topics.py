#!/usr/bin/env python3
"""task-10"""
import pymongo
import uuid


def update_topics(mongo_collection, name, topics):
    """changes the topics of a document"""
    mongo_collection.update_all({"name": name}, {"$set": {"topics": topics}})
