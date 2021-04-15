from flask import render_template, Request, Flask, request, redirect
from textblob import TextBlob


app = Flask(__name__)

def extract_sentiment(text):
    blob = TextBlob(text)
    senti_value = 0
    for sentence in blob.sentences:
        senti_value += sentence.sentiment.polarity

    overall_sentiment = senti_value/len(blob.sentences)

    if overall_sentiment<=-0.5:
        return "Negative"
    elif overall_sentiment >=0.5:
        return "Positive"
    elif overall_sentiment>-0.5 and overall_sentiment<0.5:
        return "Neutral"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        textvalue = request.form['w3review']
        sentiment = extract_sentiment(textvalue)
        # return redirect('/sentimentanalysis/'+sentiment)
        return render_template("sentiment.html", sentiment=sentiment)
    return render_template('index.html')

# Download API
# @app.route("/sentimentanalysis/<sentiment>", methods = ['GET', 'POST'])
# def sentiment_value(sentiment):
#     return render_template('sentiment.html', value=sentiment)


if __name__ == "__main__":
    app.run(debug=False, threaded=True)
