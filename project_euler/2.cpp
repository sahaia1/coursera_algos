#include <iostream>
#include <iterator>
#include <map>

using namespace std;

int fibo(int x, map<int, int> &fib)
{
    map<int, int>::iterator retval;
    retval = fib.find(x);
    if (retval != fib.end())
    {
        return retval->second;
    }
    else
    {
        int value = fibo(x - 1, fib) + fibo(x - 2, fib);
        fib.insert(pair<int, int>(x, value));
        return value;
    }
}
int main()
{
    map<int, int> fib;
    fib.insert(pair<int, int>(1, 1));
    fib.insert(pair<int, int>(2, 2));

    int sum = 0;
    int r = 1;

    while (1)
    {
        int t = fibo(r++, fib);
        if (t > 4000000)
            break;
        if (t % 2 == 0)
            sum += t;
    }
    cout << sum << endl;
    return 0;
}