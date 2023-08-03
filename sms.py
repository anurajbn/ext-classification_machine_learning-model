import stremlit as st
import pickle
import nltk

tfidf = pickel.load(open('vectorizer.pkl','rb'))
model = pickel.load(open('model.pkl','rb'))


st.title("Email/SMS spam classifier")

input_sns = st.text_input("Enter the message")


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    for i in text
        if i.isalnum():
            y.append(i):

    text = y[:]
    y.claer()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            text = y[:]


y.claer()

for i in text:
    y.append(ps.stem(i))
return " ".join(y)


transfrom_sms = transform_text(input_sns)

vector_input = tfidf.transform([transform_sns])

result = model.predict(vector_input)[0]

if result ==1:
    st.header("Spam")
else:
    st.header("Not Spam")