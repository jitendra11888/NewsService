from flask import Flask, jsonify, request   
import mysql.connector

app=Flask(__name__)   

con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jitu@techM',
    database='kmpdatabase')

@app.route('/getArticles', methods=['GET'])
def get_articles():
    cursor = con.cursor(dictionary=True)
    cursor.execute("Select *From articles;")
    articles = cursor.fetchall()
    cursor.execute("Select *From sources;")
    sources = cursor.fetchall()

    
    for article in articles: 
        article["source"] = [source for source in sources ]
    
    cursor.close()
    con.close()

    return jsonify({"articles": articles}),200

if __name__ == "__main__":
    print("Server started at http://localhost:5000")
    app.run(debug=True)

