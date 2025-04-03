import matplotlib.pyplot as plt
import numpy as np
import math

class Function:
    x: np.array
    y: np.array
    k: float
    d: float
    

    def __init__(self, coordinates, learning_rate = 0.02, epochs = 2000):
        self.x = coordinates[:,0]
        self.y = coordinates[:,1]
        k = 0.0
        d = 0.0
        for i in range(epochs):
            k, d = self.__gradient(learning_rate, k, d)
        self.k = k
        self.d = d    

    
    def get(self, x):
        return self.k * x + self.d
    
    def __error(self, k, d):
        error = 0.0
        for i in range(len(self.x)):
            error += (self.y - ( k * self.x + d))**2

        return error/len(self.x)    

    def __gradient(self, learning_rate, k, d):
        
        n = len(self.x)
        kerror = 0.0
        derror = 0.0
        for i in range(n):
            kerror += -(2/n) * self.x[i] * (self.y[i] - (k*self.x[i]+d))
            derror += -(2/n) * (self.y[i] - (k*self.x[i]+d))


        k = k - kerror * learning_rate
        d = d - derror * learning_rate

        return k, d

        

            
        
        
        

    def plot(self):
        
        plt.figure(figsize=(7,4))
        start = math.floor(np.min(self.x))
        end = math.ceil(np.max(np.sort(self.x)))

        plt.scatter(self.x,self.y)
        plt.plot(list(range(start,end)), [self.get(x) for x in range(start,end)])
        plt.show()

if __name__ == "__main__":
    coords = np.array([[1,2],[3,7],[5,8],[1,4],[4.5,3.7]])
    function = Function(coordinates=coords)

    function.plot()