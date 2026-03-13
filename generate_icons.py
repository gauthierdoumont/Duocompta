import struct, zlib, os

def create_png(size, r, g, b):
    def chunk(t, d):
        c = t + d
        return struct.pack('>I', len(d)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)
    rows = b''
    for y in range(size):
        row = b'\x00'
        for x in range(size):
            dx = x - size/2
            dy = y - size/2
            dist = (dx*dx + dy*dy) ** 0.5
            if dist <= size/2 - 2:
                row += bytes([r, g, b])
            else:
                row += bytes([14, 15, 20])
        rows += row
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0))
    idat = chunk(b'IDAT', zlib.compress(rows))
    iend = chunk(b'IEND', b'')
    return b'\x89PNG\r\n\x1a\n' + ihdr + idat + iend

sizes = {'hdpi': 72, 'mdpi': 48, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}
for density, size in sizes.items():
    png = create_png(size, 212, 175, 55)
    base = f'app/src/main/res/mipmap-{density}'
    os.makedirs(base, exist_ok=True)
    for name in ['ic_launcher.png', 'ic_launcher_round.png']:
        with open(f'{base}/{name}', 'wb') as f:
            f.write(png)
    print(f'Icon {density} ({size}px) OK')
