public class Tarefa4Java {
    public static void aplicarDesconto(Produto p) {

        System.out.println("Antes: " + p.preco);

        p.preco = p.preco * 0.9;

        System.out.println("Depois: " + p.preco);
    }

    public static void main(String[] args) {

        Produto prod = new Produto();
        prod.nome = "Mouse";
        prod.preco = 100;

        aplicarDesconto(prod);

        System.out.println("No main: " + prod.preco);
    }
}
