package MiCodigo;

public class Fecha {
private int dia;
private int mes;
private int anio;
/**
* @param dia
* @param mes
* @param anio
*/
public Fecha(int dia, int mes, int anio) {
super();
this.dia = dia;
this.mes = mes;
this.anio = anio;
}
public int getDia() {
return dia;
}
public void setDia(int dia) {
this.dia = dia;
}
public void setDia(String nombredia) {
if(this.dia==1)nombredia="Primero";
if(this.dia==2)nombredia="Segundo";
if(this.dia==3)nombredia="Tercero";


}
public int getMes() {
return mes;
}
public String getMes(int modo) {
String nombreMes="";
if(modo==0) {
if(this.mes==1)nombreMes="Enero";
if(this.mes==2)nombreMes="Febrero";
if(this.mes==3)nombreMes="Marzo";
}

if(modo==1) {
if(this.mes==1)nombreMes="ENERO";
if(this.mes==2)nombreMes="FEBRERO";
if(this.mes==3)nombreMes="MARZO";
}
if(modo==2) {
if(this.mes==1)nombreMes="Es el mes 1";
if(this.mes==1)nombreMes="Es el mes 1";
if(this.mes==1)nombreMes="Es el mes 1";

}
return nombreMes;
}
public void setMes(int mes) {//poner mas d esto
this.mes = mes;
}
public void setMes(String nombreMes) {//Polimorfismo 2 instrucciones mismo nombre hace cosas distintas
if(nombreMes=="Enero")this.mes=1;
if(nombreMes=="Febrero")this.mes=2;
if(nombreMes=="Marzo")this.mes=3;
}
public int getAnio() {
return anio;
}
public void setAnio(int anio) {
this.anio = anio;
}
boolean esPosterior(Fecha nuevaFecha){//boolean devuelve verdadero o falso
boolean loEs;
loEs=false;
if(this.getAnio()>nuevaFecha.getAnio()) {
loEs=true;
}
else {
if(this.getAnio()==nuevaFecha.getAnio()) {
if(this.getMes()>nuevaFecha.getMes()) {
loEs=true;
}
else {
if(this.getAnio()==nuevaFecha.getAnio()) {
if(this.getMes()>nuevaFecha.getMes()) {
if(this.getDia()>nuevaFecha.getDia()) {
loEs=true;
return loEs;
}

}

}

}
}
}
return loEs;
}
}