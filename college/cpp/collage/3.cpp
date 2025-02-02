#include<iostream>
using namespace std;

class shape{
    protected:
        int sides;
    public:
        void tellShape(){
            if(sides==3){
                cout<<"Trianlge"<<endl;
            }else if(sides==4){
                cout<<"Quadrilateral"<<endl;
            }
        }
};
class triangle:public shape{
    public:
        triangle(){
            sides = 3;
        }
};
class quadrilateral:public shape{
    public:
        quadrilateral(){
            sides = 4;
        }
};
int main(){
    triangle a;
    quadrilateral b;
    a.tellShape();
    b.tellShape();
    return 0;
}
