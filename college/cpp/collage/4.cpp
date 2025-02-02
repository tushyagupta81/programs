#include<iostream>
using namespace std;

class number{
    protected:
        int a,b;
    public:
        void getdata(){
            cin>>a>>b;
        }
};
class sub:public number{
    private:
        int tot;
    public:
        void calculate(){
            tot = a-b;
        }
        void show(){
            cout<<"Subtraction"<<endl;
            cout<<"Total = "<<tot<<endl;
        }
};
class add:public number{
    private:
        int tot;
    public:
        void calculate(){
            tot = a+b;
        }
        void show(){
            cout<<"Addition"<<endl;
            cout<<"Total = "<<tot<<endl;
        }
};

int main(){
    add a;
    sub b;
    a.getdata();
    a.calculate();
    a.show();
    b.getdata();
    b.calculate();
    b.show();
    return 0;
}
