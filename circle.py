from flask import Flask,request

app = Flask(__name__)
@app.route('/area/<radius>',methods = ['POST'])

def area(radius):
    output = request.json
    area = 3.14*float(output["radius"])*float(output["radius"])
    return{"Area of Circle ": area}
if __name__ == "__main__":
    app.run()