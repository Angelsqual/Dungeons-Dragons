package Core;

import java.util.Random;

/**
 *
 * @author Angelsqual
 */
public class AtaqueArco implements Ataque {

    @Override
    public String toString() {
        return "arco";
    }

    @Override
    public int lanzaAtaque(Personaje enemigo) {
        int resultado;
        Random ran = new Random();
        int ataque = 50;
        int acierta = ran.nextInt(2);
        double factor = ran.nextDouble();
        resultado = (int) (ataque * acierta * factor);
        enemigo.updateSalud(-resultado);
        return resultado;

    }

}