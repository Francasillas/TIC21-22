package MiCodigo;

public class ManejaVehiculo {

public static void main(String[] args) {
// TODO Auto-generated method stub
vehiculo miBarquito;
Coche miCoche;
CocheElectrico miCochePilas;
miBarquito=new vehiculo("Titanic2","acuatico");
miCoche=new Coche("Delorian","terrestre");
miCochePilas=new CocheElectrico("Tesla","terrestre");
System.out.println("Mi coche es un "+miCochePilas.getnombre());
}

}


