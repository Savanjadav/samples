#include <iostream>
using namespace std;
class replace
{
public:
    int arr[50], k, count=0, n, i;
    void input()
    {
        cout<<"Enter the number of inputs: ";
        cin>>n;
        cout<<"Enter the numbers: "<<endl;
        for (int i=0;i<n;i++)
        {
            do
            {
                cin>>arr[i];
                if (arr[i]<=0)
                {
                    cout<<"Please enter positive value"<<endl;
                }
                else
                {
                    break;
                }
            } while (1==1);
        }
    }
    void output()
    {
        cout<<"Array is: "<<endl;
        for (i=0;i<n;i++)
        {
            cout<<arr[i]<<" ";
        }
    }
    void key()
    {
        cout<<"\nEnter key: ";
        cin>>k;
        for (i=0;i<n;i++)
        {
            if (arr[i]==k)
            {
                arr[i]=-1;
                count=count+1;
            }
        }
        cout<<"--------------------After Replacement--------------------"<<endl;
        cout<<"Final array is: "<<endl;
        for (i=0;i<n;i++)
        {
            cout<<arr[i]<<" ";
        }
        cout<<"\n"<<count<<" replacements done"<<endl;
    }
};
int main()
{
    replace a1;
    a1.input();
    a1.output();
    a1.key();
}