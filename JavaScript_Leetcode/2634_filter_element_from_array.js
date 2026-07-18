/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
    const array = []
    for (let i = 0; i < arr.length; i++) {
        const filteredArr = fn(arr[i], i)
        if (filteredArr) {
            array.push(arr[i])
        }
    }
    return array

};