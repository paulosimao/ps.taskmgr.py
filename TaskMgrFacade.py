from pymongo import MongoClient
from bson import ObjectId
import json


class TaskMgrFacade:
    def __init__(self):
        with open('config.json') as data_file:
            self.data = json.load(data_file)
        self.client = MongoClient(self.data['dburl'])
        self.col = self.client.tasks.tasks

    def getTasks(self):
        ret = []
        for doc in self.col.find():
            ret.append(doc)
        return ret

    def inserTask(self, t):
        ret = self.col.insert(t)
        return ret

    def createNew(self) -> dict:
        d = {"completed": False, "desc": "New Task"}
        id = self.inserTask(d)  # type : ObjectId
        d['_id'] = id
        return d

    def deleteOne(self, id):
        self.col.delete_one({"_id": ObjectId(id)})

    def updateOne(self, id, fname, fval):
        self.col.update({"_id": ObjectId(id)}, {"$set": {fname: fval}})

    def getTaskDetails(self, id):
        ret = self.col.find_one({"_id": ObjectId(id)})
        return ret
