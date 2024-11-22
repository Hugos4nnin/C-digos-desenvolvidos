int main() {
    int a, b, resultado = 1;

    printf("Digite a base (a): ");
    scanf("%d", &a);
    printf("Digite o expoente (b): ");
    scanf("%d", &b);

    // Garantindo que 'a' e 'b' são inteiros e positivos
    if (a < 0 || b < 0) {
        printf("Por favor, insira números inteiros e positivos.\n");
        return 1;
    }

    // Estrutura de repetição com teste no início para calcular a potenciação
    int contador = 0;
    while (contador < b) {
        resultado *= a;  // Multiplica o resultado pela base
        contador++;      // Incrementa o contador
    }

    printf("O resultado de %d^%d é: %d\n", a, b, resultado);

    return 0;
}
