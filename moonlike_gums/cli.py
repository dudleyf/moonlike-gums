import click
from moonlike_gums.words import haikunate


@click.command()
def project_name():
    click.echo(haikunate())


if __name__ == "__main__":
    project_name()
