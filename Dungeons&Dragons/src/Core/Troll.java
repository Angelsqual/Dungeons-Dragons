package Core;

public class Troll extends Personaje {

    public Troll(String nombre) {
        super(nombre);
        this.salud = 1000;
    }

    @Override
    public String toString() {
        return "[ TROLL: " + this.nombre + ": " + this.salud + " ]";
    }

    @Override
    public int[] ataca(Personaje enemigo) {
        int[] resultados = new int[1];
        resultados[0] = this.ataque.lanzaAtaque(enemigo);

        return resultados;
    }
}
