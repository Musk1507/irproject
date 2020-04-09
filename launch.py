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
    <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
    </head>
    <body style="width: 880px; margin: auto;">  
        <h1>Automated Essay Summarization and Grading</h1>
        <p>Ranked sentences: '''+str(ranked_sentence)+''' </p>
        <p>Summary: '''+str(summary)+''' </p>
        <p>You have scored: '''+str(round(marks,1))+''' on 10</p>
        <p>These are the spelling mistakes you have made: '''+str(mispelled)+''' </p>
        <p>These are some good vocabulary terms that you have been graded on: '''+str(vocab)+''' </p>
    </body>
    </html>
    '''
    

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port = 5000)