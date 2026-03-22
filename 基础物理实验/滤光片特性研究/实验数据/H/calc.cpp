#include<cstdio>
#include<cstdlib>
using namespace std;


int main()
{
    freopen("yellowblue.txt","r",stdin);
    freopen("out.txt","w",stdout);
    float b[2][500];
    for(int i=0;i<=300;i++)
    {
        scanf("%f%f",&b[0][i],&b[1][i]);
        printf("%.1f\n",b[1][i]);
    }
    return 0;
}