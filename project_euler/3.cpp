#include <iostream>
#include <cmath>

using namespace std;

int prime_fact(long number)
{
    for (long i = 2; i < ceil(sqrt(number)); i++)
    {
        if (number % i == 0)
        {
            return prime_fact(number / i);
        }
    }
    return number;
}
int main()
{
    long number = 600851475143;
    cout << prime_fact(number) << endl;
}