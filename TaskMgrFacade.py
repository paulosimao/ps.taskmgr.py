from pymongo import MongoClient
from bson import ObjectId


class TaskMgrFacade:
    keysArray = []
    itemsArray = []

    def __init__(self):
        self.client = MongoClient()
        self.col = self.client.tasks.tasks

    def getTasks(self):
        self.keysArray = []
        ret = []
        for doc in self.col.find():
            self.keysArray.append(doc['_id'])
            ret.append(doc)
        return ret

    def inserTask(self, t):
        ret = self.col.insert(t)
        self.keysArray.append(ret)
        return ret

    def createNew(self) -> dict:
        d = {"completed": False, "desc": "New Task"}
        id = self.inserTask(d)  # type : ObjectId
        d['_id'] = id
        return d

    def deleteOne(self, id):
        objid = self.keysArray[id]
        self.keysArray.remove(objid)
        self.col.delete_one({"_id": objid})

    def updateOne(self, id, fname, fval):
        self.col.update({"_id": self.keysArray[id]}, {"$set": {fname: fval}})

    def getTaskDetails(self, id):
        ret = self.col.find_one({"_id": self.keysArray[id]})
        return ret
