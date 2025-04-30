#ifndef __STRUCT_H
#define __STRUCT_H

#include <string>

using namespace std;

const bool show_iteration = true;
const bool show_dispatch_info = true;
const bool show_arrival_info = true;

struct argument {
    int inter_arrival_start;
    int inter_arrival_end;

    int service_time_start;
    int service_time_end;

    int number_of_jobs;
    int number_of_servers;
};

struct Time {
    int start;
    int end;
};

struct event {
    double time;
    string instruction;
};

struct work {
    double duration;
    double produced_time;
};

struct CompareEvent {
    bool operator()(const event& lhs, const event& rhs) {
        return lhs.time > rhs.time;  // Reverse logic for min-heap
    }
};

#endif