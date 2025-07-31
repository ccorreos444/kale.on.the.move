from flask import Flask, render_template

# Initialize the Flask app.
# 'template_folder' and 'static_folder' tell Flask where to find your HTML templates and static assets.
app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    """
    Renders the main home page of the itinerary generator.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask development server.
    # debug=True enables debug mode, which provides helpful error messages
    # and automatically reloads the server on code changes.
    app.run(debug=True)