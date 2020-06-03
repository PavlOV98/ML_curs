import math
class Iris:
    sepal_length =0
    sepal_width = 0
    petal_length = 0
    petal_width = 0
    type=""
    new_type=""
    id=0
    def __init__(self,str,id):
        str = str.split(',')
        #print(str)
        self.id=id
        self.type = str[4][0:-1]
        self.sepal_length=float(str[0])
        self.sepal_width = float(str[1])
        self.petal_length = float(str[2])
        self.petal_width = float(str[3])
    def get_dist(self,b):
        return (math.sqrt(((self.sepal_length - b.sepal_length) ** 2) + ((self.sepal_width - b.sepal_width)** 2) + ((self.petal_length - b.petal_length)** 2)+ ((self.petal_width - b.petal_width)** 2)))

    def normilise(self, min_arg=[], max_arg=[]):
        self.petal_length = (self.petal_length - min_arg[0]) / (max_arg[0] - min_arg[0])
        self.petal_width = (self.petal_width - min_arg[1]) / (max_arg[1] - min_arg[1])
        self.sepal_length = (self.sepal_length - min_arg[2]) / (max_arg[2] - min_arg[2])
        self.sepal_width = (self.sepal_width - min_arg[3]) / (max_arg[3] - min_arg[3])

class Check:
    type=""
    len=0.0
    def __init__(self,study=Iris,find=Iris):
        self.type=study.type
        self.len=study.get_dist(find)

    def __str__(self):
        return (self.len.__str__() + ' ' + self.type.__str__())

def keyFunc(item=Check):
   return item.len