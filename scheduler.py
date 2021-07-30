import sched, time

class Scheduler:
    def __init__(self, function_to_run, delay):
        self.s = sched.scheduler(time.time, time.sleep)
        self.function_to_run = function_to_run
        self.delay = delay

    def run_job(self):
        self.function_to_run()
        self.s.enter(self.delay, 1, self.run_job)

    def run(self):
        self.s.enter(1, 1, self.run_job)
        self.s.run()
