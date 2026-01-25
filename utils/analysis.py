def analyze_sessions(sessions):
    if not sessions:
        return {}

    time_counts = {"morning": 0, "afternoon": 0, "evening": 0}
    energy_trend = []
    task_counts = {}
    energy_map = {"low": 1, "medium": 2, "high": 3}
    total_duration = 0

    for session in sessions:
        time_period = session[2]
        duration = int(session[3])
        energy = session[4]
        task = session[5]

        time_counts[time_period] += 1
        task_counts[task] = task_counts.get(task, 0) + 1
        energy_trend.append(energy_map.get(energy, 0))
        total_duration += duration

    session_count = len(sessions)
    average_duration = total_duration // session_count

    if session_count >= 10:
        consistency = "High"
    elif session_count >= 5:
        consistency = "Moderate"
    else:
        consistency = "Low"

    if total_duration >= 600:
        workload = "Heavy"
    elif total_duration >= 300:
        workload = "Moderate"
    else:
        workload = "Light"

    return {
        "time_distribution": time_counts,
        "task_distribution": task_counts,
        "energy_trend": energy_trend,
        "average_duration": average_duration,
        "consistency_level": consistency,
        "workload_level": workload
    }