import click
from os.path                 import expanduser
from svgrepo_dl.engine.utils import true_exists_collection_url 
from svgrepo_dl.toolkit      import Color as cl

def no_arguments_msg(verbose:bool) -> None:
    cl.p(cl.BOLD, cl.Y, "NOTE:", "You didn't provide any url.")
    if verbose:
        cl.p(
            cl.BOLD, "   |Example:\n      ",
            cl.G, cl.BOLD, "svgrepo_dl",
            cl.BOLD, "save-col",
            "https://www.svgrepo.com/collection/colored-svg-logos/",
        )


def no_collection_found_msg() -> None:
    cl.p(cl.BOLD, cl.R, "ERROR:", "Check the arguments above.")




@click.command(help="will install all the collections you want.")
@click.argument('collections', nargs=-1,)
@click.option('--verbose', is_flag=True, help="Enable verbose output.")
@click.option(
    '-o', '--path-folder', 
    default=expanduser("~")+"/Pictures/",  # Set a default path
    show_default=True,  # Show the default value in the help message
    type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True),
    help="Specify the output folder path (must exist)."
)

def save_col(collections:list[str], verbose:bool, path_folder:str) -> None:
    print(path_folder)
    if not collections:
        no_arguments_msg(verbose)
        return None
        
    collections = true_exists_collection_url(collections, verbose)
    if not collections:
        no_collection_found_msg()
        return None

        
        
    

