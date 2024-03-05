package Core;

import java.util.Random;

/**
 *
 * @author Angelsqual
 */
public class AtaqueCuchillo implements Ataque {

    @Override
    public String toString() {
        return "cuchillo";
    }

    @Override
    public int lanzaAtaque(Personaje enemigo) {
        int resultado;
        Random random = new Random();
        int ataque = 25;
        int acierta = random.nextInt(2);
        double factor = random.nextDouble();
        resultado = (int) (acierta * factor * ataque);
        enemigo.updateSalud(-resultado);
        return resultado;
    }

}
