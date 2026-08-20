"""Minimal example for SchemaDiff."""

from schemadiff import schemadiff


def main():
 runner = schemadiff({"name": "SchemaDiff", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()