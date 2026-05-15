public class Tarefa1Java {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String[] students = new String[5];
        double[][] grades = new double[5][3];
        double[] average = new double[5];
        String[] situations = new String[5];

        for (int i = 0; i < 5; i++) {

            System.out.println("\n=== Aluno " + (i + 1) + " ===");

            System.out.print("Nome: ");
            students[i] = sc.nextLine();

            double sum = 0;

            for (int j = 0; j < 3; j++) {
                System.out.print("Nota " + (j + 1) + ": ");
                grades[i][j] = sc.nextDouble();

                sum += grades[i][j];
            }

            sc.nextLine();

            average[i] = sum / 3;

            if (average[i] >= 7) {
                situations[i] = "Aprovado";
            } else if (average[i] >= 5) {
                situations[i] = "Recuperação";
            } else {
                situations[i] = "Reprovado";
            }
        }

        System.out.println("\n===== RELATÓRIO FINAL =====");

        for (int i = 0; i < 5; i++) {

            System.out.println("\nAluno: " + students[i]);

            System.out.println("Notas:");
            for (int j = 0; j < 3; j++) {
                System.out.println("Nota " + (j + 1) + ": " + grades[i][j]);
            }

            System.out.printf("Média: %.2f\n", average[i]);
            System.out.println("Situação: " + situations[i]);
        }

        sc.close();
    }
}

public class Tarefa1JavaRefatorado {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String[] students = new String[5];
        double[][] grades = new double[5][3];
        double[] average = new double[5];
        String[] situations = new String[5];

        for (int i = 0; i < 5; i++) {

            addStudentInList(students, i, sc);
            addeGrades(grades, i, sc);
            calcAverage(grades, average, i);

            situations[i] = average[i] >= 7 ? "Aprovado" : average[i] >= 5 ? "Recuperação" : "Reprovado";
        }

        System.out.println("\n===== RELATÓRIO FINAL =====");

        for (int i = 0; i < 5; i++) {

            printStudent(students, i);
            printGrades(grades, i);

            System.out.printf("Média: %.2f\n", average[i]);
            System.out.println("Situação: " + situations[i]);
        }

        sc.close();
    }

    public static void printStudent(String[] students, int indiceStudent) {
        System.out.println("\nAluno: " + students[indiceStudent]);
    }

    public static void printGrades(double[][] grades, int indiceStudent) {
        System.out.println("Notas:");
        for (int j = 0; j < 3; j++) {
            System.out.println("Nota " + (j + 1) + ": " + grades[indiceStudent][j]);
        }
    }

    public static void addStudentInList(String[] students, int indice, Scanner sc) {
        System.out.println("\n=== Aluno " + (indice + 1) + " ===");
        System.out.print("Nome: ");
        students[indice] = sc.nextLine();
    }

    public static void addeGrades(double[][] grades, int indice, Scanner sc) {
        for (int j = 0; j < 3; j++) {
            System.out.print("Nota " + (j + 1) + ": ");
            grades[indice][j] = sc.nextDouble();

            sc.nextLine();
        }
    }

    public static void calcAverage(double[][] grades, double[] average, int indice) {
        double sum = 0;
        for (int j = 0; j < 3; j++) {
            sum += grades[indice][j];
        }
        average[indice] = sum / 3;
    }

}



