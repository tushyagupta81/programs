#include<iostream>
using namespace std;

class Person{
    private:
        int age:
    public:
        Person(int a){
            if(a<0){
                age = 0;
                cout<<"Age is not valid, setting age to 0."<<endl;
            }else{
                age = a;
            }
        }
        void yearPasses(){
            age++;
        }
        void amIOld(){
            if(age<13){
                cout<<"You are young."<<endl;
            }else if(age>=13 && age<=18){
                cout<<"You are a teenager."<<endl;
            }else{
                cout<<"You are old."<<endl;
            }
        }
}

int main(){

    reutrn 0;
}
