import time
import datetime

class MyKey:
    timestamp = ""
    keys = ["Lockwood 4","Lockwood 5"]
    filename = ""
    est_code = ""
    final_code = ""
    key_type = ""
    pin_1 = [-1,-1]
    pin_2 = [-1,-1]
    pin_3 = [-1,-1]
    pin_4 = [-1,-1]
    pin_5 = [-1,-1]
    pin_6 = [-1,-1]
    
    def __init__(self, file):
        self.filename = file
        self.timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        
    def printFilename(self):
        print(self.filename)
        
    def printTimestamp(self):
        print(self.timestamp)
    
    def printPins(self):
        print(self.pin_1)
        print(self.pin_2)
        print(self.pin_3)
        print(self.pin_4)
        print(self.pin_5)
        print(self.pin_6)
        
    def printKeyType(self):
        print(self.key_type)
        
    def setKeyType(self):
        flag = False
        while (flag == False):
            print("Choose key type:")
            for i in range(len(self.keys)):
                print("[{}] - {}".format(i,self.keys[i]))
            input_key = int(input("Number: "))
            if (input_key < 0) or (input_key >= len(self.keys)):
                print("input number must be between {} and {}".format("0",len(self.keys)))
                flag = False
            else:
#                 input_key
                self.key_type = self.keys[input_key]
                print("Key Type is {}".format(self.key_type))
                flag = True