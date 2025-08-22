import heapq
from collections import deque
from datetime import datetime

class HospitalQueue:
    def __init__(self, avg_consult_time=10):
        self.emergency_queue = []   # Min-heap: (severity, arrival_time, patient_name)
        self.regular_queue = deque()
        self.avg_consult_time = avg_consult_time
        self.arrival_counter = 0  # To keep track of arrival order

    def add_patient(self, name, is_emergency=False, severity=5):
        self.arrival_counter += 1
        if is_emergency:
            heapq.heappush(self.emergency_queue, (severity, self.arrival_counter, name))
            print(f"🚨 Emergency patient added: {name} (Severity {severity})")
        else:
            self.regular_queue.append((self.arrival_counter, name))
            print(f"🧑‍⚕️ Regular patient added: {name}")

    def next_patient(self):
        if self.emergency_queue:
            severity, _, name = heapq.heappop(self.emergency_queue)
            return f"🚨 Treating emergency patient: {name} (Severity {severity})"
        elif self.regular_queue:
            _, name = self.regular_queue.popleft()
            return f"🧑‍⚕️ Treating regular patient: {name}"
        else:
            return "✅ No patients waiting."

    def estimated_wait_time(self, name):
        # Check in emergency queue
        for idx, (_, _, n) in enumerate(self.emergency_queue):
            if n == name:
                return idx * self.avg_consult_time

        # Check in regular queue (after all emergencies are done)
        for idx, (_, n) in enumerate(self.regular_queue):
            if n == name:
                return (len(self.emergency_queue) + idx) * self.avg_consult_time

        return None


# Example usage
if __name__ == "__main__":
    hospital = HospitalQueue()

    # Add patients
    hospital.add_patient("anil")  # regular
    hospital.add_patient("bharath", is_emergency=True, severity=2)
    hospital.add_patient("gowtham", is_emergency=True, severity=1)
    hospital.add_patient("David")

    # Estimate wait time
    print("Wait time for anil:", hospital.estimated_wait_time("anil"), "minutes")
    print("Wait time for Bharath:", hospital.estimated_wait_time("Bharath"), "minutes")

    # Treat patients
    print(hospital.next_patient())
    print(hospital.next_patient())
    print(hospital.next_patient())
    print(hospital.next_patient())
    print(hospital.next_patient())
