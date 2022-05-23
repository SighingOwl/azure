package modbus;
//import py4j.GatewayServer;
import de.re.easymodbus.modbusclient.*;

public class GetDigitalValue {
	static ModbusClient modbusClient = new ModbusClient("211.226.15.56", 502);
	
	public static void main(String[] args) {
		/*GatewayServer gatewayServer2 = new GatewayServer(new GetSensorValue());
		gatewayServer2.start();+                                                         
		System.out.println("Gateway Server Started");*/
		
		boolean tmp[];
		
		try {
			tmp = modbusClient.ReadDiscreteInputs(0, 7);
			for(int i = 0; i < 7; i++) {
				System.out.println(tmp[i]);
			}
		}
		catch (Exception e) {
			System.out.println("Error");
		}
	}
}

