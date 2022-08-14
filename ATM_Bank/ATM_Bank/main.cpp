#include<iostream>
#include<string.h>
#include<Windows.h>
using namespace std;

int main(){
	int pin, choice, balanse = 1000;
	float witdraw, depost;
	int correct = true;
	cout << "\t*****tWellcome to the ATM_bank*****\n\n\n";
	cout << "Enter PIN: ";
	cin >> pin;
	while (pin != 2425){
		cout << "Plase Enter acrrect PIN.....\n";
		cout << "Enter PIN: ";
		cin >> pin;
	}
	do
	{
		cout << "\n 1. Cheek acount" << endl;
		cout << "\n 2. Witdeaw Cash" << endl;
		cout << "\n 3. Depost Cash" << endl;
		cout << "\n 4. Quit" << endl;
		cout << "Sheas any Option : ";
		cin >> choice;
		switch (choice){
		case 1:
			cout << "Your Cash New : $" << balanse << endl;
			break;
		case 2:
			cout << "Enter amumet: ";
			cin >> witdraw;
			if (witdraw > balanse){
				cout << "Your Cash is not Equal";
			}
			else
			{
				balanse = balanse - witdraw;
				cout << "Your Cash new$" << balanse << endl;
				break;
		case 3:
			cout << "Enter amount Set ";
			cin >> depost;
			balanse = balanse + depost;
			cout << "Your Corrent balanse is: $" << balanse << endl;
			break;
		case 4:
			cout << "\n\n******Thank you for using ATM_Bank ******\n\n";
			correct = false;
			break;

		default:
			cout << "Invaled Input\n";
			break;
			}
		}
		
	} while (correct != false);
}