from src.port import initialize_app


app = initialize_app()


if __name__ == "__main__":

    host = '127.0.0.1'
    port = 8000
    debug = True
    threaded = True

    app.run(host=host, port=port, debug=debug, threaded=threaded)
