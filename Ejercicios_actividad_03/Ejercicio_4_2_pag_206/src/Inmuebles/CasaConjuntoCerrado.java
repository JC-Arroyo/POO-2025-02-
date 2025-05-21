
package Inmuebles;

public class CasaConjuntoCerrado {
	
	protected static double valorArea = 2500000;
	protected int valorAdministración;
	protected boolean tienePiscina;
	protected boolean tieneCamposDeportivos;
	
	void imprimir() {
		super.imprimir();
		System.out.println("Valor de la administración = " +
		valorAdministración);
		System.out.println("Tiene piscina? = " + tienePiscina);
		System.out.println("Tiene campos deportivos? = " +
		tieneCamposDeportivos);
		System.out.println();
	}
}
