import java.math.BigInteger;

public class Problema1 {
    private int num;

    public Problema1(){
        this.num=0;
    }


    public BigInteger calcularFactorial(){
        BigInteger factorial=BigInteger.ONE;

        if(getNum()==0){
            return factorial;
        }

        for(int i=2;i<=getNum();i++){
            factorial=factorial.multiply(BigInteger.valueOf(i));
        }
        return factorial;
    }

    public int getNum() {
        return num;
    }

    public void setNum(int num){
        this.num = num;
    }

}
