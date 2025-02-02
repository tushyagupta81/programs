#include<iostream>
using namespace std;

class b{
    private:
        float f;
    public:
        b(){
            f=10;
        }
        operator float(){
            return f;
        }
};

int main(){
    b obj;
    float t;
    t = obj;
    cout<<t;
    return 0;
}
