from waitress import serve
from SupabaseAuth import app

if __name__ == '__main__':

    serve(app, port='8010')