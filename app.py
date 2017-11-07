import click

@click.command()
@click.argument('file', type=click.File('r'))
def main(file):
    """Processes a driver/trip input file and reports statistics on the drivers."""
    print(file.readlines())

if __name__ == '__main__':
    main()
