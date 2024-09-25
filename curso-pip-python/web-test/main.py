import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return store.get_categories()

@app.get("/html", response_class=HTMLResponse)
def get_html():
    return """ 
    <html>
        <head>
            <title>Web Test</title>
        </head>
        <body>
            <h1>Web Test</h1>
            <ul>
                <li>Category 1</li>
                <li>Category 2</li>
                <li>Category 3</li>
            </ul>
        </body>
    </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()