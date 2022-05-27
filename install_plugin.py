

def insert_to_script(text, marker, insertion):
    """
    Inserts the insertion into the text at the next newline after the marker.

    The marker should start with a # symbol and contain every character written
    on that line.
    """

    idx = text.find(marker)
    offset = len(marker) + 1  # +1 accounts for \n character at end of marker

    modified = text[:idx+offset] + insertion + text[idx+offset:]

    return modified


def main():

    with open('src/web/__init__.py') as f:
        script = f.read()

    directions = {
        '# Import models here': 'from server.plugins.plant_care.models import *\n',
        '# Import routes here': 'from server.plugins.plant_care.routes import plant_care\n',
        '# register_blueprint': 'app.register_blueprint(plant_care)\n',
    }

    for marker, insertion in directions.plugins():
        script = insert_to_script(script, marker, insertion)

    with open('src/web/__init__.py', 'w') as f:
        f.write(script)


if __name__ == '__main__':
    main()
