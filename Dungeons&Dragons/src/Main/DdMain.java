package Main;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import Core.Ataque;
import Core.AtaqueArco;
import Core.AtaqueCuchillo;
import Core.AtaqueEspada;
import Core.Caballero;
import Core.Personaje;
import Core.Rey;
import Core.Troll;

/**
 *
 * @author Angelsqual
 */
public class DdMain {

    public static void main(String[] args) {
        List<Personaje> hombres = new ArrayList();
        List<Personaje> trolls = new ArrayList();
        Ataque espada = new AtaqueEspada();
        Ataque arco = new AtaqueArco();
        Ataque cuchillo = new AtaqueCuchillo();
        Rey arturo = new Rey("Arturo");
        arturo.setAtaque(espada);
        Caballero lancelot = new Caballero("Lancelot");
        lancelot.setAtaque(espada);
        Caballero percival = new Caballero("Percival");
        percival.setAtaque(arco);
        hombres.add(arturo);
        hombres.add(lancelot);
        hombres.add(percival);
        Random random = new Random();
        int numeroTrolls = random.nextInt(10) + 2;
        int n = 1;
        for (int i = 0; i < numeroTrolls; i++) {
            Troll troll = new Troll("Troll " + n);
            int numeroArmas = random.nextInt(3);
            if (numeroArmas == 0) {
                troll.setAtaque(espada);
            }
            if (numeroArmas == 1) {
                troll.setAtaque(arco);
            }
            if (numeroArmas == 2) {
                troll.setAtaque(cuchillo);
            }
            trolls.add(troll);
            n = n + 1;

        }
        boolean fin = true;
        while (fin) {
            for (int i = 0; i < hombres.size(); i++) {
                int x = random.nextInt(trolls.size());
                Personaje enemigo = trolls.get(x);
                int[] resultados = hombres.get(i).ataca(enemigo);
                System.out.println(hombres.get(i) + " lucha contra " + enemigo);
                for (int j = 0; j < resultados.length; j++) {
                    if (resultados[j] == 0) {
                        System.out.println("Ataque con " + hombres.get(i).getAtaque() + " (falla)");
                    } else {
                        System.out.println("Ataque con " + hombres.get(i) + " (-" + resultados[j] + ")");
                    }

                }
                if (enemigo.getSalud() <= 0) {
                    System.out.println(enemigo + " muere!!");
                    trolls.remove(enemigo);
                }
                if (trolls.isEmpty()) {
                    System.out.println("El ganador son los HEROES!!");
                    System.out.println("Los supervivientes fueron: ");
                    System.out.println(hombres);
                    fin = false;
                }
            }
            for (int i = 0; i < trolls.size(); i++) {
                int x = random.nextInt(hombres.size());
                Personaje enemigo = hombres.get(x);
                int[] resultados = trolls.get(i).ataca(enemigo);
                System.out.println(trolls.get(i).getNombre() + " lucha contra " + enemigo.getNombre());
                for (int j = 0; j < resultados.length; j++) {
                    if (resultados[j] == 0) {
                        System.out.println("Ataque con" + trolls.get(i).getAtaque() + " (falla)");
                    } else {
                        System.out.println("Ataque con " + trolls.get(i).getAtaque() + " (-" + resultados[j] + ")");
                    }
                }
                if (enemigo.getSalud() <= 0) {
                    System.out.println(enemigo + " muere!!");
                    hombres.remove(enemigo);
                }
                if (hombres.isEmpty()) {
                    System.out.println("Los MALOS GANAN!!");
                    System.out.println("Los trolls supervivientes son: ");
                    System.out.println(trolls);
                    fin = false;
                }

            }

        }
    }
}