
public class CuentaBancaria {
	
	String nombresTitular;
	String apellidosTitular;
	int númeroCuenta;
	tipoCuenta tipoCuenta;
	float saldo = 0;

	CuentaBancaria(String nombresTitular, String apellidosTitular, int
		numeroCuenta, tipoCuenta tipoCuenta) {			
		this.nombresTitular = nombresTitular;
		this.apellidosTitular = apellidosTitular;
		this.númeroCuenta = numeroCuenta;
		this.tipoCuenta = tipoCuenta;
	}
	
	void imprimir() {
		System.out.println("Nombres del titular = " + nombresTitular);
		System.out.println("Apellidos del titular = " + apellidosTitular);
		System.out.println("Número de cuenta = " + númeroCuenta);
		System.out.println("Tipo de cuenta = " + tipoCuenta);
		System.out.println("Saldo = " + saldo);
	}
		
	void consultarSaldo() {
		System.out.println("El saldo actual es = " + saldo);
	}
	
	boolean consignar(int valor) {
		
		if (valor > 0) {
			saldo = saldo + valor; 
			System.out.println("Se ha consignado $" + valor + " en la "
				+ "cuenta. El nuevo saldo es $" + saldo);
		return true;
		} else {
		System.out.println("El valor a consignar debe ser mayor que	"
				+ "cero.");
		return false;
		}
	}
	
	boolean retirar(int valor) {
	
		if ((valor > 0) && (valor <= saldo)) {saldo = saldo - valor; 
			System.out.println("Se ha retirado $" + valor + " en la cuenta. "
					+ "El nuevo saldo es $" + saldo);
		return true;
		} else {
			System.out.println("El valor a retirar debe ser menor que el "
					+ "saldo actual.");
		return false;
		}
	}
}
