#include <iostream>
#include <cmath> // Para usar la función trunc

using namespace std;

int main() {
    double dolares;
    int b100, b50, b20, b10, b5, b1;
    double m1, m050, m025, m010, m005, m001;

    cout << "Escribe una cantidad de dinero: ";
    cin >> dolares;

    // Billetes
    b100 = trunc(dolares / 100);
    dolares = fmod(dolares, 100);
    b50 = trunc(dolares / 50);
    dolares = fmod(dolares, 50);
    b20 = trunc(dolares / 20);
    dolares = fmod(dolares, 20);
    b10 = trunc(dolares / 10);
    dolares = fmod(dolares, 10);
    b5 = trunc(dolares / 5);
    dolares = fmod(dolares, 5);
    b1 = trunc(dolares / 1);
    dolares = fmod(dolares, 1);

    // Monedas
    dolares *= 100; // Convertimos a centésimos
    m050 = trunc(dolares / 50);
    dolares = fmod(dolares, 50);
    m025 = trunc(dolares / 25);
    dolares = fmod(dolares, 25);
    m010 = trunc(dolares / 10);
    dolares = fmod(dolares, 10);
    m005 = trunc(dolares / 5);
    dolares = fmod(dolares, 5);
    m001 = trunc(dolares / 1);
    dolares = fmod(dolares, 1);

    // Mostrar resultados
    cout << "Billetes de 100: " << b100 << endl;
    cout << "Billetes de 50: " << b50 << endl;
    cout << "Billetes de 20: " << b20 << endl;
    cout << "Billetes de 10: " << b10 << endl;
    cout << "Billetes de 5: " << b5 << endl;
    cout << "Billetes de 1: " << b1 << endl;
    cout << "Monedas de 0.50: " << m050 << endl;
    cout << "Monedas de 0.25: " << m025 << endl;
    cout << "Monedas de 0.10: " << m010 << endl;
    cout << "Monedas de 0.05: " << m005 << endl;
    cout << "Monedas de 0.01: " << m001 << endl;

    return 0;
}
