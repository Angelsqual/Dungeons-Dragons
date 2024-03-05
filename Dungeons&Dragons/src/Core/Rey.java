package Core;

public class Rey extends Personaje {

    public Rey(String nombre) {
        super(nombre);
        this.salud = 2000;

    }

    @Override
    public String toString() {
        return "[KING: " + this.nombre + ": " + this.salud + "]";

    }

    @Override
    public int[] ataca(Personaje enemigo) {
        int[] resultados = new int[3];
        resultados[0] = this.ataque.lanzaAtaque(enemigo);
        resultados[1] = this.ataque.lanzaAtaque(enemigo);
        resultados[2] = this.ataque.lanzaAtaque(enemigo);

        return resultados;
    }

}