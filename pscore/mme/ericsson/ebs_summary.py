import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

ebs_file = 'mmee2b.csv'
ebs_load = pd.read_csv(ebs_file)[['event_id', 'event_result', 'apn', 'cause_code', 'imsi', 'sub_cause_code']]
ebs_load = ebs_load[ebs_load['event_id'] != 'event_id']

ebs_load_success = ebs_load[ebs_load['event_result'] == "success"]
ebs_load_fail = ebs_load[ebs_load['event_result'] != "success"]

mmee2b_ebs[mmee2b_ebs['event_id']=='activate'].groupby('sub_cause_code').count().sort_values(by=['event_id'], ascending=False)['event_id']
