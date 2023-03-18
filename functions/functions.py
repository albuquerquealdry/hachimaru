import json

def setContextAccount():
    accesskey = input("AWS_ACCESS_KEY: ")
    secretkey = input("AWS_SECRET_KEY: ")
    nameContext = input("NAME CONTEXT: ")
    arquivo = open(f"contexts/context-{nameContext}", "a")
    arquivo.write(f"{accesskey} \n{secretkey} \n{nameContext}")