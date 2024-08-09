#include<iostream>
using namespace std;

class animal{
    private:
        int feed;
        int sleep;
    public:
        void setFeed(){
            cin>>feed;
        }
        void setSleep(){
            cin>>sleep;
        }
    protected:
        int getCondition(){
            if(sleep==1 && feed==1){
                return 1;
            }else{
                return 0;
            }
        }
};
class dog:public animal{
    private:
        void bark(){
            cout<<"BARK!"<<endl;
        }
    public:
        void checkCondition(){
            if(getCondition()==0){
                bark();
                cout<<"Bad Condition"<<endl;
                bark();
            }else{
                cout<<"Good condition"<<endl;
            }
        }
};
int main(){
    dog o;
    o.setFeed();
    o.setSleep();
    o.checkCondition();
    o.setFeed();
    o.setSleep();
    o.checkCondition();
    return 0;
}
