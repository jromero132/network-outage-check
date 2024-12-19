# Network Outage Check

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?logo=buy-me-a-coffee&logoColor=black)](<https://buymeacoffee.com/jromero132> "Buy Me a Coffee - jromero132")
[![Made with Python](https://img.shields.io/badge/Python->=3.8-blue?logo=python&logoColor=white)](<https://python.org> "Go to Python homepage")

---

> [!NOTE]  
> This is a very simple and naive, yet effective way to check whether you have an internet connection or not. This
> project is only intended for personal use.

## Overview

A Python tool for monitoring network connectivity and detecting potential service outages using scheduled HTTP requests
to Google.

### Features

- Periodic network availability checks
- HTTP request-based connectivity testing
- Logging of network status

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/jromero132/network-outage-check.git
cd network-outage-check
pip install -r requirements.txt
```

### Dependencies

- requests (>=2.32.3, <2.33)
- schedule (>=1.2.2, <1.3)

### Running the Project

In order to run the project, just run the following command:

```bash
python main.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [license](license) file for details.

### Happy Coding! 🚀
