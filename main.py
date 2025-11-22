import click

@click.group()
def cli():
    """CLI for interacting with the desktop agent."""
    pass

@cli.command()
def chat():
    """Chat command."""
    click.echo("Chat command not implemented yet.")

@cli.command()
def account():
    """Account command."""
    click.echo("Account command not implemented yet.")

@cli.command()
def positions():
    """Positions command."""
    click.echo("Positions command not implemented yet.")

@cli.command()
def trade():
    """Trade command."""
    click.echo("Trade command not implemented yet.")

@cli.command()
def search():
    """Search command."""
    click.echo("Search command not implemented yet.")

if __name__ == '__main__':
    cli()