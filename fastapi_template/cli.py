import shutil
from pathlib import Path
import click

TEMPLATE_DIR = Path(__file__).parent / "template"

@click.command()
@click.argument("project_name")
def main(project_name):
    """Create a new FastAPI project from the template."""
    dest = Path.cwd() / project_name
    if dest.exists():
        click.echo(f"Error: Directory '{project_name}' already exists.")
        return
    shutil.copytree(TEMPLATE_DIR, dest)
    click.echo(f"Created new FastAPI project at {dest}")
    click.echo(f"Next steps:")
    click .echo(f"  cd {project_name}")
    click.echo(f"  pip install -r requirements.txt (if present)")
    click.echo(f"  uvicorn app.main:app --reload")

if __name__ == "__main__":
    main()
