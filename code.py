def multiply(a, b):
    result = None

    try:
        result = a * b
    except Exception as e:
        print(e)
        result = None

    return result
