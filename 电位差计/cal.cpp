#include<cstdio>
#include<cmath>
using namespace std;

double e[6];

int main()
{
    double E=0,u=0;
    for(int i=1;i<=5;i++) scanf("%lf",&e[i]),E+=e[i];
    E/=5;
    for(int i=1;i<=5;i++) u+=(E-e[i])*(E-e[i]);
    u=sqrt(u/20);
    printf("%.10lf",u*1.14);
    return 0;
}