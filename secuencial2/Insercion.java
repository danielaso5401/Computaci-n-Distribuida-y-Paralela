package secuencial2;

public class Insercion {
	int cadena[];
	public Insercion(int a[]) {//Recibir el arreglo
		this.cadena=a;
	}
	
	public void ordenar() {//Implementar el ordenameinto por inserion
		for (int i = 1; i < cadena.length; ++i) {
            int llave = cadena[i];
            int j = i - 1;
            while (j >= 0 && cadena[j] > llave) {
            	cadena[j + 1] = cadena[j];
                j = j - 1;
            }
            cadena[j + 1] = llave;
        }
		
	}

}
