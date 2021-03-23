package secuencial2;
import secuencial.Insercion;
import java.io.*;
import com.panayotis.gnuplot.JavaPlot;

public class Prueba {

	public static void main(String[] args) {

		int TOPE = 10;
		int arr[];
		FileWriter fichero = null;
        PrintWriter pw = null;
        try
        {
            fichero = new FileWriter("prueba2.txt");
            pw = new PrintWriter(fichero);
    		for(int n=1;n<=TOPE;n++) {
    			arr = generar(n);
    			//imprimir(arr);
    			Insercion p1 = new Insercion(arr);			
    			p1.ordenar();
    			//imprimir(arr);
    			//System.out.println(p1.time());
    			pw.println(p1.time());
    			//System.out.println("-------------------");
    		}

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
           try {
           if (null != fichero)
              fichero.close();
           } catch (Exception e2) {
              e2.printStackTrace();
           }
        }
        JavaPlot p = new JavaPlot();

        p.addPlot("plot F:\\CDP\\prueba2.txt with lines");

        p.plot();

	}

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
