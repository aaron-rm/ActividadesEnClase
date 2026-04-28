#include <iostream>

int main() {
  
    float temperatura;

    std::cout << "Ingrese la temperatura en grados centígrados: ";
    std::cin >> temperatura;

    if (temperatura > 100) {
        std::cout << "Por encima del punto de ebullición" << std::endl;
    }

    return 0; 
}

