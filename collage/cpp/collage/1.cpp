#include<iostream>
using namespace std;

class Vehicle{
    private:
        int fuel;
        int capacity;
    public:
        void getFuel(){
            cin>>fuel;
        }
        void getCapacity(){
            cin>>capacity;
        }
        void showFuel(){
            cout<<"Fuel = "<<fuel<<endl;
        }
        void showCapacity(){
            cout<<"Capacity = "<<capacity<<endl;
        }
};
class bus:public Vehicle{
    public:
        void getInfo(){
            getFuel();
            getCapacity();
        }
        void showInfo(){
            cout<<"Bus"<<endl;
            showFuel();
            showCapacity();
        }
};
class car:public Vehicle{
    public:
        void getInfo(){
            getFuel();
            getCapacity();
        }
        void showInfo(){
            cout<<"Car"<<endl;
            showFuel();
            showCapacity();
        }
};

int main(){
    car c;
    bus b;
    b.getInfo();
    b.showInfo();
    c.getInfo();
    c.showInfo();
    return 0;
}
