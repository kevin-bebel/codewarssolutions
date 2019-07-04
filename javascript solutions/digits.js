function digPow(n, p) {
    //Split to digits
    let digits = n.toString().split('');
    digits = digits.map((x) => parseInt(x));

    let multi = digits.reduce((sum, digit, idx) => {
        return sum += Math.pow(digit, (p + idx))
    }, 0)

    let k = Math.floor(multi / n);

    if (k * n === multi ) {
        return k
    } else {
        return -1
    }

}