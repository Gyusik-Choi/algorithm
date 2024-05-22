const bisectRight = (low, high) => {
    while (low < high) {
        mid = Math.floor((low + high) / 2);

        if (numbers[mid] <= mid) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }

    return low;
}


const bisectLeft = (low, high) => {
    while (low < high) {
        mid = Math.floor((low + high) / 2);

        if (numbers[mid] < mid) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }

    return low;
}

// https://github.com/python/cpython/blob/3.11/Lib/bisect.py
// bisectLeft 와 bisectRight 의 차이는
// mid 인덱스에 해당하는 배열의 값과 찾으려는 값이
// 같을 경우 처리하는 방식이 다르다
//
// bisectLeft 의 경우 
// 같을때 low 를 mid + 1 로 올리지 않고
// high 를 mid 로 내린다
//
// bisectRight 의 경우
// 같을 경우 high 를 mid 로 내리지 않고
// low 를 mid + 1 로 올린다

const binarySearch = (low, high) => {
    while (low < high) {
        mid = Math.floor((low + high) / 2);

        if (numbers[mid] < mid) {
            low = mid + 1
        } else {
            high = mid;
        }
    }

    return low;
}

const N = 7;
const numbers = [-15, -4, 2, 8, 9, 13, 15];
const idx1 = binarySearch(0, N);
const idx2 = bisectLeft(0, N);
const idx3 = bisectRight(0, N) - 1;
console.log(idx1);
console.log(idx2);
console.log(idx3);
