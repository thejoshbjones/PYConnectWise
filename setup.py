from distutils.core import setup

setup(
    name="PyWise",  # How you named your package folder (MyLib)
    packages=["PyWise"],  # Chose the same as "name"
    version="0.1",  # Start with a small number and increase it with every change you make
    license="GPLv3",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="Python client for simple, typesafe interactions with the ConnectWise APIs",  # Give a short description about your library
    author="Health IT",  # Type in your name
    author_email="dev@healthit.com.au",  # Type in your E-Mail
    url="https://github.com/HealthITAU/pywise",  # Provide either the link to your github or to your website
    download_url="https://github.com/HealthITAU/pywise/archive/refs/tags/v0.1.tar.gz",  # I explain this later on
    keywords=[
        "Python",
        "API",
        "ConnectWise",
        "Manage",
        "Automate",
        "Typed",
    ],  # Keywords that define your package best
    install_requires=["pydantic", "requests", "jinja2"],  # I get to this in a second
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",  # Again, pick a license
        "Programming Language :: Python :: 3.10",  # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.11",
    ],
)
