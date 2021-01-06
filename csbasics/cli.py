from typing import List

import click
import typer

from csbasics.linkedlist import LinkedList

cli = typer.Typer()


@cli.command()
def echo(text: str) -> None:
    print(text)


@cli.command()
@click.argument("numbers", type=int, nargs=-1)
def linkedlist(numbers: List[int]) -> None:
    print(LinkedList([int(i) for i in numbers]))


if __name__ == "__main__":
    cli()
