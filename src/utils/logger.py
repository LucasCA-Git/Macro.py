from datetime import datetime
import os

LOG_FILE = os.path.join("logs", "automation.log")

def log_message(message):
    """Loga mensagens no arquivo automation.log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{timestamp} - {message}\n")
