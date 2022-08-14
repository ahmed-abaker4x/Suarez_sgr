#include<iostream>
#include<conio.h>
using namespace std;
class name
{public:
	char f_name[10];
	char m_name[10];
	char l_name[10];
};
class data
{public:
	int day, mounth, year;
};
class student
{public:
	name na;
	int number;
	data d;
};
main(){
	student st[2];
	int i;
	cout << "Enter student info: " << endl;
	for ( i = 0; i < 3; i++){
		cout << "Enter the Value of the Student " << i + 1 << endl;
		cout << "Student farst_name " <<i+1<<" ";
		cin >> st[i].na.f_name;
		cout << "Student medel_name " <<i+1<<" ";
		cin >> st[i].na.m_name;
		cout << "Student last_name"<<i+1 <<" " ;
		cin >> st[i].na.l_name;
		cout << "Student number" <<i+1 <<" ";
		cin >> st[i].number;
		cout << "Student regster day" << i + 1 << " ";
		cin >> st[i].d.day;
		cout << "Student regster mounth:" << i + 1 << " ";
		cin >> st[i].d.mounth;
		cout << "Student regster year:" << i + 1 << " ";
		cin >> st[i].d.year;
		cout << endl;
	}
	for (i = 0; i < 2; i++){
		cout<<"Imformention of the Student " << i + 1 << endl;
		cout << "studant name: " << st[i].na.f_name << " ";
		cout << st[i].na.m_name << " ";
		cout << st[i].na.l_name << endl;
		cout << "Student number: " << st[i].number << endl;
		cout << "Student regster day: " << st[i].d.day << ".";
		cout << st[i].d.mounth << ".";
		cout << st[i].d.year << endl;
		cout << endl;
	}
	getch();
}



