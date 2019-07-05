//https://www.codewars.com/kata/a-string-of-sorts/javascript

function sortString(string, ordering) {
    let s = ""
    let chars = string.split("")

    for (var i = 0; i < ordering.length; i++) {
        const _c = chars.filter((item) => item === ordering[i])
        s = s + _c.join("")
        chars = chars.filter((item) => item !== ordering[i])
        //console.log(chars);
    }

    s = s + chars.join("");
    return s;
}

console.log(sortString("foos", "of"))
console.log(sortString("string", "gnirts"))
console.log(sortString("banana","abn"))