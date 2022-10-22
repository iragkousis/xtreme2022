#include <iostream>
using namespace std;


int main(){
	int n, t; 
	int input;
	bool in[30][180];
	for(int i; i<30; ++i){
		for(int j; j<180; ++j){
			in[i][j]=0;
		}
	}
	int count;
	cin >> t;
	for(int i=0; i<t; i++){
		cin >> n; 
		if(n==0) {
			cout << 1 << endl;
			continue;
		}

		count = 0;
		for(int j=0; j<n; ++j){
			scanf("%d", &input);
			cout << "|" << input;
			if(input<0) {
				input = input%360;
				input += 360;
			}
			input = input%180;
			cout <<"|" <<  input << endl;
			if (in[i][input]==0){
				cout << "true1" << endl;
				in[i][input]=1;
				++count;
			}

		}
		cout << count*2 << endl;
	}
	return 0;
}