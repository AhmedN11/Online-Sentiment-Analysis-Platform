# Online-Sentiment-Analysis-Platform
In this project, I made a basic Sentiment analysis web app based on Machine Learning.

Data used for this project is available on Kaggle : <a href="https://www.kaggle.com/datasets/cosmos98/twitter-and-reddit-sentimental-analysis-dataset?select=Twitter_Data.csv" target="_blank">Twitter and Reddit Sentimental analysis Dataset</a>.

Here is my <a href="https://www.linkedin.com/in/nani-ahmed/" target="_blank">LinkedIn Profile</a>.

My email address : <a href="mailto:ahmednani015@gmail.com">ahmednani015@gmail.com</a>.

## Presentation of the web app
Here is a demo of the app :
You insert the text youwant to classify and let the rest unfold :
Here's an example of a 
![](https://i.imgur.com/qFvCZlS.png)

![](https://i.imgur.com/DMPC7MY.png)
</br>
</br>
![](https://i.imgur.com/gPIFn7a.png)
![](https://i.imgur.com/zqd28x8.png)
</br>
</br>![](https://i.imgur.com/6tPbfmS.png)![](https://i.imgur.com/UOyF42d.png)
</br>
</br>
# Text Processing

Data preprocessing is an essential step in building a Machine Learning model and depending on how well the data has been preprocessed; the results are seen.

In NLP, text preprocessing is the first step in the process of building a model.

The various text preprocessing steps done in this project are:

1.  Tokenization
2.  Lower casing
3.  Stop words removal
4.  Stemming

## 1.  Tokenization

The process of breaking down a text into smaller units called tokens, such as words, phrases, symbols, and other elements.

## 2.  Lower casing

The process of converting all the characters in a text to lowercase. (NLP -> nlp).  
Words like _Book_ and _book_ mean the same but when not converted to the lower case those two are represented as two different words in the vector space model (resulting in more dimensions).

## 3.  Stop words removal

The process of removing words that are commonly used in a language but do not contribute significantly to the meaning of the text, such as "the", "a", and "an".

## 4.  Stemming

The process of reducing inflected (or sometimes derived) words to their word stem, base, or root form—generally a written word form.

<br>
<br>

### Update : I packaged this app into a Docker image and pushed it to a [DockerHub Repository](https://hub.docker.com/repository/docker/ahmednani/sentiment-analysis-web-app/general)
<br>
To pull and run this image locally you can execute the following lines (docker login required):<br>
```docker pull ahmednani/sentiment-analysis-web-app```
<br>then :<br>
```docker run -p 5000:5000 -d ahmednani/sentiment-analysis-web-app```

<br>and the web app should be up in [localhost](https://localhost:5000)
