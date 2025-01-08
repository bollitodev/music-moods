class FacialExpressionRecognitionModel:
    def __init__(self):
        self.emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

    def predict(self, image):
        prediction = 3
        return self.emotions[prediction]

    def get_emotions(self):
        return self.emotions

    def get_emotion(self, index):
        return self.emotions[index]

    def get_emotion_index(self, emotion):
        return self.emotions.index(emotion)