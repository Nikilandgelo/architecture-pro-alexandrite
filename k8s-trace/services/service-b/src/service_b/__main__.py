from uvicorn import run


if __name__ == '__main__':
    run("service_b.app:app", host="0.0.0.0", port=9001)
