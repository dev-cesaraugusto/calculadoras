#include <iostream>
using namespace std;

int main() {
    double num1, num2;
    char operador;

    cout << "Insira o primeiro número: ";
    cin >> num1;

    cout << "Insira o operador matemático (+, -, *, /): ";
    cin >> operador;

    cout << "Insira o segundo número: ";
    cin >> num2;

    if (operador == '+') {
        cout << num1 << " + " << num2 << " = " << num1 + num2 << endl;
    }
    else if (operador == '-') {
        cout << num1 << " - " << num2 << " = " << num1 - num2 << endl;
    }
    else if (operador == '*') {
        cout << num1 << " * " << num2 << " = " << num1 * num2 << endl;
    }
    else if (operador == '/') {
        if (num2 == 0) {
            cout << "Divisão por zero!" << endl;
        }
        else {
            cout << num1 << " / " << num2 << " = " << num1 / num2 << endl;
        }
    }
    else {
        cout << "Operador inválido!" << endl;
    }

    return 0;
}
