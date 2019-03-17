import os
import time
import pandas as pd


def time_stamp_to_date(timestamp):
    time_struct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d',time_struct)


def get_file_modify_time(data_path, save__file_path):
    ids, rets = os.listdir(data_path), []
    for patient_id in ids:
        patient_path = os.path.join(data_path, patient_id)
        slice_ids = os.listdir(patient_path)
        modify_time = os.path.getmtime(os.path.join(patient_path, slice_ids[0]))
        print(patient_id, time_stamp_to_date(modify_time))
        if time_stamp_to_date(modify_time) == '2019-01-09':
            rets.append(0)
        elif time_stamp_to_date(modify_time) == '2019-01-10':
            rets.append(1)
        else:
            print('wrong date: {0}'.format(patient_id))
    print(len(ids), len(rets))

    # make submission
    df_submit = pd.DataFrame({'id': ids, 'ret': rets})
    df_submit.to_csv(save__file_path, index=False)


if __name__ == '__main__':
    get_file_modify_time('/test_dataset', 'submit.csv')

