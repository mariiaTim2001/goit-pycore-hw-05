def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "❌ Contact not found. Enter a valid name."
        except ValueError:
            return "❌ Give me name and phone please."
        except IndexError:
            return "❌ Not enough arguments. Please provide all required info."
    return inner
