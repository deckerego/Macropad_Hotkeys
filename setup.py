from setuptools import setup # type: ignore

setup(
    name="macropad-hotkeys",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="Use your Adafruit Macropad to setup hotkeys and macros for a number of applications",
    long_description="CircuitPython application that runs on the Adafruit Macropad for extensible macros and hotkeys",
    long_description_content_type="text/markdown",
    url="https://github.com/deckerego/Macropad_Hotkeys",
    author="DeckerEgo",
    author_email="john@deckerego.net",
    py_modules=[],
    install_requires=[],
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Human Interface Device (HID)",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="adafruit circuitpython micropython macropad hotkeys macros keyboard hid",
)