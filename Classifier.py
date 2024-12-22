import pickle

def load_and_predict(input_text):
    
    with open('Task_Classifier.pkl', 'rb') as file:
        model = pickle.load(file)

    input_text = input_text.replace('[^a-zA-Z0-9\s]', '')
    prediction = model.predict([input_text])

    
    return prediction[0]



