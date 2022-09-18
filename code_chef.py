#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int p,count=0;
	int x;
	for(int i=0;i<4;i++){
	    cin>>p;
	    if(p>=10){
	        count++;
	    }
	}
	
	cout<<count;
	return 0;
}
