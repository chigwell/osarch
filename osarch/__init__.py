import platform


def detect_system_os():
    system_platform = platform.system().lower()
    return system_platform


def detect_architecture():
    arch = platform.machine()
    if arch in ['AMD64', 'x86_64']:
        arch = '64'
    else:
        arch = '32'
    return arch


def detect_system_architecture():
    return detect_system_os(), detect_architecture()

