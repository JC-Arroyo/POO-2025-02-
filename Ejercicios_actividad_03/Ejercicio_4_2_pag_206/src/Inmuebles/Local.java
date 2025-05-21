
package Inmuebles;

public class Local extends Inmueble{
	
	enum tipo {INTERNO,CALLE};
	protected tipo tipoLocal; 
	
	public Local(int identificadorInmobiliario, int área, String dirección,
			tipo tipoLocal) {
			
		super(identificadorInmobiliario, área, dirección);
		this.tipoLocal = tipoLocal;
	}
	
	void imprimir() {
		super.imprimir(); 
		System.out.println("Tipo de local = " + tipoLocal);
	}
	
}
