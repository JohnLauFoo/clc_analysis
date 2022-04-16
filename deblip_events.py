import numpy as np


def deblip_helper(event_processed, events, win_size):
    if len(events) == 0:
        return event_processed

    else:
        del_idx = []
        curr_onset = events[0].timestamp_range[0]
        for i in range(0, len(events)):
            if (events[i].timestamp_range[0] - curr_onset) * 1000 <= win_size:
                del_idx.append(i)
            else:
                break

        return deblip_helper(np.append(event_processed, events[0]), np.delete(events, del_idx), win_size)


def deblip_events(events, win_size): return deblip_helper(np.array([]), events, win_size)