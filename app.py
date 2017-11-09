import click

from trippy.process import Processor

@click.command()
@click.argument('file', type=click.File('r'))
def main(file):
    """Processes a driver/trip input file and reports statistics on the drivers."""
    process = Processor()
    
    for line in file:
        process.process_line(line)
    
    print('\n'.join(process.get_report()))

if __name__ == '__main__':
    main()
