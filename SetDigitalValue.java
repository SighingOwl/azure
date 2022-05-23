package modbus;
//import py4j.GatewayServer;
import de.re.easymodbus.modbusclient.*;

public class SetDigitalValue {
	static ModbusClient modbusClient = new ModbusClient("211.226.15.56", 502);
	
	public static void main(String[] args) {
		/*GatewayServer gatewayServer2 = new GatewayServer(new GetSensorValue());
		gatewayServer2.start();
		System.out.println("Gateway Server Started");*/
		
		try {
			modbusClient.WriteSingleCoil(189, true);
			System.out.println("complete");
		}
		catch (Exception e) {
			System.out.println("Error");
		}
	}
}
