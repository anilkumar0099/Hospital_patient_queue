# 🏥 Hospital Patient Queue Manager

A Python project to simulate a hospital's patient queue system with **emergency** and **regular** cases.  
This project demonstrates the use of **Priority Queue** (for emergencies) and **FIFO Queue** (for regular patients), along with estimated wait times.

---

## 🚀 Features
- ✅ Emergency patients handled with **Priority Queue** (severity level)  
- ✅ Regular patients handled with **FIFO Queue**  
- ✅ Estimated wait time calculation (default 10 minutes per patient)  
- ✅ Processes patients in correct order (emergency → regular)  
- ✅ Simple and easy to extend  

## 🛠️ Tech Requirements
- **Priority Queue (heapq)** → For emergency patients, based on severity.  
- **Normal Queue (deque)** → For regular patients in order of arrival.  
- **Timestamps/Order counter** → To ensure correct handling order.  

## 📖 How It Works
1. Add patients as either **regular** or **emergency** (with severity level `1–5`).  
   - Lower severity number = higher priority.  
2. System estimates wait times based on position in queue.  
3. Patients are processed in this order:
   - Emergency patients (sorted by severity, then arrival order)  
   - Regular patients (FIFO order)  

## ▶️ Example Usage
Run the script:
```bash
python hospital_queue.py

## Example Output:

🧑‍⚕️ Regular patient added: anil
🚨 Emergency patient added: Bharath (Severity 2)
🚨 Emergency patient added: Gowtham (Severity 1)
🧑‍⚕️ Regular patient added: David

Wait time for Alice: 20 minutes
Wait time for Bob: 10 minutes

🚨 Treating emergency patient: Gowtham (Severity 1)
🚨 Treating emergency patient: Bharath (Severity 2)
🧑‍⚕️ Treating regular patient: anil
🧑‍⚕️ Treating regular patient: David
✅ No patients waiting.

