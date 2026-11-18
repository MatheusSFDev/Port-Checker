# 🔍 Port Checker (Concurrent TCP Port Scanner)

A high-performance Command-Line Interface (CLI) tool built in Python to scan and verify active TCP ports on a target host. Designed for rapid network diagnostics, infrastructure auditing, and service availability checks.

## 🚀 Features

* **Massive Concurrency:** Utilizes `concurrent.futures.ThreadPoolExecutor` with adjustable high-worker capacity (`max_workers=1000`) to scan thousands of ports simultaneously.
* **Full Range Scanning:** Capable of sweeping the entire TCP port spectrum (from `1` to `65535`) in mere seconds.
* **Optimized Socket Timeouts:** Configured with a tight response timeout (`0.5s`) to ensure quick identification of active services without hanging the execution.
* **Robust Exception Handling:** Gracefully handles network exceptions (`socket.timeout`, `ConnectionRefusedError`, and generic errors) ensuring stable execution.
* **Strict IP Validation:** Built-in IPv4 validation function checking proper octet boundaries (`0` to `255`) prior to executing network actions.
* **Interactive CLI Interface:** Clean, user-friendly terminal loop allowing continuous target testing.

## 🛠️ Technologies Used

* **Python 3.10+** (utilizes structural pattern matching `match/case`)
* Standard Libraries (zero external dependencies required):
  * `socket`
  * `concurrent.futures`
