import qrcode

# 实例化QRCode生成qr对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
# 传入数据
data = 'http://www.baidu.com/'
qr.add_data(data)

# 生成二维码
img = qr.make_image()

# 保存二维码
img_file = r'保存路径'
img.save(img_file)
# 展示二维码
img.show()

