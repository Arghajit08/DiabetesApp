import joblib
import seaborn as sb
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd
import numpy as np
PATH="diabetes.csv"
df=pd.read_csv(PATH)
def get_graph():
    model=joblib.load("model.sav")
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(usf,c,d,e,color):
    model=joblib.load("model.sav")
    plt.switch_backend('AGG')
    figy=plt.figure()
    axis1=sb.scatterplot(x='Age',y=c,data=df,hue='Outcome',palette='rainbow')
    axis2=sb.scatterplot(x='Age',y=c,data=usf,color=color)
    plt.xticks(np.arange(10,100,5))
    plt.yticks(np.arange(0,d,e))
    plt.title('0 - Healthy & 1 - Unhealthy')
    plt.tight_layout()
    graph=get_graph()
    return graph
#import data from html file
#then plt.plot(data,Age)    
#I think we can't call plt like that as we call model.predict we have to look into error in screenshot csrf why plots are not working
#fault is in manage.py and result.html have to check tomorrow
#fault was debug was set false after completing editing set DEBUG=False in settings.py
#could not interpret value input by user for x in get_plot()i.e. a can be interpreted for parameter x in get_plot()
model=joblib.load("model.sav")
