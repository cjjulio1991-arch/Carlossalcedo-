import os
import time

class SystemTelemetry:
    """
    Real-time system telemetry engine.
    Parses /proc filesystem for functional metrics.
    """

    @staticmethod
    def get_cpu_usage():
        """Parses /proc/stat to calculate CPU usage."""
        try:
            with open('/proc/stat', 'r') as f:
                line = f.readline()
                parts = line.split()
                if len(parts) < 5: return (0.0, 0.0)
                idle = float(parts[4])
                total = sum(float(p) for p in parts[1:])
                return (idle, total)
        except Exception:
            return (0.0, 0.0)

    @staticmethod
    def calculate_cpu_percent(prev_idle, prev_total):
        curr_idle, curr_total = SystemTelemetry.get_cpu_usage()
        diff_idle = curr_idle - prev_idle
        diff_total = curr_total - prev_total
        if diff_total == 0: return 0.0
        return max(0.0, min(100.0, 100.0 * (1.0 - diff_idle / diff_total)))

    @staticmethod
    def get_memory_info():
        """Parses /proc/meminfo."""
        mem_info = {}
        try:
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    parts = line.split(':')
                    if len(parts) == 2:
                        name = parts[0].strip()
                        value = parts[1].split()[0].strip()
                        mem_info[name] = int(value) # in kB

            total = mem_info.get('MemTotal', 1)
            free = mem_info.get('MemFree', 0)
            buffers = mem_info.get('Buffers', 0)
            cached = mem_info.get('Cached', 0)
            used = total - free - buffers - cached
            return {
                "total_mb": round(total / 1024, 2),
                "used_mb": round(used / 1024, 2),
                "percent": round((used / total) * 100, 2)
            }
        except Exception:
            return {"total_mb": 0, "used_mb": 0, "percent": 0}

    @staticmethod
    def get_load_avg():
        """Parses /proc/loadavg."""
        try:
            with open('/proc/loadavg', 'r') as f:
                parts = f.readline().split()
                return [float(x) for x in parts[:3]]
        except Exception:
            return [0.0, 0.0, 0.0]

    @staticmethod
    def get_all_metrics(prev_cpu=None):
        cpu_p = 0.0
        if prev_cpu:
            cpu_p = SystemTelemetry.calculate_cpu_percent(prev_cpu[0], prev_cpu[1])

        curr_cpu = SystemTelemetry.get_cpu_usage()
        return {
            "cpu_percent": round(cpu_p, 2),
            "memory": SystemTelemetry.get_memory_info(),
            "load_avg": SystemTelemetry.get_load_avg(),
            "cpu_raw": curr_cpu
        }

telemetry = SystemTelemetry()
