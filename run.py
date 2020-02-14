""" This selects the __init__.py file from the folder App """
from App import app
""" If the package is run from Python terminal, then it opens in debug mode """
if __name__ == '__main__':
    app.run(debug=True)