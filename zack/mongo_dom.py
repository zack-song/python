import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["wap_data"]
mycol = mydb["im_talk_list"]

for x in mycol.find():
    print(x)