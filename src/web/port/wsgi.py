from port import initialize_app


app = initialize_app()


if __name__ == "__main__":

    host = '127.0.0.1'
    port = 5000
    debug = True
    threaded = True

    logger.info(f'Running Flask app at {host}:{port}...')

    app.run(host=host, port=port, debug=debug, threaded=threaded)
