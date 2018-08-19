// 数値の時は計算する
let text = prompt('入力せよ');
if(! isNaN(text)){
    console.log(parseInt(text) + 80);
}

// 文字列'入力せよ'を表示し、ユーザが入力した値を、変数'text'に入れろ
// もし、変数'text'の値が数値ならば、
// 変数'text'の値を整数化したものに、整数'80'を加えて表示しろ。