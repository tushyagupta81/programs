#include <iostream>

using namespace std; 

class bank{
    private:
        char name[100];
        int acc;
        char t;
        int bal;
    public:
        void assign(){
            cin >>name>>acc>>t>>bal;
        }
        void deposit(int b){
            bal += b;
        }
        void withdraw(int a){
            bal -= a;
        }
        void holder(){
            cout<<name<<" "<<bal<<endl;
        }
};

int main(){
    bank o;
    o.assign();
    o.holder();
    o.deposit(500);
    o.holder();
    o.withdraw(1000);
    o.holder();
    return 0;
}
