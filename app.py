#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request, render_template


# In[2]:


app = Flask(__name__)
#use 2 underscores on each side: means its a reserved word
#used to prevent people from uploading ur code to the cloud


# In[3]:


import joblib


# In[4]:


@app.route("/",methods = ["GET", "POST"]) #this is a decorator: any function declare below need this decorator as required by Flask to be runned
def index(): #define a function
    if request.method == "POST":
        rates = float(request.form.get("rates")) #to take back the data on jupyter, use FLOAT() because its number type
        print(rates)
        model1 = joblib.load("Regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("Tree")
        r2 = model2.predict([[rates]])     
        return(render_template("index.html", result1 = r1, result2 = r2)) #need to render the template before running it
    else:
        return(render_template("index.html", result1="waiting", result2="waiting")) #need to render the template before running it


# In[ ]:


if __name__ == "__main__":
    app.run()
    #need to do this in a cloud environment: means 
    
#error: use WGSI server, click the blue link to load the hdml page


# In[ ]:




