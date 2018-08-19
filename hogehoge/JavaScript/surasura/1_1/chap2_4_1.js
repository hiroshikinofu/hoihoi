// else節を追加してみよう
let text = prompt('入力せよ');
if(! isNaN(text)){
    console.log(parseInt(text) + 80);
}else{
    console.log('数字ではない');
}

// 文字列'入力せよ'を表示し、ユーザの入力した値を変数'text'に入れろ
// もし、変数'text'の値が数値の場合だったら、
// 変数'text'の値を整数化し、数値'80'を加えて表示しろ。
// 変数'text'の値が数値以外の場合、
// 文字列'数字ではない'を表示させろ。