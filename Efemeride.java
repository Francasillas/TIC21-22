package MiCodigo;
//Clase hija de fecha

public class Efemeride extends Fecha {
private String quePaso;


public Efemeride(int dia, int mes, int anio,String quePaso) {
super(dia, mes, anio);//lleva a la clase madre los atributos exclusivos de ella
// TODO Auto-generated constructor stub
this.setQuePaso(quePaso);
}


public String getQuePaso() {
return quePaso;
}


public void setQuePaso(String quePaso) {
this.quePaso = quePaso;
}


}