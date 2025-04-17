#include "Server.h"

Server::Server(int service_time_generated_from, int service_time_generated_to) {
    this->service_time_generated_from = service_time_generated_from;
    this->service_time_generated_to = service_time_generated_to;

    processing_from = -1;  // not working
    processing_to = -1;    // not working
}

void Server::picked(double now_time) {
    // generate time randomly

    const double inter_arrival =
        service_time_generated_from +
        (double)rand() / (RAND_MAX) *
            (service_time_generated_to - service_time_generated_from);

    processing_from = now_time;
    processing_to = now_time + inter_arrival;

    return;
}

bool Server::available(double now_time) {
    // only checking the right bound
    // don't know if it would cause any problem

    if (now_time <= processing_to) {
        return false;
    }

    // this server is available to handle new requests
    // so it is not processing anything

    processing_from = -1;
    processing_to = -1;

    return true;
}