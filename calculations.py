def get_pte_from_va(address):
    address >>= 9
    address &= 0x7FFFFFFFF8
    address += 0x0FFFFF68000000000
    return address


def get_pde_from_va(address):
    address >>= 18
    address &= 0x3FFFFFF8
    address += 0xFFFFF6FB40000000
    return address


def get_ppe_from_va(address):
    address >>= 27
    address &= 0x1FFFF8
    address += 0xFFFFF6FB7DA00000
    return address


def get_pxe_from_va(address):
    address >>= 36
    address &= 0xFF8
    address += 0xFFFFF6FB7DBED000
    return address
