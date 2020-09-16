from flask import *  
app = Flask(__name__)  
  
from Product_Detail import Product
@app.route('/addProduct',methods = ['POST'])  
def addProduct():  
      name=request.form['product']  
      print(name)
      rate=request.form['rate']  
      quantity=request.form['quantity']
      amount=request.form['amount']
      product=Product(name,rate,quantity,amount)
      product.save(name,rate,quantity,amount)
      productdetail=product.load()
      return productdetail.__dict__ 
   
if __name__ == '__main__':  
   app.run(debug = True)  