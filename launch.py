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
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    </head>
    <style>
        html,body,h1,h2,h3,h4,h5,h6 {font-family: "Roboto", sans-serif;}
        h1,h2,h3,h4 {color: Teal;}
    </style>
    <body style="width: 880px; margin: auto;">
        <br><blockquote class="blockquote text-center"><p class="mb-0"><h1>Automated Essay Summarization and Grading</h1></p>
        <footer class="blockquote-footer">AESG</footer>
        </blockquote>
        <div class="alert alert-light" role="alert">
            For some, writing an essay is as simple as sitting down at their computer and beginning to type. But, a lot more planning goes into writing an essay successfully. If you have never written an essay before, or if you struggle with writing and want to improve your skills, you have come to the right place. AESG is a software that will cretique your essay immediatley and help you improve your essay writing skills.
        </div>
        <form action="/grade">
            <br>
            <h4>Enter your essay here:</h4><br>
            <div class="alert alert-warning" role="alert">
            Please note: Your essay must be greater than 250 words but must not exceede 500 words, also do not leave any extra spaces before or after your essay.
            </div><br>
            <textarea rows = "10" cols = "120" class="form-control" name = "essay"></textarea><br><br>
            <div align= "right"><button type="submit" class="btn btn-success">Submit</button></div>
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
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    </head>
    <style>
    html,body,h1,h2,h3,h4,h5,h6 {font-family: "Roboto", sans-serif;}
    h1,h2,h3,h4 {color: Teal;}
    </style>
    <body style="width: 880px; margin: auto">
        <p><h4>Initial Essay:</h4> '''+essay+''' </p>
        <p><h4>Ranked sentences:</h4> '''+str(ranked_sentence)+''' </p>
        <div class="alert alert-success" role="alert">
            Your essay has been summarized succesfully
        </div>
        <p><h4>Summary:</h4> '''+str(summary)+''' </p>
        <div class="alert alert-success" role="alert">
            Your essay has been graded succesfully
        </div>
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