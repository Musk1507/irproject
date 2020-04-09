from flask import Flask
from grading import gradingFunction 
from summarize import generate_summary
app = Flask(__name__)

@app.route('/')
def hello_world():
    ranked_sentence,summary = generate_summary( "essay3.txt", 5)
    marks,mispelled,vocab = gradingFunction("essay3.txt","dataset.txt")
    return '''
    <!DOCTYPE html>
    <head>
    <title>ARSG</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    </head>
    <style>
    html,body,h1,h2,h3,h4,h5,h6 {font-family: "Roboto", sans-serif;}
    h1,h2,h3,h4 {color: Teal;}
    </style>
    <body style="width: 880px; margin: auto; background-color: GhostWhite;">
        <h1><center>Automated Essay Summarization and Grading</center></h1>
        <p><h4>Ranked sentences:</h4> '''+str(ranked_sentence)+''' </p>
        <p><h4>Summary:</h4> '''+str(summary)+''' </p>
        <p><h4>Grade:</h4> You have scored: '''+str(round(marks,1))+'''/10</p>
        <p>These are the spelling mistakes you have made: '''+str(mispelled)+''' </p>
        <p>These are some good vocabulary terms that you have been graded on: '''+str(vocab)+''' </p>
    </body>
    </html>
    '''
    

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port = 5000)