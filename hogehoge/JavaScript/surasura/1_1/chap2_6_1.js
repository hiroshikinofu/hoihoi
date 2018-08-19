// else if節の書き方を覚えよう
let text = prompt('年齢は？');
let age = parseInt(text);
if(age < 20) {
    console.log('未成年');
} else if(age < 65) {
    console.log('成人');
} else {
    console.log('高齢者');
}

// 文字列'年齢は？'を表示し、ユーザの入力した値を、変数'text'に入れろ
// 変数'text'の値を整数化し、変数'age'に入れろ
// もし、変数'age'の値が、20以下の場合、
// 文字列'未成年'を表示させろ
// そうではなく、変数'age'の値が、20以上65未満の場合、
// 文字列'成人'を表示させろ
// そうではなく、変数'age'の値が65以上の場合、
// 文字列'高齢者'を表示させろ