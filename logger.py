import time
import psutil
import math
import datetime

from util.json_manager import setup_json, read_json, write_json

def logger():
    avg_cpu_per = []
    abg_cpu_clock = []
    avg_memory = []
    data = read_json()
    print(f'cpu core: {psutil.cpu_count()}core \t disk: {round(psutil.disk_usage("/").total/1024**3, 2)}GB')
    print('\n'+'\n'+'\n')
    print('\033[32m'+'logger start...'+'\033[0m')
    start = time.time()
    while data['status'] != 'done':
        data = read_json()
        cpu_per = psutil.cpu_percent()
        avg_cpu_per.append(cpu_per)
        cpu_clock = psutil.cpu_freq().current
        abg_cpu_clock.append(cpu_clock)
        memory = psutil.virtual_memory().percent
        avg_memory.append(memory)

        now = datetime.datetime.now()
        print(data,'\t')
        print(f'now: {now.hour}:{now.minute}:{now.second} \t elapsed time', math.floor(time.time()-start), 'sec \t')
        print(f'cpu: {cpu_per}% \t cpu_clock: {cpu_clock}MHz \t memory: {memory}% \t'+ "\033[3A")
        time.sleep(1)

    print('\n'+'\n'+'\n')
    print(f'average cpu: {round(sum(avg_cpu_per)/len(avg_cpu_per), 2)}% \t average cpu clock: {round(sum(abg_cpu_clock)/len(abg_cpu_clock), 2)} \t average memory: {round(sum(avg_memory)/len(avg_memory), 2)}')