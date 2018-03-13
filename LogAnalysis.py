from flask import Flask, request, redirect, url_for
from flask import render_template
from LogQuery import popArticle, popArtAuthor, logErrPerc
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def showReportOpt():
    """ This function displays the home page for reporting options. """
    return render_template('showReportOpt.html')


@app.route('/getReport/<int:Report_id>', methods=['GET', 'POST'])
def getReport(Report_id):
    """ This function calls function for the selected report by user. """
    if Report_id == 0:
        items = popArticle()
    elif Report_id == 1:
        items = popArtAuthor()
    elif Report_id == 2:
        items = logErrPerc()
    return jsonify(data=items)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
