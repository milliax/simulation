# UUs simulation

## Debugging

You can enable debugging rules in struct.h

## Target

to build a simulation system that can handle UUs.

### Inputs
```
inter-arrival time U[a,b]
service time U[c,d]
number of servers: S
number of jobs: n
```

## Structure

### main
to receive the arguments.

### lifetime_manager

time discreted

    Store up coming events with time and what would happen when time comes. (sorted) (priority queue)
    Do that in the next iteration.

### server

the processing server that record the start time and end time for the server.

### struct.h

define all the structs used in this program

### excutables

```
make
```

then main or main.exe is what you want