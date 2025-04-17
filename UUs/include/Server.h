#ifndef __SERVER_H__
#define __SERVER_H__

#include <cstdlib>

using namespace std;

class Server {
   private:
    double service_time_generated_from;
    double service_time_generated_to;

    double processing_from;
    double processing_to;

   public:
    Server(int, int) {};

    bool available(double);
    void picked(double);
    double finishing_time();
};

#endif