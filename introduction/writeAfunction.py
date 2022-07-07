
def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

year = int(input("Masukkan Tahun: "))
if is_leap(year) == True:
    print(str(year) + " Tahun Kabisat")
else:
    print(str(year) + " Bukan Tahun Kabisat")
