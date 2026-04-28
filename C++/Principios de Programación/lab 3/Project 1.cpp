#include <iostream>
using namespace std;


void absoluto(float num) { 
    if (num >= 0) {
        cout << "El valor absoluto es: " << num << endl; 
    } else {
        cout << "El valor absoluto es: " << -num << endl; 
    }
}

int main() { 
    float num; 
    string continuar; 
    do {
        cout << "Ingrese un número: ";
        cin >> num; 
        absoluto(num); 
        cout << "¿Quiere ingresar otro numero? (si o no): ";
        cin >> continuar;
    } while (continuar == "si");

    return 0; 
}


