class Event:

    def __init__(self, start_idx, end_idx, start_timestamp, end_timestamp, event_duration):
        self.idx_range = [start_idx, end_idx]
        self.timestamp_range = [start_timestamp, end_timestamp]
        self.duration = event_duration