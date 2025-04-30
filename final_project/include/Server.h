#ifndef __SERVER_H__
#define __SERVER_H__

#include <cstdlib>

#include "struct.h"

using namespace std;

class Server {
   private:
    double processing_from;
    double processing_to;

   public:
    Server();

    bool available(double);
    double picked(double, work);
    double finishing_time();
};

#endif