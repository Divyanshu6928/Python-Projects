import qrcode as qr
image = qr.make("https://divyanshu-neon.vercel.app/")
image.save("portfolio.png")