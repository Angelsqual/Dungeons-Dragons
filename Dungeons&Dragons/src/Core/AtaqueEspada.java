package Core;

import java.util.Random;

/**
 *
 * @author Angelsqual
 */
public class AtaqueEspada implements Ataque {

    @Override
    public String toString() {
        return "espada";
    }

    @Override
    public int lanzaAtaque(Personaje enemigo) {
        int resultado;
        Random random = new Random();
        int ataque = 100;
        int acierta = random.nextInt(2);
        double factor = random.nextDouble();
        resultado = (int) (ataque * acierta * factor);
        enemigo.updateSalud(-resultado);
        return resultado;
    }

}
