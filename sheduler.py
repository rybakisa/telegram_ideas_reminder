import sched, time

s = sched.scheduler(time.time, time.sleep)

def run_job():
    print("From print_time", time.time())
    s.enter(10, 1, run_job)

def run():
    s.enter(1, 1, run_job)
    s.run()

run()