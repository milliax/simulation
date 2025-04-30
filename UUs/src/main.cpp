#include <stdio.h>
#include <stdlib.h>

#include <ctime>
#include <iostream>

#include "LifetimeManager.h"

int main() {
    std::srand(time(NULL));
    printf("Welcome to UUs Emulator\n");

    int a, b, c, d, s, n;

    // a = 0;
    // b = 10;
    // c = 0;
    // d = 20;

    // s = 1;
    // n = 5;

    LifetimeManager env = LifetimeManager();

    cout << "Please input the following parameters: " << endl;
    
    cout << "Inter-arrival time start: ";
    cin >> a;
    cout << "Inter-arrival time end: ";
    cin >> b;
    cout << "Service time start: ";
    cin >> c;
    cout << "Service time end: ";
    cin >> d;
    cout << "Number of servers: ";
    cin >> s;
    cout << "Number of jobs: ";
    cin >> n;
    // printf("Inter-arrival time start: %d\n", a);
    // printf("Inter-arrival time end: %d\n", b);
    // printf("Service time start: %d\n", c);
    // printf("Service time end: %d\n", d);
    // printf("Number of jobs: %d\n", n);
    // printf("Number of servers: %d\n", s);
    printf("====================================\n");

    env.config(argument{
        inter_arrival_start : a,
        inter_arrival_end : b,

        service_time_start : c,
        service_time_end : d,

        number_of_jobs : n,
        number_of_servers : s,
    });

    // printf("Start Emulation\n");
    double average_waiting_time = env.start();

    // printf("Average Waiting time: %f", average_waiting_time);
    cout << "Average Waiting time: " << average_waiting_time << endl;
    printf("====================================\n");

    return 0;
}