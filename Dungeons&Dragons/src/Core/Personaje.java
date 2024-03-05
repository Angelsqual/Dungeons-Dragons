package Core;

public abstract class Personaje {
    protected String nombre;
    protected int salud;
    protected Ataque ataque;

    public Personaje(String nombre) {
        this.nombre = nombre;
    }

    /**
     * @return the nombre
     */
    public String getNombre() {
        return nombre;
    }

    /**
     * @return the salud
     */
    public int getSalud() {
        return salud;
    }

    public Ataque getAtaque() {
        return this.ataque;
    }

    /**
     * @param ataque the ataque to set
     */
    public void setAtaque(Ataque ataque) {
        this.ataque = ataque;
    }

    public int updateSalud(int value) {
        this.salud = this.salud + value;
        return this.salud;
    }

    public abstract int[] ataca(Personaje enemigo);

}
