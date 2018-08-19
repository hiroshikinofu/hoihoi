// ２つのif文を組み合わせる
let text =prompt('年齢は？');
if(! isNaN(text)){
    let age = parseInt(text);
    if(age < 20){
        console.log('未成年');
    }
}

// 文字列'年齢は？'を表示し、ユーザが入力した値を、変数'text'に入れる
// もし、変数'text'の値が数値であるならば、
// 変数'text'の値を整数化し、変数'age'に入れろ
// さらに、変数'age'の値が20以下の場合、
// 文字列'未成年'を表示させろ