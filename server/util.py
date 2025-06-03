import json
import pickle
import numpy as np

__columns = None
__location = None
__model = None


def load_saved_artifacts():
    print("Loading artifacts:")
    global __columns
    global __location
    global __model

    with open('./BHP/server/artifacts/columns.json','r') as  f:
        __columns = json.load(f)['data_columns']
        __location = __columns[3:]

    with open('./BHP/server/artifacts/Price_Prediction_Model.pickle','rb') as f:
        __model = pickle.load(f)

    print("Loading artifacts done")


def get_location_names():
    return __location

def get_data_columns():
    return __columns

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__columns))
    x[0] = sqft 
    x[1] = bhk
    x[2] = bath

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


if __name__=="__main__":
    load_saved_artifacts()
    get_location_names() 
    print(get_estimated_price('1st Phase JP Nagar',1000,2,2))
