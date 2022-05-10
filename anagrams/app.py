from flask import Flask, render_template

app = Flask(__name__)
f = open('words.txt')
word_list=f.read().splitlines()

@app.route("/words/")

@app.route("/words/<string:word>")
def words(word):
    list1=[]
    for w in word_list:
        if sorted(w.upper())==sorted(word.upper()):
            list1.append(w)

    return render_template('template1.html', word=word, list1=list1)

