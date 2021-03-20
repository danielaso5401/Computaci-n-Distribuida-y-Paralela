package secuencial2;

public class Prueba {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int TOPE = 10;
		int arr[];
		for(int n=1;n<=TOPE;n++) {
			//generar un arreglo de tamano "n"
			arr = generar(n);
			imprimir(arr);
			Insercion p1 = new Insercion(arr);			
			p1.ordenar();
			imprimir(arr);
			System.out.println("-------------------");
		}		
	}
	//Generar arreglos de peores casos
	//Ejemplo: Si n=5 0> arr={5,4,3,2,1}
	private static int[] generar(int n) {
		
		int aux=0;
		int arreglo[]=new int[n];
		for (int i = n; i > 0; --i){
			arreglo[aux]=i;
			aux=aux+1;
		}
			
		return arreglo;
	}

	private static void imprimir(int[] arr1) {
		int n = arr1.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr1[i] + " ");
        System.out.println();
	}

}
