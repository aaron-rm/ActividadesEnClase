
public class Problema3 {
    private int numinf=0,numsup=0;

    public Problema3(){
        this.numinf=0;
        this.numsup=0;
    }

    public boolean esPrimo(int n){
        if(n<2){
            return false;
        }
        if(n==2){
            return true;
        }
        if(n%2==0){
            return false;
        }
        for(int i=2;i<=Math.sqrt(n);i++){
            if(n%i==0){
                return false;
            }
        }
        return true;
    }

    public void mostrarNumPrimos(){
        int i=0,suma=0,cantidad=0;
        System.out.print("Números primos:");
        for(i=getNuminf();i<=getNumsup();i++){
            if(esPrimo(i)){
                System.out.print(" "+i);
                suma+=i;
                cantidad++;
            }
        }
        System.out.println();
        System.out.println("Cantidad de números primos: "+cantidad);
        System.out.println("Suma de números primos: "+suma);
    }

    public int getNuminf() {
        return numinf;
    }

    public int getNumsup() {
        return numsup;
    }

    public void setNuminf(int numinf) {
        this.numinf = numinf;
    }

    public void setNumsup(int numsup) {
        this.numsup = numsup;
    }
}
