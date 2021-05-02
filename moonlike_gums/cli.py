import click
from moonlike_gums.gen import project_name


@click.command()
def gen_project_name():
    click.echo(project_name())


if __name__ == "__main__":
    gen_project_name()
