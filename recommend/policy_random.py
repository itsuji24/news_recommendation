import random
import numpy as np


class PolicyRandom():
    def __init__(self):
        pass
		
    def set_articles(self, articles):
        pass
                        
    def recommend(self, timestamp, user_features, articles):
        return random.choice(articles)
    
    def update(self, reward):
        pass