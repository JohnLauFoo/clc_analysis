import numpy as np


def extract_events(stimulation, timestamps):
    if len(stimulation) != len(timestamps):
        raise ValueError('stimulation array and timestamps array must have the same length')

    changedstatus = np.append(False, np.abs(np.diff(stimulation)))
    changedidx = np.where(changedstatus)[0]
    changedtime = np.array(timestamps)[changedstatus]
    if len(changedtime) % 2: changedtime = np.delete(changedtime, [-1])

    return np.array([Event(a, b, c, d, e) for a, b, c, d, e in zip(changedidx[::2],
                                                                   changedidx[1::2],
                                                                   changedtime[::2],
                                                                   changedtime[1::2],
                                                                   1000 * np.diff(changedtime)[::2])])