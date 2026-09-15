import pandas as pd
import numpy as np

raw_rows = [
    {"name": " Amara ", "scores": "92,85,78"},
    {"name": "Leo", "scores": "88,91,73"},
    {"name": "Priya", "scores": "65,72,150"},         
    {"name": "Sam", "scores": "70,not_a_number,60"},  
    {"name": "Amara", "scores": "95,90,88"},          
    {"name": "Jade", "scores": "81,77,84,90"},
]

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.locked = False

        valid_scores = []
        for s in scores:
            if not (0 <= s <= 100):
                raise InvalidScoreError(f"Score {s} is out of bounds (0-100).")
            valid_scores.append(s)
            
        if not valid_scores:
            raise InvalidScoreError("No valid scores provided.")
            
        self.scores = np.array(valid_scores)






