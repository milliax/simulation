#include "LifetimeManager.h"

void LifetimeManager::config(argument input) {
    // need intervals

    inter_arrival.start = input.inter_arrival_start;
    inter_arrival.end = input.inter_arrival_end;
    service.start = input.service_time_start;
    service.end = input.service_time_end;

    total_jobs = input.number_of_jobs;
    total_servers = input.number_of_servers;

    // create sufficient servers

    servers.clear();

    for (int i = 0; i < total_servers; ++i) {
        Server* s = new Server(service.start, service.end);
        servers.emplace_back();
    }

    return;
}

int LifetimeManager::start() {
    // generate first arrival time

    events.emplace(event{time : 0, instruction : "arrival"});

    // start of emulating
    int total_time_elapsed = 0;
    int jobs_dispatched = 0;

    while (!events.empty()) {
        // assign works to available server
        event latest_event = events.top();
        events.pop();

        if (latest_event.instruction == "arrival") {
            if (jobs_dispatched >= total_jobs) {
                continue;
            }

            // TODO: generate arrival time and assign to server

        } else {
            printf("Undefined instruction in LifetimeManager\n");
        }
    }

    return total_time_elapsed;
}