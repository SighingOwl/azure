package modbus;
import py4j.GatewayServer;
import de.re.easymodbus.modbusclient.*;

public class GetSensorValue {
	static ModbusClient modbusClient = new ModbusClient("211.226.15.56", 502);
	
	public static void main(String[] args) {
		GatewayServer gatewayServer = new GatewayServer(new GetSensorValue());
		gatewayServer.start();
		System.out.println("Gateway Server Started");
	}

	public static void connectModbus() {
		try {
			modbusClient.Connect();
		}
		catch (Exception e) {
		}
	}
	
	public static void closeModbus() {
		try {
			modbusClient.Disconnect();
		}
		catch (Exception e) {
		}
	}
	
	public float getTemp() {
		int tmp[];
		float temp;
		
		try {
			tmp = modbusClient.ReadInputRegisters(0, 5);
			temp = ModbusClient.ConvertRegistersToFloat(tmp, ModbusClient.RegisterOrder.LowHigh);
			System.out.println(temp);
			
			return temp;
		}
		catch (Exception e) {
			return -1000000;
		}
	}
	
	public float getHumid() {
		int tmp[];
		float humid;
		
		try {
			//System.out.println(modbusClient.ConvertRegistersToFloat(modbusClient.ReadInputRegisters(0, 5)));
			tmp = modbusClient.ReadInputRegisters(2, 5);
			humid = ModbusClient.ConvertRegistersToFloat(tmp, ModbusClient.RegisterOrder.LowHigh);
			System.out.println(humid);
			
			return humid;
		}
		catch (Exception e) {
			return -1000000;
		}
	}
	
	public float getCO2() {
		int tmp[];
		float CO2;
		
		try {
			//System.out.println(modbusClient.ConvertRegistersToFloat(modbusClient.ReadInputRegisters(0, 5)));
			tmp = modbusClient.ReadInputRegisters(4, 5);
			CO2 = ModbusClient.ConvertRegistersToFloat(tmp, ModbusClient.RegisterOrder.LowHigh);
			System.out.println(CO2);
			
			return CO2;
		}
		catch (Exception e) {
			return -1000000;
		}
	}
}
