#include <iostream>

int main() {
    
    float angulo;

    std::cout << "Ingrese el ángulo en grados sexagesimales: ";
    std::cin >> angulo;

    if (angulo == 90) {
        std::cout << "El ángulo es recto" << std::endl;
    } else {
        std::cout << "El ángulo no es recto" << std::endl;
    }

    return 0; 
}

