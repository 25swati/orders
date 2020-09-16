import pickle
class Product:

    
	
    def __init__(self, name, rate, quantity, amount):
        self.name = name
        self.rate = rate
        self.quantity = quantity
        self.amount = amount
		

    def save(self, name, rate, quantity, amount):
        
        product=Product(name,rate,quantity,amount)
        picklefile = open('product', 'wb')
        pickle.dump(product, picklefile)
        picklefile.close()
    
    def load(self):
        loadproduct=open('product','rb')
        data=pickle.load(loadproduct)
        return data




        
      