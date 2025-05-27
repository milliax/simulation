
from database import Database
from area import AreaDispatcher
from typing import List, Tuple

import os

from dotenv import load_dotenv
load_dotenv()

isDev = os.getenv("DEBUG") == "true"

if __name__ == "__main__":
    print("Program started")

    resources = Database(user="11302_SIM",
                         password="11302",
                         hostname="140.113.59.168")

    resources.connect()

    query = resources.execute_query(
        "SELECT * FROM SIM_STUDENT. SIM_ALLOCATE_DISPATCH_1")

    query2 = resources.execute_query(
        "SELECT * FROM SIM_STUDENT. SIM_ALLOCATE_DISPATCH_2")

    resources.close()

    iter: list[dict[str, int]] = []

    if not query or not query2:
        print("Database query returned no results.")
        exit(1)

    for q in query2:
        i = {
            "id": q[0],
            "workers": q[1],
            "limitation": q[2],
        }
        iter.append(i)

    """ Tests from database """
    print("tests: ")
    for i in iter:
        print("id: ", i["id"])
        print("workers: ", i["workers"])
        print("time limitations: ", i["limitation"])

    layout = {}

    for row in query:
        # print(row)
        instance = row[0]
        area = row[1]
        machine = row[2]
        processing_time = row[3]
        load_unload_time = row[4]

        if instance not in layout:
            layout[instance] = {}

        if area not in layout[instance]:
            layout[instance][area] = []

        layout[instance][area].append({
            "machine": machine,
            "processing_time": processing_time,
            "load_unload_time": load_unload_time
        })

    # print(dictionary)

    caching: dict[str, dict[int, int]] = {}

    """
    caching: {
        "area_name": {
            "worker_cnt": processing_time
        }
    }
    
    """

    for e in iter:
        print(f"Instance: {e['id']}")
        print(f"  Total Workers: {e['workers']}")
        print(f"  Time limitation: {e['limitation']} seconds")

        better_solution_found = True
        minimum_waiting_time = 1e10
        best_permutation = []

        # distribut e['workers'] workers to areas

        # using instance 1 for all tasks
        number_of_areas = len(layout['1'].keys())
        permutations = []

        for i in range(number_of_areas):
            # distribute workers evenly
            if i == number_of_areas - 1:
                # last area gets all remaining workers
                workers = e["workers"] - \
                    (e["workers"] // number_of_areas) * (number_of_areas - 1)
            else:
                workers = e["workers"] // number_of_areas

            permutations.append(workers)

        print(f"  Workers distribution: {permutations}")

        # for area in layout[1]:

        while better_solution_found:
            # continue until no better solution is found

            all_permutations = []
            better_solution_found = False

            for i in range(len(permutations)):
                for j in range(len(permutations)):
                    if i != j:
                        new_permutation = permutations.copy()
                        new_permutation[i] += 1
                        new_permutation[j] -= 1
                        all_permutations.append(new_permutation)

            if isDev:
                print(f"  All permutations: {all_permutations}")

            for p in all_permutations:

                sum = 0

                for tied in zip(p, layout['1'].keys()):
                    # print(f"tied: {tied}")

                    if caching.get(tied[1]) is not None and caching[tied[1]].get(tied[0]) is not None:
                        sum += caching[tied[1]][tied[0]]
                        if isDev:
                            print(
                                f"  HIT cache for area {tied[1]} with {tied[0]} workers")
                        continue

                    if isDev:
                        print(f"  Area: {tied[1]}, Workers: {tied[0]}")

                    a = AreaDispatcher(
                        number_of_workers=tied[0],
                        # using instance 1 for all tasks
                        machines=layout['1'][tied[1]],
                        total_processing_time=e["limitation"],
                        area_name=tied[1],
                    )

                    result = a.dispatch()
                    if isDev:
                        print(
                            f"  Processing time for area {tied[1]} with {tied[0]} time: {result}")
                    sum += result

                    caching.setdefault(tied[1], {})[tied[0]] = result

                if sum < minimum_waiting_time:
                    minimum_waiting_time = sum
                    best_permutation = p
                    better_solution_found = True
                    permutations = p
                    if isDev:
                        print(f"  Found better solution: {p} with time {sum}")

                    p = permutations

                if isDev:
                    print(f"Total processing time: {sum}, with permutation: {p}")

            # for machine in dictionary[key][area]:
            #     print(f"    Machine: {machine['machine']}")
            #     print(f"      Processing time: {machine['processing_time']}")
            #     print(f"      Load/unload time: {machine['load_unload_time']}")

        print(
            f"Best permutation: {best_permutation} with time {minimum_waiting_time}")

    # print(f"caching: {caching}")

    """ write result back to database """
    # db = Database(user="TEAM_11",
    #               password="team11",
    #               hostname="140.113.59.168")

    # db.connect()

    # query = db.execute_query("SELECT * FROM SIM_STUDENT. SIM_ALLOCATE_DISPATCH_1")
