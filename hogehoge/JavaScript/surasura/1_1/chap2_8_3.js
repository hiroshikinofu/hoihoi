// !演算子を使ってfalseのときだけ実行する
let text = prompt('年齢は？');
if(!isNaN(text)){
    console.log('数値に変換可能');
}

// 文字列'年齢は？'を表示し、ユーザの入力した値を、変数'text'に入れろ
// もし、変数'text'の値が数値に変換可能の場合、
// 文字列'数値に変換可能'を表示しろ