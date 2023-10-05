 // 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F
#include<iostream>
using namespace std;

int main(){
    int n;
    cin >> n; 
    if (n >= 90){
        cout << "A" << endl;
    }else if (n<=89 && n>=80){
        cout << "B" << endl;
    }else if (n<=79 && n >=70){
        cout << "C" << endl; 
    }else if(n<=69 && n>=60){
        cout << "D"<< endl; 
    }else{
        cout << "F"<< endl; 
    }
    return 0;
}