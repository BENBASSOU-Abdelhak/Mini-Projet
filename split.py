from utility.cross_validation import split_5_folds
from configx.configx import ConfigX
import os 

if __name__ == "__main__":
    configx = ConfigX()
    configx.k_fold_num = 5 
    configx.rating_path = "data/ratings_data.txt"
    configx.rating_cv_path = "../data/cv/"
    print(configx.rating_path)
    split_5_folds(configx)