def analyze_sessions(sessions):
    if not sessions:
        return {}

    time_counts = {}
    energy_counts = {}
    task_counts = {}
    total_duration = 0

    for session in sessions:
        time_period = session[2]
        duration = int(session[3])
        energy = session[4]
        task = session[5]

        time_counts[time_period] = time_counts.get(time_period, 0) + 1
        energy_counts[energy] = energy_counts.get(energy, 0) + 1
        task_counts[task] = task_counts.get(task, 0) + 1
        total_duration += duration

    return {
        "most_productive_time": max(time_counts, key=time_counts.get),
        "most_common_energy": max(energy_counts, key=energy_counts.get),
        "most_common_task": max(task_counts, key=task_counts.get),
        "average_duration": total_duration // len(sessions)
    }