#include<iostream>
#include<map>
using namespace std;

int main(){
    int a;
    cin>>a;
    map<string,long> per;
    map<string,long>::iterator it;
    for(int i=0;i<a;i++){
        string name;
        long number;
        cin>>name>>number;
        per[name]=number;
    }
    
    string find[100001];
    // int p=0;
    int t=0;
    while(cin>>find[t]){
        t++;
    }
    // for(int i=0;i<100001;i++){
    //     cin>>find[i];
    //     p++;
    // }

    for(int i=0;i<t;i++){
        it = per.find(find[i]);
        if(it != per.end()){
            cout<<it->first<<"="<<it->second<<endl;
        }
        else{
            cout<<"Not found"<<endl;
        }
        // int s=0;
        // for(auto element : per){
        //     if(find[i]==element.first){
        //         s=1;
        //         cout<<element.first<<"="<<element.second<<endl;
        //     }
        // }
        // if(s==0){
        //     cout<<"Not found"<<endl;
        // }
    }
    return 0;
}
