from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
data ={
    
        "message":["hello bro",
        "how are you",
        "you win price",
        "you win offer",
        "offer loan from bajaj finance",
        "data percentage",
    
    ],
    
        "labels":["spam",
        "harm",
        "spame",
        "harm",
        "spam",
        "harm",
    ]
}
dataframe =pd.DataFrame(data)
vectorize =CountVectorizer()
x =vectorize.fit_transform(dataframe["message"])
y =dataframe["labels"]
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=42)
model =MultinomialNB()
model.fit(x_train,y_train)
predict =model.predict(x_test)
accuracy =accuracy_score(y_test,predict)
print("accuracy_score:",accuracy)
msg =input("Enter the your message to detected spam or harms:")
vector =vectorize.transform([msg])
predict =model.predict(vector)
print("label:",predict)
