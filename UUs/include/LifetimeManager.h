#ifndef __LIFETIME_MANAGER_H__
#define __LIFETIME_MANAGER_H__

#include <unistd.h>  // For UNIX/Linux systems

#include <queue>
#include <string>
#include <vector>

#include "Server.h"
#include "struct.h"

using namespace std;

class LifetimeManager {
   private:
    // config
    argument arg;

    vector<Server*> servers;
    priority_queue<event, vector<event>, CompareEvent> events;
    // maintain a PQ that top is always the earliest
    queue<work> work_todo;
    // queue of works to be done
    // FIFO

   public:
    ~LifetimeManager();
    LifetimeManager();
    void config(argument);
    double start();
};

#endif