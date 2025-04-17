#include <stdio.h>
#include <stdlib.h>

#include <ctime>

#include "LifetimeManager.h"

int main() {
    std::srand(time(NULL));
    printf("Hello, World!\n");

    // ask for the inputs
    // inter-arrival time [a,b]
    // service time [c,d]
    // number of servers S
    // number of jobs N

    int a, b, c, d, s, n;

    a = 0;
    b = 10;
    c = 0;
    d = 20;

    s = 1;
    n = 1;

    int total_time_spent = 0;

    // for (int i = 0; i < n; ++i) {
    // this is the total job times
    LifetimeManager env = LifetimeManager();

    env.config(argument{

    });

    int time_spent = env.start();

    total_time_spent += time_spent;
    // }

    printf("Average Time Consumed: %f", (double)total_time_spent / n);

    return 0;
}