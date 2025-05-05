
public class ejercicioPag95 {

	public static void main(String[] args) {
		CuentaBancaria cuenta = new CuentaBancaria("Pedro","Pérez",
		123456789,tipoCuenta.AHORROS);
		cuenta.imprimir();
		cuenta.consignar(200000);
		cuenta.consignar(300000);
		cuenta.retirar(400000);
	}
}
