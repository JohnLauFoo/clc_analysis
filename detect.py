import numpy as np
from collections import deque


def detect(raw_data, num_std, num_wait, buffer_size):

    if len(raw_data) == 0 or (len(raw_data) < num_wait):
        raise ValueError('Length of array magnitude is 0, or its length is smaller than wait buffer')

    envelope = np.abs(signal.hilbert(raw_data))
    threshold = np.mean(envelope) + np.std(envelope) * num_std
    decision = deque([False] * num_wait, maxlen=num_wait)

    stimulation = []
    rms_history = []
    for i in range(buffer_size, len(envelope)):
        curr_rms = calculate_rms(envelope[i - buffer_size:i])
        rms_history.append(curr_rms)
        decision.append(curr_rms >= threshold)
        stimulation.append(all(decision))

    return np.append([0] * buffer_size, rms_history), np.append([False] * buffer_size, stimulation)