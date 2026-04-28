public class Problema4 {
    private double numMayor=0;

    public Problema4(){
        this.numMayor=0;
    }

    public void setNumMayor(double numMayor) {
        if(numMayor>getNumMayor()){
            this.numMayor=numMayor;
        }
    }

    public double getNumMayor() {
        return numMayor;
    }

}
