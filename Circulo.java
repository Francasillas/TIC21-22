package MiCodigo;

public class Circulo {
	int coordx;
	int coordy;
	double radio; //double=float pero mejor
/**
* @param coordx
* @param coordy
* @param radio
*/
	public Circulo(int coordx, int coordy, double radio) {
		super();
		this.coordx = coordx;
		this.coordy = coordy;
		this.radio = radio;
	}
	public int getCoordx() {
		return coordx;
	}
	public void setCoordx(int coordx) {
		this.coordx = coordx;
	}
	public int getCoordy() {
		return coordy;
	}
	public void setCoordy(int coordy) {
		this.coordy = coordy;
	}
	public double getRadio() {
		return radio;
	}
	public void setRadio(double radio) {
		this.radio = radio;
	}

//Metodo Circulo
	public double devuelveArea() {
        double Area;
        Area=Math.PI*Math.pow(radio,2);
        return(Area);
		}
	
//public double
	public double devuelveLongitud() {
        double longitud;
        longitud=Math.PI*radio;
        return longitud;
	}              
}