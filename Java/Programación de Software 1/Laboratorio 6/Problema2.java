
public class Problema2 {
    private int num=0;

    public Problema2(){
        this.num=0;
    }

    public int calcularSuma(){
        int suma=0,temp=getNum();
        while(temp>0){
            suma+= temp % 10;
            temp /=10;
        }
        return suma;
    }


    public void setNum(int num) {
        this.num = num;
    }

    public int getNum() {
        return num;
    }
}
