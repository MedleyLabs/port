import sys
sys.path.insert(0, '/home/eric/port/src')  # TODO REMOVE

from port import initialize_app

app = initialize_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
