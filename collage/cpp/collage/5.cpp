#include<iostream>
using namespace std;

class account{
    protected:
        int a;
    public:
        void getacc(){
            cin>>a;
        }
};
class programmer:public account{
    private:
        int bonus;
    public:
        void getbonus(){
            cin>>bonus;
        }
        void show(){
            cout<<"Total = "<<bonus+a<<endl;
        }
};

int main(){
    programmer a;
    a.getacc();
    a.getbonus();
    a.show();
    return 0;
}
