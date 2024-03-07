from datetime import datetime

def salam_pembuka() -> None:
    jam_sekarang = datetime.now().hour
    if jam_sekarang < 11:
        return 'Selamat pagi!'
    elif jam_sekarang < 15:
        return 'Selamat siang!'
    elif jam_sekarang < 19:
        return 'Selamat sore!'
    else:
        return 'Selamat malam!'
