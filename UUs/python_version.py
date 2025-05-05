import random
import heapq
from collections import deque

# ---------- 資料結構定義 ----------

def create_event(time, instruction):
    return (time, instruction)  # for heapq, use tuple for auto-ordering

def create_work(duration, produced_time):
    return {
        'duration': duration,
        'produced_time': produced_time
    }

def create_server():
    return {
        'processing_from': -1.0,
        'processing_to': -1.0
    }


# ---------- Server 操作 ----------

def server_is_available(server, now_time):
    if now_time + 1e-6 < server['processing_to']:
        return False
    server['processing_from'] = -1.0
    server['processing_to'] = -1.0
    return True

def server_pick(server, now_time, work):
    waiting_time = now_time - work['produced_time']
    server['processing_from'] = now_time
    server['processing_to'] = now_time + work['duration']
    return waiting_time

def server_finishing_time(server):
    return server['processing_to']


# ---------- 模擬主邏輯 ----------

def simulate(argument):
    servers = [create_server() for _ in range(argument['number_of_servers'])]
    events = []
    work_queue = deque()

    heapq.heappush(events, create_event(0.0, 'arrival'))

    total_waiting_time = 0.0
    jobs_dispatched = 0
    iteration = 0

    while events:
        time, instruction = heapq.heappop(events)

        iteration += 1

        if instruction == 'arrival':
            if jobs_dispatched >= argument['number_of_jobs']:
                continue

            jobs_dispatched += 1

            inter = argument['inter_arrival_start'] + random.random() * (argument['inter_arrival_end'] - argument['inter_arrival_start'])
            service_time = argument['service_time_start'] + random.random() * (argument['service_time_end'] - argument['service_time_start'])

            work_queue.append(create_work(service_time, time))

            heapq.heappush(events, create_event(time + inter, 'arrival'))

        for server in servers:
            if work_queue and server_is_available(server, time):
                work = work_queue.popleft()
                waiting_time = server_pick(server, time, work)
                heapq.heappush(events, create_event(server_finishing_time(server), 'job_finish'))
                total_waiting_time += waiting_time
                break

    return total_waiting_time / jobs_dispatched if jobs_dispatched > 0 else 0.0


# ---------- 主程式 ----------

def main():
    random.seed()

    a = int(input("Inter-arrival time [a]: "))
    b = int(input("Inter-arrival time [b]: "))
    c = int(input("Service time [c]: "))
    d = int(input("Service time [d]: "))
    s = int(input("Number of servers: "))
    n = int(input("Number of jobs: "))


    # arg = create_argument(a, b, c, d, n, s)
    avg_waiting = simulate({
        'inter_arrival_start': a,
        'inter_arrival_end': b,
        'service_time_start': c,
        'service_time_end': d,
        'number_of_jobs': n,
        'number_of_servers': s
    })

    print(f"\nAverage Waiting Time: {avg_waiting:.4f}")

if __name__ == '__main__':
    main()