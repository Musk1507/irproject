from flask import Flask, request
from grading import gradingFunction 
from summarize import generate_summary
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>AESG</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    </head>
    <style>
        html,body,h1,h2,h3,h4,h5,h6 {font-family: "Roboto", sans-serif;}
        h1,h2,h3,h4 {color: Teal;}
    </style>
    <body style="width: 880px; margin: auto; background-color: GhostWhite;">
        <br><h1><center>Automated Essay Summarization and Grading</center></h1>
        <form action="/grade">
            <br>
            <h4>Enter your essay here:</h4><br>
            <textarea rows = "10" cols = "120" name = "essay">
            </textarea><br><br>
            <div align= "right"><button type="submit">Submit</button></div>
        </form>
    </body></html>
    """


@app.route('/grade')
def summarize_grade():
    essay = request.args.get('essay', 'World')
    ranked_sentence,summary = generate_summary(essay, 5)
    marks,mispelled,vocab,flg = gradingFunction(essay,"dataset.txt")
    if flg == 1:
        length = "The essay you have typed is not of the appropriate size"
    else:
        length = "The length of your essay is perfect"
    return '''
    <!DOCTYPE html>
    <head>
    <title>AESG</title>
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
        <p><h4>Initial Essay:</h4> '''+essay+''' </p>
        <p><h4>Ranked sentences:</h4> '''+str(ranked_sentence)+''' </p>
        <p><h4>Summary:</h4> '''+str(summary)+''' </p>
        <p><h4>Grade:</h4> You have scored: '''+str(round(marks,1))+'''/10</p>
        <p>These are the spelling mistakes you have made: '''+str(mispelled)+''' </p>
        <p>These are some good vocabulary terms that you have been graded on: '''+str(vocab)+''' </p>
        <p>'''+length+''' </p>
    </body>
    </html>
    '''
    

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port = 5000)