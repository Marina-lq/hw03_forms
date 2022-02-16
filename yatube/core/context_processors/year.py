from datetime import datetime


def year():
    dt = datetime.now().year
    return {
        'year': dt
    }
