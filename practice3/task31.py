import struct


def f31(binary):
    def struct_a(offset):
        [a1] = struct.unpack('< B', binary[offset: offset + 1])
        offset += 1
        [a2] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        [a3] = struct.unpack('< b', binary[offset: offset + 1])
        offset += 1
        [a4] = struct.unpack('< b', binary[offset: offset + 1])
        offset += 1
        size, offset = struct.unpack('> H I', binary[offset:offset + 6])
        a5 = [struct_e(offset + i * (8 + 3 + 1 + 4)) for i in range(size)]
        offset += 6
        return {
        'A1': a1,
        'A2': struct_b(a2),
        'A3': a3,
        'A4': a4,
        'A5': a5,
        }
    def struct_b(offset):
        [b1] = struct.unpack('< b', binary[offset: offset + 1])
        offset += 1
        [b2] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        [b3] = struct.unpack('> h', binary[offset: offset + 2])
        offset += 2
        [b4] = struct.unpack('< b', binary[offset: offset + 1])
        offset += 1
        return {
        'B1': b1,
        'B2': struct_c(b2),
        'B3': b3,
        'B4': b4,
        }
    def struct_c(offset):
        [c1] = struct.unpack('> d', binary[offset: offset + 8])
        offset += 8
        size = 6
        c2 = ''.join([chr(i) for i in binary[offset: offset + size]])
        offset += 6
        [c3] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        c4 = struct_d(offset)
        offset += 4 + 1 + 2 + 1
        [c5] = struct.unpack('> h', binary[offset: offset + 2])
        offset += 2
        return {
        'C1': c1,
        'C2': c2,
        'C3': c3,
        'C4': c4,
        'C5': c5,
        }
    def struct_d(offset):
        size, address = struct.unpack('> H H', binary[offset:offset + 4])
        d1 = list(struct.unpack('>' + str(size) + 'H', binary[address:address + 2 * size]))
        offset += 4
        [d2] = struct.unpack('< B', binary[offset: offset + 1])
        offset += 1
        [d3] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        [d4] = struct.unpack('< B', binary[offset: offset + 1])
        offset += 1
        return {
        'D1': d1,
        'D2': d2,
        'D3': d3,
        'D4': d4,
        }
    def struct_e(offset):
        size, address = struct.unpack('> I I', binary[offset:offset + 8])
        e1 = list(struct.unpack('>' + str(size) + 'q', binary[address:address + 8 * size]))
        offset += 8
        e2 = list(struct.unpack('< 3B', binary[offset:offset + 3]))
        offset += 3
        [e3] = struct.unpack('< b', binary[offset: offset + 1])
        offset += 1
        [e4] = struct.unpack('> i', binary[offset: offset + 4])
        offset += 4
        return {
        'E1': e1,
        'E2': e2,
        'E3': e3,
        'E4': e4
        }
    return struct_a(4)

