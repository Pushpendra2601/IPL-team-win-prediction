import pickle

filename='model.pkl'
model= pickle.load(open(filename,'rb'))

print (model)
    
