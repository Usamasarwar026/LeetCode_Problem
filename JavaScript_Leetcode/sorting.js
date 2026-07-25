
let array = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]

function ascending(arr){
    let len = arr.length;
    for (let i = 0; i < len-1; i++) {
        for (let j = 0; j < len-i-1; j++) {
            if(arr[j] > arr[j+1]){
                let temp = arr[j];
                arr[j] = arr[j+1]
                arr[j+1] = temp
            }
        }
        
    }
    return arr
}

console.log("sorting array", ascending(array))