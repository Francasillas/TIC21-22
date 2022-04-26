package MiCodigo;

public class Coche extends vehiculo {
	private String marca;
	public Coche(String identificador, String medio ) {
		super(identificador, medio);
	}
	public String getMarca() {
		return marca;
	}
	public void setMarca(String marca) {
		this.marca = marca;
	}
	
}
