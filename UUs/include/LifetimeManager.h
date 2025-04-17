#ifndef __LIFETIME_MANAGER_H__
#define __LIFETIME_MANAGER_H__

#include <queue>
#include <string>
#include <vector>

#include "Server.h"

using namespace std;

struct argument{
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
    bool operator<(const event& rhs) const { return time < rhs.time; }
};

class LifetimeManager {
   private:
    vector<Server> servers;
    // config
    Time inter_arrival;
    Time service;

    double present_arrival_time;
    priority_queue<event> events;
    
    int total_jobs;
    int total_servers;

   public:
    LifetimeManager() = default;
    void config(argument);
    int start();
};

#endif