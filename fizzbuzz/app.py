from flask import Flask, render_template

app = Flask(__name__)

@app.route("/fizzbuzz/")
#set default number 

@app.route("/fizzbuzz/<int:number>")
def start(number=-1):
    n=0
    l = []
    while 0<=n<number:
        n=n+1
        if n%3==0 and n%5==0:
            l.append('Fizzbuzz')
        elif n%3==0 and n%5!=0:
            l.append('Fizz')
        elif n%3!=0 and n%5==0:
            l.append('Buzz')
        else:
            l.append(n)

    return render_template('adventure.html', number=number, list1=l)

