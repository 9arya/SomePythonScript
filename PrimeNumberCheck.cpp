//MIT License
//
//Copyright (c) 2026 9arya
#include<iostream>
#include<string>
using namespace std;
int main(int argc, char** argv){
	long Integer;
	if (argc < 2){
		cout << "enter number:";
		cin >> Integer;
	}else{Integer = stol(argv[1]);}
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
