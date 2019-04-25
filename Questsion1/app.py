from flask import Flask
import bpy

app = Flask(__name__)
@app.route('/getObjloc', methods=['POST','GET'])
def location():
	return "CUBE OBJECT LOCATION [X]: "+str(bpy.data.objects["Cube"].location[0])+" [Y]: "+str(bpy.data.objects["Cube"].location[1])+" [Z]:"+str(bpy.data.objects["Cube"].location[2])
## debug = True
## THIS IS TO START SERVICE ON SERVER WITH 'http://host:port/'
if __name__ == '__main__':
   app.run(host='localhost', port='5009')
