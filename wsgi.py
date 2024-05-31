from app import app

def application(environ, start_response):
    return app(environ, start_response)

# Start the server
if __name__ == "__main__":
    from gunicorn import server as gunicorn_server
    gunicorn_server.run()
