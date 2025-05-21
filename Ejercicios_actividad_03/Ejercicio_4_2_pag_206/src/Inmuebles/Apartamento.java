
package Inmuebles;

public class Apartamento extends InmuebleVivienda{

	public Apartamento(int identificadorInmobiliario, int área, String
		dirección, int númeroHabitaciones, int númeroBaños) {
		super(identificadorInmobiliario, área, dirección,
			númeroHabitaciones, númeroBaños);
	}
	
	void imprimir() {
		super.imprimir(); 
	}
}
