/* Joãozinho comprou uma pizza e gostaria de distribuir seus pedaços entre seus amigos, sendo que a pizza tem 8 pedaços.

Joãozinho pediu sua ajuda para saber quantas pizzas seriam necessárias para dividir entre seus amigos, para que cada um coma no mínimo 1 pedaço de pizza.
Entrada

O usuário entrará com o número XX de amigos.
Saída


A saída constará do número total de pizzas que Joãozinho pedirá.
*/
#include <stdio.h>

int main() {
  int amigos, i; // Number of friends
  int pizzaSlices = 8; // Slices per pizza

  printf("Digite o número de amigos: ");
  scanf("%d", &amigos);

  int pizzasNeeded = 0; // Initialize pizza counter

  // Calculate pizzas needed
  while (amigos > 0) {
    if (pizzaSlices % amigos <= 1 ) {
      pizzasNeeded++; // Increment pizza count (full pizza)
      printf("%d", pizzasNeeded);
    } else {
     for(int i = 0; i < amigos; i++){
       pizzasNeeded+=(i/pizzaSlices);;
     }
    }
  }

  // Print total pizzas required
  printf("Joãozinho precisa de %d pizzas.\n", pizzasNeeded);

  return 0;
}