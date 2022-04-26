package MiCodigo;

public class ManejaFecha {

public static void main(String[] args) {
// TODO Auto-generated method stub
Fecha fecha1;
Fecha fecha2;
Efemeride efemeride1;
efemeride1=new Efemeride(23,2,2004,"texto");
fecha1=new Fecha(6,8,2004);
fecha2=new Fecha(30,6,2004);

if(fecha1.esPosterior(fecha2)==true) {
System.out.println("La fecha 1 es posterior a la fecha 2");
}
else {
System.out.println("La fecha 1 es anterior o igual a la fecha 2");

}
fecha1.setMes(2);
System.out.println("El nuevo mes es "+fecha1.getMes(0));//0=modo
fecha1.setMes("Enero");
System.out.println("El nuevo mes es "+fecha1.getMes(1));

if(fecha1.esPosterior(efemeride1)==true) {
System.out.println("La fecha 1 es posterior a la efemeride");
}
else {
System.out.println("La fecha 1 es anterior o igual a la efemeride");
}


System.out.println("En la efemeride se celebra: ");
System.out.println(efemeride1.getQuePaso());
	}	
}