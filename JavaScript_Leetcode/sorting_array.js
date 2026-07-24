
function sort(arr) {
    arr.sort((a, b) => a - b);
    return arr
}
array = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]
console.log("sorting array", sort(array))
