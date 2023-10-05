def generate(env):
    py_name = "python" if env["PLATFORM"] == "win32" else "python3"
    env.SetDefault(
        PYTHON3=py_name,
    )


def exists(env):
    return True
