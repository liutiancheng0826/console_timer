import datetime
import time
import subprocess

def loop_print_time(times: int) -> None:
    if times == 0:
        return
    
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)
    subprocess.run('cls', shell=True)
    #subprocess.call('cls', shell=True)

    return loop_print_time(times-1)

if __name__ == "__main__":
    loop_print_time(10)