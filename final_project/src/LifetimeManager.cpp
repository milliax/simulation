#include "LifetimeManager.h"

LifetimeManager::~LifetimeManager() {
    // free all servers

    for (auto s : servers) {
        delete s;
    }
    servers.clear();

    return;
}

LifetimeManager::LifetimeManager() {
    // constructor
    // initialize servers

    queue<work> empty_work_todo;
    swap(work_todo, empty_work_todo);

    priority_queue<event, vector<event>, CompareEvent> empty_events;
    swap(events, empty_events);

    servers.clear();

    return;
}

void LifetimeManager::config(argument input) {
    // need intervals

    arg = input;

    // create sufficient servers

    servers.clear();

    for (int i = 0; i < arg.number_of_servers; ++i) {
        Server* s = new Server();
        // servers.push_back(&s);
        servers.push_back(s);
    }

    return;
}

double LifetimeManager::start() {
    // generate first arrival time

    events.emplace(event{time : 0, instruction : "arrival"});

    // statistics variables
    double total_waiting_time = 0;
    int jobs_dispatched = 0;
    int num_of_iteration = 0;

    // start the simulation
    // while ((jobs_dispatched < arg.number_of_jobs) || (work_todo.size() > 0))

    while (!events.empty()) {
        // assign works to available server
        event latest_event = events.top();
        events.pop();

        if (show_iteration) {
            printf("\nIteration: %d\n", num_of_iteration++);
            printf("statistics: \n");
            printf("number of jobs: %ld\n", work_todo.size());
            printf("number in queue: %ld\n", events.size());
            printf("number of servers: %ld\n", servers.size());
            printf("number of jobs dispatched: %d\n", jobs_dispatched);
            printf("this Time: %f\n", latest_event.time);
            printf("this Instruction: %s\n", latest_event.instruction.c_str());
            printf("\n");

            // print all events
            // printf("Events in queue: \n");
            // vector<event> events_copy;
            // while (!events.empty()) {
            //     events_copy.push_back(events.top());
            //     events.pop();

            //     printf("Time: %f, Instruction: %s\n",
            //     events_copy.back().time,
            //            events_copy.back().instruction.c_str());
            // }
            // for (auto e : events_copy) {
            //     events.emplace(e);
            // }
            // printf("\n");
        }

        if (latest_event.instruction == "arrival") {
            if (jobs_dispatched >= arg.number_of_jobs) {
                continue;
            }
            jobs_dispatched += 1;

            // generate next arrival

            if (show_arrival_info) {
                printf("\nJob arrived at %f\n", latest_event.time);
            }

            const double inter =
                arg.inter_arrival_start +
                (double)rand() / (RAND_MAX) *
                    (arg.inter_arrival_end - arg.inter_arrival_start);
            const double service_time =
                arg.service_time_start +
                (double)rand() / (RAND_MAX) *
                    (arg.service_time_end - arg.service_time_start);

            work_todo.emplace(work{
                duration : service_time,
                produced_time : latest_event.time
            });  // push new work into queue

            events.emplace(event{
                time : latest_event.time + inter,
                instruction : "arrival"
            });  // next arrival time

        } else if (latest_event.instruction == "job_finish") {
            // job finished
            if (show_arrival_info) {
                printf("\nJob finished at %f\n", latest_event.time);
            }

        } else {
            printf("Undefined instruction in LifetimeManager\n");
        }

        if (!work_todo.empty()) {
            // push job into servers
            // printf("number of servers: %ld\n", servers.size());

            // bool server_available = false;

            for (auto s : servers) {
                if (s->available(latest_event.time)) {  // server is available
                    auto work = work_todo.front();
                    work_todo.pop();

                    // server_available = true;

                    if (show_dispatch_info) {
                        printf("Server dispatched at %f, with duration: %f\n",
                               latest_event.time, work.duration);
                    }

                    double waiting_time = s->picked(latest_event.time, work);
                    // push finish time to timestamp(event)
                    events.emplace(event{
                        time : s->finishing_time(),
                        instruction : "job_finish"
                    });

                    total_waiting_time += waiting_time;
                    break;
                }
            }

            // if(!server_available) {
            //     // printf("Server is available\n");
            //     printf("No server available, job is waiting\n");
            // } 
        }
    }

    return total_waiting_time / jobs_dispatched;
}