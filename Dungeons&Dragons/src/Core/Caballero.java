package Core;

public class Caballero extends Personaje {

    public Caballero(String nombre) {
        super(nombre);
        this.salud = 1500;
    }

    @Override
    public String toString() {
        return "[KNIGHT: " + this.nombre + ": " + this.salud + " ]";
    }

    @Override
    public int[] ataca(Personaje enemigo) {
        int[] resultados = new int[2];
        resultados[0] = this.ataque.lanzaAtaque(enemigo);
        resultados[1] = this.ataque.lanzaAtaque(enemigo);

        return resultados;
    }
}