import json
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# return countries 
@app.route("/api/geoData/")
def Countries():
    f = open('./assets/json/countries.json','r',encoding="utf8")
    return f.read();

# return states 
@app.route("/api/geoData/<C_Code>")
def States(C_Code):
    f = open('./assets/json/states.json','r',encoding="utf8")
    # Transform json input to python objects
    input_dict = json.loads(f.read())
    print('input dict : ',input_dict)
    # Filter python objects with list comprehensions
    output_dict = [x for x in input_dict if(x['country_code'] == C_Code)]
    print('output dict : ',output_dict)
    print('C_Code : ',C_Code)
    # Transform python object back into json
    return json.dumps(output_dict) 

# return cities 
@app.route("/api/geoData/<C_Code>/<S_Code>")
def Cities(C_Code,S_Code):
    f = open('./assets/json/cities.json','r',encoding="utf8")
    # Transform json input to python objects
    input_dict = json.loads(f.read())
    print('input dict : ',input_dict)
    # Filter python objects with list comprehensions
    output_dict = [x for x in input_dict if(x['country_code'] == C_Code and x['state_code'] == S_Code)]
    print('output dict : ',output_dict)
    print('C_Code : ',C_Code)
    # Transform python object back into json
    return json.dumps(output_dict) 


if __name__=='__main__':
    app.run(debug=True)
