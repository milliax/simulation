import numpy as np
import matplotlib.pyplot as plt

# 加工時間矩陣 (100 jobs x  Content edited for clarity processors)
pTime = [
    [80, 74, 130], [256, 20, 94], [67, 115, 18], [167, 6, 243], [39, 206, 238],
    [228, 280, 249], [41, 198, 251], [217, 2, 166], [
        128, 255, 226], [270, 21, 248],
    [140, 157, 89], [218, 284, 205], [
        188, 199, 173], [279, 216, 30], [156, 138, 35],
    [294, 201, 148], [112, 55, 169], [
        222, 75, 124], [90, 152, 106], [268, 57, 24],
    [239, 13, 160], [214, 60, 14], [235, 103, 92], [
        273, 175, 187], [163, 164, 64],
    [65, 109, 269], [220, 283, 71], [51, 170, 96], [
        105, 195, 23], [154, 192, 98],
    [56, 36, 276], [162, 274, 296], [70, 17, 104], [
        210, 174, 146], [42, 272, 151],
    [287, 116, 37], [209, 253, 45], [
        254, 252, 194], [202, 66, 171], [12, 82, 288],
    [54, 176, 141], [76, 101, 241], [61, 7, 48], [
        81, 259, 237], [246, 131, 184],
    [127, 281, 31], [183, 240, 95], [58, 8, 40], [9, 295, 207], [28, 250, 208],
    [219, 230, 144], [168, 4, 278], [52, 59, 189], [
        223, 108, 161], [132, 158, 177],
    [85, 69, 292], [165, 110, 221], [261, 11, 224], [26, 32, 29], [234, 68, 22],
    [1, 229, 258], [190, 38, 111], [203, 123, 211], [
        225, 300, 212], [182, 53, 121],
    [181, 118, 196], [185, 107, 135], [
        227, 260, 117], [83, 277, 263], [233, 5, 242],
    [271, 264, 72], [213, 25, 159], [126, 44, 122], [
        178, 231, 88], [142, 99, 244],
    [139, 298, 136], [282, 134, 77], [
        290, 27, 236], [10, 297, 114], [286, 47, 46],
    [186, 91, 245], [62, 204, 266], [73, 100, 143], [133, 93, 16], [150, 197, 15],
    [78, 76, 86], [3, 149, 125], [293, 50, 145], [34, 137, 49], [180, 285, 102],
    [155, 43, 257], [84, 153, 147], [120, 299, 262], [
        33, 129, 267], [215, 113, 191],
    [179, 193, 97], [79, 63, 87], [289, 119, 200], [
        232, 275, 172], [291, 265, 247]
]

# ==== 參數設定(與演算法相關) ====
NUM_ITERATION = 2000     # 世代數
NUM_CHROME = 300         # 染色體個數
NUM_BIT = 100            # 染色體長度 (工件數)
Pc = 0.755                 # 交配率
Pm = 0.0048               # 突變率

NUM_PARENT = NUM_CHROME
NUM_CROSSOVER = int(Pc * NUM_CHROME / 2)
NUM_CROSSOVER_2 = NUM_CROSSOVER * 2
NUM_MUTATION = int(Pm * NUM_CHROME * NUM_BIT)

np.random.seed()

# ==== 基因演算法函式 ====

def initPop():  # 初始化群體
    p = []
    for _ in range(NUM_CHROME):
        p.append(np.random.permutation(NUM_BIT))  # 隨機排列 0 到 NUM_JOB-1
    return p

def fitFunc(x):  # 適應度函數
    # combine pTime with order x
    process_time = [[pTime[i][0], pTime[i][1], pTime[i][2], x[i]]
                    for i in range(len(x))]

    process = sorted(process_time, key=lambda x: x[3])

    m1 = list(range(len(x)))
    m2 = list(range(len(x)))
    m3 = list(range(len(x)))

    # for i in range(len(x)):
    for i in range(len(x)):
        p1 = process[i][0]
        p2 = process[i][1]
        p3 = process[i][2]

        if i == 0:
            m1[i] = p1
            m2[i] = m1[0] + p2
            m3[i] = m2[0] + p3
        else:
            m1[i] = max(m1[i-1] + p1, m2[i-1])
            m2[i] = max(m1[i] + p2, m3[i-1])
            m3[i] = m2[i] + p3

    return -m3[len(x)-1]  # 負的最後工件的完成時間


def evaluatePop(p):  # 評估群體之適應度
    return [fitFunc(p[i]) for i in range(len(p))]


def selection(p, p_fit):  # 二元競爭式選擇法
    a = []
    for _ in range(NUM_PARENT):
        [j, k] = np.random.choice(NUM_CHROME, 2, replace=False)
        if p_fit[j] > p_fit[k]:
            a.append(p[j].copy())
        else:
            a.append(p[k].copy())
    return a


def crossover_uniform(p):  # 均勻交配
    a = []
    for _ in range(NUM_CROSSOVER):
        mask = np.random.randint(2, size=NUM_BIT)
        [j, k] = np.random.choice(NUM_PARENT, 2, replace=False)
        child1, child2 = p[j].copy(), p[k].copy()
        remain1, remain2 = list(p[j].copy()), list(p[k].copy())
        for m in range(NUM_BIT):
            if mask[m] == 1:
                remain2.remove(child1[m])
                remain1.remove(child2[m])
        t = 0
        for m in range(NUM_BIT):
            if mask[m] == 0:
                child1[m] = remain2[t]
                child2[m] = remain1[t]
                t += 1
        a.append(child1)
        a.append(child2)
    return a


def mutation(p):  # 突變
    for _ in range(NUM_MUTATION):
        row = np.random.randint(NUM_CROSSOVER_2)
        [j, k] = np.random.choice(NUM_BIT, 2, replace=False)
        p[row][j], p[row][k] = p[row][k], p[row][j]


def sortChrome(a, a_fit):  # 根據適應度排序
    a_index = range(len(a))
    a_fit, a_index = zip(*sorted(zip(a_fit, a_index), reverse=True))
    return [a[i] for i in a_index], list(a_fit)


def replace(p, p_fit, a, a_fit):  # 適者生存
    b = np.concatenate((p, a), axis=0)
    b_fit = p_fit + a_fit
    b, b_fit = sortChrome(b, b_fit)
    return b[:NUM_CHROME], list(b_fit[:NUM_CHROME])


# ==== 主程式 ====
pop = initPop()
pop_fit = evaluatePop(pop)

best_outputs = [np.max(pop_fit)]
mean_outputs = [np.average(pop_fit)]


best_permutation = []
best_makespan = 1e10

outer_loop = 0

with open('best_makespan.txt', 'r') as f:
    # get the number from the file
    best_makespan = int(f.read()) 

while(True):
    outer_loop += 1

    iter_num = NUM_ITERATION

    if outer_loop > 1:
        iter_num = 1000

    for i in range(iter_num):
        parent = selection(pop, pop_fit)
        offspring = crossover_uniform(parent)
        mutation(offspring)
        offspring_fit = evaluatePop(offspring)
        pop, pop_fit = replace(pop, pop_fit, offspring, offspring_fit)
        # 將最佳染色體的工件編號從 0-based 轉為 1-based
        best_permutation = [job + 1 for job in pop[0]]
        best_outputs.append(np.max(pop_fit))
        mean_outputs.append(np.average(pop_fit))
        
        
        print(f'o: {outer_loop} iteration {i}: makespan = {-pop_fit[0]}, permutation = {pop[0]}')

        if -pop_fit[0] < best_makespan:
            best_makespan = -pop_fit[0]
            best_permutation = pop[0]

            with open('best_permutation.txt', 'w') as f:
                f.write(' '.join(map(str, best_permutation)))
            with open('best_makespan.txt', 'w') as f:
                f.write(str(best_makespan))

    # add random pop into the population

    new_random_pop = initPop()

    mid = int(NUM_CHROME / 2)
    pop = pop[:mid] + new_random_pop[:NUM_CHROME - mid]



# 畫圖
plt.plot(best_outputs, label='Best Fitness')
plt.plot(mean_outputs, label='Average Fitness')
plt.xlabel("Iteration")
plt.ylabel("Fitness (-Makespan)")
plt.legend()
plt.savefig('job_shop_fitness_plot.png')
