# Entry point of the Flask application
# Import the create_app() function and starts the server

from app import create_app

app = create_app()

if __name__ == "__main__":
    # Run the API on port 5000 and make it accessible from outside the container
    app.run(host="0.0.0.0", port=5000, debug=True)
