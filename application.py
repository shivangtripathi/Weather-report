from flask import Flask,request,render_template
import requests
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    if request.method=='POST':
        city=request.form['city']
    else:
        city= 'Gorakhpur'    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2a57d46e61594955f37bd5c0cdfed460&units=metric'.format(city)    

    rqst = requests.get(url)
    data= rqst.json()

    info={
    "temp":str(data['main']['temp']),
    "wind_speed":str(data['wind']['speed']),
    "coordinates":'Longitute' + ' ' + str(data['coord']['lon'])+' '+'Latitude'+' '+str(data['coord']['lat']),
    "des":str(data['weather'][0]['description']),
    }
    return render_template('index.html',data=info)

if __name__ == '__main__': 
    app.run(debug = True)   
    cache.clear()  

