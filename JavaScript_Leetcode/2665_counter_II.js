/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {
    let val = init
    return {
        increment: function () {

            return ++val
        },
        decrement: function () {
            return --val
        },
        reset: function () {
            return val = init
        },
    }
};


const counter = createCounter(5)

console.log("increment", counter.increment());
console.log("reset", counter.reset());
console.log("increment", counter.increment());
console.log("decrement", counter.decrement());
