
var expect = function (val) {
    return {
        toBe: function (val1) {
            if (val1 !== val) {

                throw new Error("Not Equal")
            }
            return true
        },
        notToBe: function (val2) {
            if (val2 === val) {

                throw new Error("Equal")
            }
            return true
        }
    }

};


console.log(expect(5).toBe(5));
console.log(expect(5).notToBe(5));
