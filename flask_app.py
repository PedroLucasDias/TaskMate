from app import create_app
app = create_app()

if __name__ == "__main__":
    app.run("192.168.2.105", 5555, True)
