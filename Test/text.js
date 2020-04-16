// const calcNumber = (n) => (f) => (num) => f(n, num);

// const clacwith2 = calcNumber(2);
// const clacwith3 = calcNumber(3);

// const add = (num1, num2) => num1 + num2;
// const mul = (num1, num2) => num1 * num2;

// const add2 = clacwith2(add);
// const add3 = clacwith3(add);
// const mul2 = clacwith2(mul);
// const mul3 = clacwith3(mul);

// console.log(add3(3));
// console.log(add2(3));
// console.log(mul2(3));
// console.log(mul3(3));
// console.log(0.2 + 1.1 === 1.3);


// var name = 'zero';

// function log() {
//     console.log(name);
// }

// function ad() {
//     var name = 'nero';
//     log();
// }


// ad();

// var name = 'zero';
// function log() {
//     console.log(name);
//     }

// function wrapper() {
//     var name = 'nero';
//     log();
//     }
// wrapper();

// var name ='zero';
// function wrapper() {
//     name ='nero';
//     log();
//     function log() {
//         console.log(name);
//         }};

// wrapper();

// const counter = function() {
//     let count = 0;
//     function changeCount(num) {
//         count += num
//     }
//     return {
//         increase: function () {
//             changeCount(+1);
//         },
//         decrease: function() {
//             changeCount(-1);
//         },
//         getCount: function() {
//             return count
//         }
//     }
// };

// const counterClosure = counter();

// console.log(counterClosure.getCount());
// counterClosure.increase();
// console.log(counterClosure.getCount());
// console.log(counterClosure.count)
// console.log(counter)

function scopeTest() {
    var scope = [];
    for (var i = 0; i < 10; i++) {
        (function(j) {
        scope[j] = function() {
            console.log(j)
        }
    })(i)
    }
    scope[2]();
}
scopeTest();