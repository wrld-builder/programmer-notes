var username;
let $username = 'Username';       // обьявлем переменные
console.log(username, $username);

let a = 0, b = 1, c = 2;
console.log(a, b, c);

// ****************************************************

const xConst = 100;
// xConst = 500; - error

// ****************************************************

const strConst = `His username is ${$username}`;        // интерполяция
console.log(strConst);

const longText = `Итак.
это Длинный текст.
И что?
так надо сдедлать`;
console.log(longText);

// ****************************************************

var var1 = undefined;         // var var1;   - одно и то же. знаечние не установлено
var var2 = null;          // у var2 отсутствует значение

let email = "tome@mimimail.com";
email = undefined;      // установим тип undefined
console.log(email); // undefined, хотя значение не устанолвено :)

// ****************************************************

const user = {
    name: "Tom",
    age: 24
};
console.log(user.name);

// ****************************************************

let id_ = 45;
console.log(id_, typeof id_);

id_ = '45'                           // можно и без ;
console.log(id_, typeof id_);

// ****************************************************

var inc = 5;
console.log(++inc);

inc = 5;
console.log(inc++);

console.log(inc ** 2);

inc **= 2;
console.log(inc);;;;;;;;;;;;;         // так тоже можно сделать

// ****************************************************

const numB = 0b0100;
console.log(numB);           // 4

// ****************************************************

var expr1 = 45, expr2 = '45';

if (expr1 == expr2) console.log('expr1 == expr2');

if (expr1 === expr2) console.log('expr1 === expr2');
else console.log('expr1 !=== expr2. Выржения не одинаковы по типу!');

// ****************************************************

const a_ = 89;
const b_ = 90;

console.log(a_ > b_ ? `${a_} > ${b_}` : `${a_} < ${b_}`);

// ****************************************************

console.log('hello' ?? 45);
console.log(undefined ?? 45);            // undefined of null
console.log(null ?? 45);

// ****************************************************

var message = 'Hello!';
const updateMsg = 'Update!';
message ??= updateMsg;
console.log(message);

message = undefined;
message ??= updateMsg;
console.log(message);

// ****************************************************

const num1 = 15;
var num2 = '28';

console.log(num1 + num2);         // 1528

console.log(num1 + Number(num2));                // 43
console.log(num1 + parseInt(num2));                // 43

// отличие:
num2 = '28hello'
console.log(num1 + Number(num2));         // NaN
console.log(num1 + parseInt(num2));       // 43

num2 = '28';
console.log(num1 + +num2);       //43

// ****************************************************

const arr = ['Tom', 'Alice', true];
arr.push(15);

console.log(arr);          // в const array можно добавить элемент
console.log(arr[8]);            // undefined
console.log(arr[0]);

arr[0] = 'hello';         // setter работает тоже
console.log(arr);

const people = [
    ['Tom', 37, true],
    ['Alice', 42, false]
]
console.log(people, people.length);

const nums = [[[[]]]];
nums[0][0] = 16;         // массив урезался, что то странное, не надо так делать
console.log(nums);

const numsNew = [];      // одномерный
console.log(numsNew);
numsNew[0] = [];         // двумерный
console.log(numsNew);
// и так далее..

const numsConstAssignTest = [1, 2, 3];
console.log(numsConstAssignTest);
// numsConstAssignTest = [4, 5, 6];          // TypeError! Assign to const
// console.log(numsConstAssignTest);

// ****************************************************

var smth;
if (smth) {          // проверка на наличие значения
    console.log('Знаечние тут есть! ->', smth);
} else {
    console.log('Значение тут нет! ->', smth);
}

// undefined возвращает false в блоке if
// null возвращает false в блоке if
// 0 или NaN возвращает false в блоке if
// если String пустая то false в if
// Object всегда отдает true

// ****************************************************

const income = 200;
switch (income) {
    case 500:
        console.log('500 == 200');
        break;
    case 200:
        console.log('200 == 200');
        break;
    default:
        console.log('Default called');
}

const income2 = 100;
switch (income2) {
    case 500:
        console.log('500 == 200');
        break;
    case 100:
    case 200:
        console.log('200 == 200 или 200 == 100. непонятно');
        break;
    default:
        console.log('Default called');
}

// ****************************************************

let s = '';
for (var i = 0; i < 5; i++) {
    s += ' ' + String(i + 1);
}
console.log(s, i);               // при let i будет ReferenceError  ; при var будет 5


const person = {name: "Tom", age: 37};
for (const property in person) {
    console.log(property + ' : ' + person[property]);
}

let smthResS = '';
const smthStr = 'Hello World!';
for (const data of smthStr) {
    smthResS += data + '-';
}
console.log(smthResS);

// for (const data of person) {                  // Object is not iterable!
//     console.log(data);
// }

const iterArr = [1, 2, 3, 4, 5];
for (const num of iterArr) console.log(num);