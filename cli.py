import subprocess

import click


@click.group()
def root():
    pass


@root.command()
def test():
    subprocess.run(["pytest"])


@root.command()
def coverage():
    subprocess.run(["coverage", "run", "-m", "pytest"])
    subprocess.run(["coverage", "report"])

@root.command()
def docs():
    subprocess.run(["pdoc", "game"])


if __name__ == "__main__":
    root()
