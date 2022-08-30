import pandas as pd
from gravityai import gravityai as grav 
import pickle

model = pickle.load(open('financial_text_classifier', 'rb'))
tfidf_vectorizer = pickle.load(open('financial_text_vectorizer', 'rb'))
label_encoder = pickle.load(open('financial_text_encoder', 'rb'))

def process(inPath, outPath):
    #Read input file 
    input_df = pd.read_csv(inPath)
    #Vectorize the data 
    features = tfidf_vectorizer.transform(input_df['body'])
    #Predict the classes   
    predictions = model.predict(features)
    #Convert output labels to categories 
    input_df['category'] = label.encoder.inverse_transform(predictions)
    #Save results to csv 
    output_df = input_df[['id', 'category']]
    output_df.to_csv(outPath, index=False)

grav.wait_for_requests(process)
