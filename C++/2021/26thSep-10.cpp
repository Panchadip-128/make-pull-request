#include <iostream>
using namespace std;
 
void Binary(int n){
int arr[1000];
int i=0;
    while(n>0){
        arr[i]=n%2;
        n=n/2;
        i++;  
    }
    for(int j=i-1;j>=0;j--){
        cout<<arr[j];
    }
    cout<<" ";
}
void BinaryNoGeneration(int n){
for(int i=1;i<=n;i++){
    Binary(i);
}
}
int main()
{
    int n;
    cout<<"Enter the range of n ";
    cin>>n;
    cout<<"Binary number from 1 to "<<n<<" "<<"is"<<endl;
    BinaryNoGeneration(n);
    return 0;
}
