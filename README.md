# extractsentiments

This is a simple webapp built in Flask to extract the sentiment from text data, it computes the sentiment based on individual sentences in a paragraph and returns the average of it.

We are using TextBlob for detecting sentiments from text which is an open-source.

If the average of sentiment received is >= 0.5:
  return Positive
elif the average of sentiment is <= -0.5:
  return Negative
elif average of sentiment is >0.5 and <-0.5:
  return Neutral



