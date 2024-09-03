import click
from svgrepo_dl.engine.mainfunctions import *


@click.group
def cli():
    """"""
    pass






  
cli.add_command(save_col)

if __name__ == '__main__':

    cli()
