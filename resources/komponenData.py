from flask import Flask, jsonify, Blueprint, request
from flask_restful import Resource, Api, reqparse, inputs, abort

komponenData = {
    "komponenData" : [
        {"nama barang" : "resistor", "no barang" : "A0001" ,"jenis": ["Resistor(nilai tetap)", "variabel resistor ", "light depending resistor(ldr)", "thermistor(ntc/ptc)"]},
        {"nama barang" : "kapasitor", "no barang" : "A0002", "jenis": ["kapasitor(non-polaritas)", "kapasitor elektrolit (polaritas)", "kapasitor variabel"]},
        {"nama barang" : "induktor", "no barang" : "A0003", "jenis" :["induktor(nilai tetap)", "induktor variabel(variabel coil)"]}
    ]
}

class readAllkomponenData(Resource):
    def get(self):
        return komponenData

class readOneUserkomponenData(Resource):
    def get(self):
        args = request.args.get('nama barang')
        args1 = request.args.get('no barang')
        for user in komponenData["komponenData"]:
            if user["nama barang"] == args:
                return user, 200 #200 = ok 
            elif user["no barang"] == args1:
                return user["jenis"], 200


        return abort (400, message = 'Data Not Exist') #400 = request yang dibuat salah atau data yang dikirim tidak ada.

# without query param
# class addUserkomponenData(Resource):
    # def post(self):  
    #     komponenData['komponenData'].append(request.json)
    #     return 'Created', 201

def nameHaveExist(nama_barang):
    for x in komponenData["komponenData"]:
        if x["nama barang"] == nama_barang:
            abort(400, message = "Data exist")
    return nama_barang

class addUserkomponenData(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "nama barang",
            help = "komponen tidak ditemukan",
            required = True,
            location = ["json"],
            type = str
        )
        super().__init__()

#with query param
    def post(self):  
        args = self.reqparse.parse_args()
        nameHaveExist(request.json["nama barang"])
        komponenData['komponenData'].append(request.json)
        return {"message" : "Created"}, 201

class editkomponenData(Resource):
    def put(self):
        req = request.json
        args = request.args.get('nama barang')
        for data in komponenData["komponenData"]:
            if data["nama barang"] == args:
                data["no barang"] = req["no barang"]
                data["jenis"] = req["jenis"]
                return data, 201

#without query param
# class deleteDataKomponen(Resource):
#     def delete(self, nama_barang):
#         for index in range(len(komponenData["komponenData"])):
#             if komponenData["komponenData"][index]["nama barang"] == nama_barang:
#                 komponenData["komponenData"].pop(index)
#         return {"message" : "Data has been Delete!"}, 200

#with query param
class deleteDataKomponen(Resource):
    def delete(self):
        args = request.args.get('nama barang')
        for index in range(len(komponenData["komponenData"])):
            if komponenData["komponenData"][index]["nama barang"] == args:
                komponenData["komponenData"].pop(index)
                return {"message" : "Data has been Delete"}, 201
        
        return {"message" : "Data Not Found"}, 404

            









komponenData_api = Blueprint('resources/komponenData', __name__)
api = Api(komponenData_api)

api.add_resource(readAllkomponenData, 'readAllkomponenData')
api.add_resource(readOneUserkomponenData, 'readOneUserkomponenData')
api.add_resource(addUserkomponenData, 'addUserkomponenData')
api.add_resource(editkomponenData, 'editkomponenData')
# api.add_resource(deleteDataKomponen, 'deleteDataKomponen/<nama_barang>')
api.add_resource(deleteDataKomponen, 'deleteDataKomponen')