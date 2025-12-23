# bfchar + bfrange (пример для F4/F8)
bfchar = {
    0x0003: ' ', 0x0014: '1', 0x0018: '5', 0x001D: ':', 0x0027: 'D',
    0x002F: 'L', 0x0036: 'S', 0x0038: 'U', 0x003B: 'X', 0x0042: '_',
    0x0059: 'v', 0x005B: 'x', 0x005D: 'z'
}
bfrange = [
    (0x0011, 0x0012, 0x002E), (0x001A, 0x001B, 0x0037), (0x0024, 0x0025, 0x0041),
    (0x0033, 0x0034, 0x0050), (0x0044, 0x004C, 0x0061), (0x004F, 0x0050, 0x006C),
    (0x0052, 0x0057, 0x006F)
]

def decode_code(code):
    if code in bfchar:
        return bfchar[code]
    for start, end, target in bfrange:
        if start <= code <= end:
            return chr(target + (code - start))
    return '?'

# Список полезных hex‑строк
hex_streams = [
    "004B0057005700530056001D0012001200470055004C005900480011004A00520052004A004F0048001100460052005000120049004C004F0048001200470012001400480054002F001A0055003B0046005B003600180057004A004500420044001B001A004C001B002400380033",
    "002500530027001B0046002F005D004C00540034",
    "02490263025D025C026B0276027102600261",
    "02700258025B",
    "003D002C0033",
    "003D002C0033",
    "003D002C003300040004"
]

decoded_text = ""
for hs in hex_streams:
    codes = [int(hs[i:i+4],16) for i in range(0,len(hs),4)]
    decoded_text += ''.join(decode_code(c) for c in codes)

print(decoded_text)
