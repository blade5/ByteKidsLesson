import qrcode
img = qrcode.make('欢迎你啊 我是谁谁谁')
with open('test.png', 'wb') as f:
    img.save(f)
