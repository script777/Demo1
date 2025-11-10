import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = None
        self.run_server()

    def run_server(self):
        if self.process:
            print("🔁 Reiniciando servidor...")
            self.process.kill()
            self.process.wait()
            time.sleep(0.5)
        else:
            print("🚀 Iniciando servidor...")
        self.process = subprocess.Popen(self.command, shell=True)

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            self.run_server()

if __name__ == "__main__":
    path = "."
    command = "python ./backend/server.py"
    event_handler = ReloadHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Deteniendo watcher...")
        if event_handler.process:
            event_handler.process.kill()
            event_handler.process.wait()
        observer.stop()
    observer.join()