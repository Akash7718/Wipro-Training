import threading, time

def task(name):
    print(f"{name} starting")
    time.sleep(2)
    print(f"{name} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=task, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed")