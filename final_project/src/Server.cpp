#include "Server.h"

Server::Server() {
    processing_from = -1;  // not working
    processing_to = -1;    // not working
}

double Server::picked(double now_time, work work_selected) {
    // generate time randomly

    const double waiting_time = now_time - work_selected.produced_time;

    processing_from = now_time;
    processing_to = now_time + work_selected.duration;

    // printf("\nServer picked job\n");
    // printf("now_time: %f\n", now_time);
    // printf("work_selected.produced_time: %f\n", work_selected.produced_time);
    // printf("work_selected.duration: %f\n", work_selected.duration);
    // printf("waiting_time: %f\n", waiting_time);
    // printf("processing_from: %f\n", processing_from);
    // printf("processing_to: %f\n", processing_to);
    // printf("\n");

    return waiting_time;
}

double Server::finishing_time() { return processing_to; }

bool Server::available(double now_time) {
    // only checking the right bound
    // don't know if it would cause any problem

    // printf("\nServer available check\n");
    // printf("now_time: %f\n", now_time);
    // printf("processing_from: %f\n", processing_from);
    // printf("processing_to: %f\n", processing_to);
    // printf("\n");

    if (now_time + 1e-6 < processing_to) { // 1e-6 is a small number
        return false;
    }

    // this server is available to handle new requests
    // so it is not processing anything

    // printf("\nServer is back to available again\n");
    processing_from = -1;
    processing_to = -1;

    return true;
}