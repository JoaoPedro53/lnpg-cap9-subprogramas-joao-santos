public class Tarefa3JavaParam {
    public static void main(String[] args) {
        int x = 10;
        System.out.println(x);
        alterarNumero(x);
        System.out.println(x);
    }

    public static void alterarNumero(int x){
        System.out.println(x);
        x += 1;
        System.out.println(x);
    }
}