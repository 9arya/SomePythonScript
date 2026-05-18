//MIT License
//
//Copyright (c) 2026 9arya
#include<iostream>
using namespace std;
int main(){
	long Integer;
	cout << "enter number:";
	cin >> Integer;
	if (Integer < 1){
		cout << "InValidInput: input is not number or is below 1" << endl;
		return 1;
	}
	cout << Integer << endl;
	for (long i = 2; i < Integer; i++){
		if (Integer % i == 0){
			cout << "is not prime number" << endl;
			return 1;
		}
	}
	cout << "is prime number" << endl;
	return 0;
}
