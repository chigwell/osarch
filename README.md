[![PyPI version](https://badge.fury.io/py/osarch.svg)](https://badge.fury.io/py/osarch)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/osarch)](https://pepy.tech/project/osarch)

# OSArch

`OSArch` is a lightweight Python package designed to detect the operating system (OS) and architecture of the system running your Python code. It simplifies accessing system details with minimal code.

## Installation

To install `OSArch`, use pip:

```bash
pip install osarch
```

## Usage

`OSArch` is easy to use. Here's a quick start guide:

```python
from osarch import detect_system_architecture

# Get OS and architecture
os_name, architecture = detect_system_architecture()
print(f"OS: {os_name}, Architecture: {architecture}")
```

This code snippet will print the OS and architecture of your system, e.g., "OS: linux, Architecture: 64".

## Features

- Easy detection of system OS and architecture.
- Simple API with minimal setup required.
- Useful for environment-specific operations in your code.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/osarch/issues).

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
