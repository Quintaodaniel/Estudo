public class Garagem {

    public static void main(String[] args) {
        Carro meuFusca = new Carro("Volkswagen", "Fusca", 1975);
        Carro minhaFerrari = new Carro("Ferrari", "F8", 2024);

        System.out.println("--- Ações com o Fusca ---");
        System.out.println("Meu carro é um " + meuFusca.getMarca() + " " + meuFusca.getModelo() + ", ano " + meuFusca.getAno() + ".");
        
        meuFusca.acelerar(60);
        meuFusca.frear(20);
        meuFusca.buzinar();
        System.out.println("Velocidade final: " + meuFusca.getVelocidadeAtual() + " km/h");


        System.out.println("\n--- Ações com a Ferrari ---");
        System.out.println("Meu outro carro é um " + minhaFerrari.getMarca() + " " + minhaFerrari.getModelo() + ", ano " + minhaFerrari.getAno() + ".");

        minhaFerrari.acelerar(200);
        minhaFerrari.frear(50);
        minhaFerrari.buzinar();
        System.out.println("Velocidade final: " + minhaFerrari.getVelocidadeAtual() + " km/h");
    }
}