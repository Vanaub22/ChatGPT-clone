from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
app=Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://anuvab_c:mymongodbatlas@cluster1.yf5gded.mongodb.net/chatgpt_clone"
mongo = PyMongo(app)

@app.route("/")
def home():
    chats=mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html",myChats=myChats)


@app.route("/api",methods=["GET","POST"])
def qa():
    if request.method=="POST":
        print(request.json)
        question=request.json.get("question")
        chat=mongo.db.chats.find_one({"question":question})
        print(chat)
        if(chat):
            data={"result":f"{chat['answer']}"}
            return jsonify(data)
        else:
            data={"result":f"Answer of {question}"}
            mongo.db.chats.insert_one({"question": question, "answer":f"answer from openai for {question}"})
            return jsonify(data)
    data={"result":"oh yeah!!"}
    return jsonify(data)


app.run(debug=True)
