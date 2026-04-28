/*
1SF115
Joseph Alvarez
Helen Bolanos
Jaziel Gonzalez
Dilam Jimenez
Aaron Remarchuk
*/


#include <iostream>
using namespace std;

int main() {
    int h;
    cout << "Introduce un numero : ";
    cin >> h;

    if (h <= 0) {
        cout << "El numero debe ser un entero positivo" << endl;
        return 1;
    }

    cout << "Secuencia de Collatz: " << h;

    while (h != 1) {
        if (h % 2 == 0) {  // Si el número es par
            h = h / 2;
        } else {  // Si el número es impar
            h = 3 * h + 1;
        }
        cout << " -> " << h;
    }

    cout << endl;
    return 0;
}
