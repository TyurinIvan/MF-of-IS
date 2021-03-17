import math

c_flag1 = 258166178649724503599487742934802526287669691117141193813325965154020153722514921601647187648221919500612597559946901707669147251080002815987547531468665467566717005154808254718275802205355468913739057891997227
N1 = 770208589881542620069464504676753940863383387375206105769618980879024439269509554947844785478530186900134626128158103023729084548188699148790609927825292033592633940440572111772824335381678715673885064259498347

c_flag2 = 82342298625679176036356883676775402119977430710726682485896193234656155980362739001985197966750770180888029807855818454089816725548543443170829318551678199285146042967925331334056196451472012024481821115035402
N2 = 106029085775257663206752546375038215862082305275547745288123714455124823687650121623933685907396184977471397594827179834728616028018749658416501123200018793097004318016219287128691152925005220998650615458757301

c_flag3 = 22930648200320670438709812150490964905599922007583385162042233495430878700029124482085825428033535726942144974904739350649202042807155611342972937745074828452371571955451553963306102347454278380033279926425450
N3 = 982308372262755389818559610780064346354778261071556063666893379698883592369924570665565343844555904810263378627630061263713965527697379617881447335759744375543004650980257156437858044538492769168139674955430611


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def find_invpow(x, n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high / 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid ** n < x:
            low = mid
        elif high > mid and mid ** n > x:
            high = mid
        else:
            return mid
    return mid + 1


flag_cubed = chinese_remainder([N1, N2, N3], [c_flag1, c_flag2, c_flag3])
flag = find_invpow(flag_cubed, 3)

print
hex(flag)[2: -1].decode("hex")