import pickle
import json
import os
import app.CONFIG as path


class Prediction():
    def __init__(self,data):
        self.data = data


    def load_raw(self):
        # print(os.getcwd())
        # print(os.listdir())
        # os.chdir('artifacts')
        # print(os.getcwd())
        with open(path.MODEL_PATH,'rb')as file:
             self.model = pickle.load(file)
        with open(path.ASSET_PATH,'r') as file:
              self.output = json.load(file)
        # print(self.output)      
    
    def predict_output(self):
         self.load_raw()
         sl = self.data['sl']
         sw = self.data['sw']
         pl = self.data['pl']
         pw = self.data['pw']
         data_list = [float(sl),float(sw),float(pl),float(pw)]
         result = self.model.predict([data_list])
         return (f'{self.output.get(str(result[0]))}')
    

if __name__ == '__main__':
     obj = Prediction()
     obj.load_raw()
     
