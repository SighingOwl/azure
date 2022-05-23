from py4j.java_gateway import JavaGateway

class query:
    def gettemp(gateway):
        temp = round(gateway.getTemp(), 1)
        print(temp)
        return temp
    
    def gethumid(gateway):
        humid = round(gateway.getHumid(), 1)
        print(humid)
        return humid
    
    def getco2(gateway):
        CO2 = round(gateway.getCO2(), 1)
        print(CO2)
        return CO2

'''
gateway = JavaGateway()
gateway.connectModbus()
gateway.closeModbus()
'''

