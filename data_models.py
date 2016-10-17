import re
import datetime

class mid_day_form:

class end_day_form:

class fallvignetten:

class pretest:

class posttest:

class sample_day:


class participant(id, start_ts, stop_ts, mid_fv, findm_pre_pid, findm_pre_k, handy_id, mid_daily, handynr, findm_post_pid_findm_post_k):

    def __init__(self, id, start_ts, stop_ts, mid_fv, findm_pre_pid, findm_pre_k, handy_id, mid_daily, handynr, findm_post_pid_findm_post_k):

        if re.match(r'[A-Z]{4,4}\d\d', id, flags=0) is not None:
            self.id = id
            self.start_ts = start_ts
            self.stop_ts = stop_ts

            self.days = []

            self.pretest = pretest

            self.posttest = posttest


        else:
            print("ERROR: incorrect ID!")

    def __