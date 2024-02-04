#include<iostream>
using namespace std;

template<class T>
class arithemetic
{
    private:
        T a;
        T b;

    public:
        arithemetic(T a, T b);
        T add();
        T sub();
};
        template<class T>
        arithemetic<T>::arithemetic(T a, T b)
        {
            this->a=a;
            this->b=b;
        }
        template<class T>
        T arithemetic<T>::add()
        {
            T c;
            c = a + b;
            return c;
        }
        template<class T>
        T arithemetic<T>::sub()
        {
            T c;
            c = a - b;
            return c;
        }


int main()
{
    arithemetic<float> ar(10.67,5.32);
    cout<<"Add : "<<ar.add()<<endl;
    cout<<"Sub : "<<ar.sub()<<endl;

    return 0;
}