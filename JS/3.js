'use strict';

function hello() {
    console.log('Hello!');
}

hello();
hello();
hello();

// ****************************************************

const message = hello;
message();

let anonMessage = function() {
    console.log('Anonymous message!');
}
anonMessage();
anonMessage = message;
anonMessage();

// ****************************************************

function printText(message) {
    console.log(message);
}
printText('Hi!');

// ****************************************************

// person = [                          // так как strict то глобальые переменные недоступны!
//     'Mike Amiri',
//     46,
//     true
// ];

const person = [                          // так как strict то глобальые переменные недоступны!
    'Mike Amiri',
    46,
    true
];

console.log(...person);

function displayInfoPerson(name, age, married) {
    console.log(`Age: ${age} | Name: ${name} | Married: ${married}`);
}
displayInfoPerson(...person);

// ****************************************************

function sumSmth(a = 8, b) {
    if (a == undefined) a = 10;
    if (b == undefined) b = 15;

    return a + b;
}
let a, b;
console.log(sumSmth(a, b));

function sumArgs() {
    let s = 0;
    for (const element of arguments) {
        s += +element;
    }

    return s;
}
console.log(sumArgs(1, 2, 3, 4, 5));

function restFunction(...numbers) {
    let s = 0;
    for (const element of numbers) {
        s += +element;
    }

    return s;
}
console.log(restFunction(1, 3));

let fInner = function() {
    console.log('Inner func ccalled!');
}

let fOuter = function(innerFunc) {
    console.log('Outer function called!');
    innerFunc();
}
fOuter(fInner);

// ****************************************************

const helloArrow = ()=> console.log('Hello Arrow!');
helloArrow();

const print = (text, a, b)=> console.log(text, +a + +b);
print('print called with text and sum:', '3', 4);

const printOneArg = text => console.log(text);                 // только 1 аргумент если можно опустить ()!
printOneArg('Ahahahah');

const sumArrow = (a, b) => a + b;
console.log(sumArrow(3, 8));

const getUserArrowInfo = (name_, age_, married_) => ({           // обязательно взять еще в круглые скобки!
    name: name_,
    age: age_,
    married: married_
});
console.log(getUserArrowInfo("Mike Amiri", 46, true));

const bigArrowFunc = (number1, number2) => {
    const numberRes = number1 + number2;
    return numberRes;
}
console.log(bigArrowFunc(1, 2));

// ****************************************************

console.log(abcd);              // undefined если var после этой строки | ReferenceError если let после этой строки
var abcd = 'Hello!';

// ****************************************************

function outerClosure() {                  // зымыкание - на самом деле бесполезная штука, которая затрудняет чтение кода. ООП это и есть постфикс над замыканием.
    let n = 0;

    function innerClosure() {
        n++;
        console.log(n);
    }

    return innerClosure;
}
const fn = outerClosure();
fn();
fn();

// ****************************************************

(function() {
    console.log('Invoked by self!');
}());

(function (a, b) {
    console.log(a * b);
}(2, 3));

console.log(
    `6 * 9 = `, (function (a, b) {
        return a * b;
    }(6, 9))
);

// ****************************************************

function printInnerReinit() {
    console.log('Доброу утро!');

    printInnerReinit = function() {
        console.log('Доброу вечера!');
    }
}
printInnerReinit();
printInnerReinit();

let funcg1 = printInnerReinit;
funcg1();
funcg1();

// ****************************************************

function change(x){
    x = 2 * x;
    console.log("x in change:", x);
}
 
let n = 10;
console.log("n before change:", n); // n before change: 10
change(n);                          // x in change: 20
console.log("n after change:", n);  // n after change: 10

// ****************************************************

function changeObjectLink(obj){
    obj.x = 2 * obj.x;
    console.log("x in change:", obj.x);
}

let xObj = {
    x: 10
};

console.log("xObj before change:", xObj); // xObj before change: 10
changeObjectLink(xObj);
console.log("xObj after change:", xObj); // xObj before change: 20

// ****************************************************

function changeObjectLinkFully(obj){
    obj = { x: obj.x * 2 };                           // тут передается копия ссылки, поэтому значение не меняется!
    console.log("x in change:", obj.x);
}

let xObj2 = {
    x: 10
};

console.log("xObj2 before change:", xObj2); // xObj2 before change: 10
changeObjectLinkFully(xObj2);
console.log("xObj2 after change:", xObj2); // xObj2 before change: 20
