public class Carro {

    private String marca;
    private String modelo;
    private int ano;
    private int velocidadeAtual;

    public Carro(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.velocidadeAtual = 0;
    }

    public void acelerar(int aumentoDeVelocidade) {
        if (aumentoDeVelocidade > 0) {
            this.velocidadeAtual += aumentoDeVelocidade;
            System.out.println(this.modelo + " acelerou. Velocidade atual: " + this.velocidadeAtual + " km/h");
        }
    }

    public void frear(int reducaoDeVelocidade) {
        if (reducaoDeVelocidade > 0) {
            this.velocidadeAtual -= reducaoDeVelocidade;
            if (this.velocidadeAtual < 0) {
                this.velocidadeAtual = 0;
            }
            System.out.println(this.modelo + " freou. Velocidade atual: " + this.velocidadeAtual + " km/h");
        }
    }
    
    public void buzinar() {
        System.out.println(this.modelo + " buzinou: Bibi!");
    }

    public String getMarca() {
        return this.marca;
    }

    public String getModelo() {
        return this.modelo;
    }

    public int getAno() {
        return this.ano;
    }

    public int getVelocidadeAtual() {
        return this.velocidadeAtual;
    }
}