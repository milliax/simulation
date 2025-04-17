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

    int job_available = 0;

    while (!events.empty()) {
        // assign works to available server
        event latest_event = events.top();
        events.pop();

        if (latest_event.instruction == "arrival") {
            if (jobs_dispatched >= total_jobs) {
                continue;
            }
            job_available += 1;

            // generate next arrival

            const double inter = inter_arrival.start +
                                 (double)rand() / (RAND_MAX) *
                                     (inter_arrival.end - inter_arrival.start);
            events.emplace(event{
                time : latest_event.time + inter,
                instruction : "arrival"
            });

        } else if (latest_event.instruction == "job_finish") {
            // TODO: handle event finished
        } else {
            printf("Undefined instruction in LifetimeManager\n");
        }

        if (job_available > 0) {
            // push job into servers
            for (auto s : servers) {
                if (s.available(latest_event.time)) {
                    s.picked(latest_event.time);
                    // push finish time to timestamp(event)
                    events.emplace(event{
                        time : s.finishing_time(),
                        instruction : "job_finish"
                    });
                    job_available -= 1;
                    break;
                }
            }
        }
    }

    return total_time_elapsed;
}