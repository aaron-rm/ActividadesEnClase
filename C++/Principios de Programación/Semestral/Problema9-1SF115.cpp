//Helen Bolaños, Aaron Remarchuck, Joseph Alvarez, Dilam, Jaziel Gonzales, 1SF115
#include <iostream>
#include <string>
using namespace std;

const int num_centros = 10;
const int years = 5;
const int meses = 12;

int main() {
    string centros[num_centros] = {
        "cataratas del iguazú",
        "perito moreno",
        "bariloche",
        "ushuaia",
        "salta",
        "mendoza",
        "córdoba",
        "mar del plata",
        "rosario",
        "buenos aires"
    };

    int visitantes[num_centros][years][meses] = {0};
    int opcion;

    do {
        cout << "seleccione una opción:\n";
        cout << "1. ingresar visitantes\n";
        cout << "2. mostrar estadísticas\n";
        cout << "3. salir\n";
        cin >> opcion;

        if (opcion == 1) {
            char letra_centros;
            int year, mes, cantidad;
            bool seguir = true;

            while (seguir) {
                cout << "centros turísticos:\n";
                for (int i = 0; i < num_centros; i++) {
                    cout << char('a' + i) << ". " << centros[i] << endl;
                }

                cout << "seleccione un centro turístico (ingrese la letra): ";
                cin >> letra_centros;

                int centro_seleccionado = letra_centros - 'a';
                if (centro_seleccionado < 0 || centro_seleccionado >= num_centros) {
                    cout << "selección inválida. intente de nuevo.\n";
                    continue;
                }

                cout << "ingrese año (0-4): ";
                cin >> year;
                cout << "ingrese mes (0-11): ";
                cin >> mes;
                cout << "cantidad de visitantes: ";
                cin >> cantidad;

                if (year >= 0 && year < years && mes >= 0 && mes < meses) {
                    visitantes[centro_seleccionado][year][mes] += cantidad;
                    cout << "visitantes registrados correctamente.\n";
                } else {
                    cout << "año o mes inválido.\n";
                }

                cout << "¿desea seguir ingresando datos? (1: sí, 0: no): ";
                cin >> seguir;
            }
        } else if (opcion == 2) {
            int total_visitantes[num_centros] = {0};

            for (int i = 0; i < num_centros; i++) {
                for (int j = 0; j < years; j++) {
                    for (int k = 0; k < meses; k++) {
                        total_visitantes[i] += visitantes[i][j][k];
                    }
                }
            }

            int max_visitantes = 0, min_visitantes = total_visitantes[0];
            int centro_mas_visitado = 0, centro_menos_visitado = 0;

            for (int i = 0; i < num_centros; i++) {
                if (total_visitantes[i] > max_visitantes) {
                    max_visitantes = total_visitantes[i];
                    centro_mas_visitado = i;
                }
                if (total_visitantes[i] < min_visitantes) {
                    min_visitantes = total_visitantes[i];
                    centro_menos_visitado = i;
                }
            }

            int max_mes = 0, min_mes = visitantes[0][years - 1][0];
            int mes_mayor_afluencia = 0, mes_menor_afluencia = 0;

            for (int k = 0; k < meses; k++) {
                for (int i = 0; i < num_centros; i++) {
                    if (visitantes[i][years - 1][k] > max_mes) {
                        max_mes = visitantes[i][years - 1][k];
                        mes_mayor_afluencia = k;
                    }
                    if (visitantes[i][years - 1][k] < min_mes) {
                        min_mes = visitantes[i][years - 1][k];
                        mes_menor_afluencia = k;
                    }
                }
            }

            cout << "total de visitantes por centro:\n";
            for (int i = 0; i < num_centros; i++) {
                cout << centros[i] << ": " << total_visitantes[i] << " visitantes.\n";
            }

            cout << "centro más visitado: " << centros[centro_mas_visitado] << " con " << max_visitantes << " visitantes.\n";
            cout << "centro menos visitado: " << centros[centro_menos_visitado] << " con " << min_visitantes << " visitantes.\n";

            cout << "mes de mayor afluencia en el último año: mes " << mes_mayor_afluencia + 1 << " con " << max_mes << " visitantes.\n";
            cout << "mes de menor afluencia en el último año: mes " << mes_menor_afluencia + 1 << " con " << min_mes << " visitantes.\n";
        }
    } while (opcion != 3);

    return 0;
}
