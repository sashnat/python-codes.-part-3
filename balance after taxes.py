def out(x, y, z):
    print ('налог $:', z/100 * x/y)
    return x/y - z/100 * x/y

print ('останется: $', out(float(input('введите сумму: ')), float(input('введите курс: ')), float(input('введите налог: ' ))))
