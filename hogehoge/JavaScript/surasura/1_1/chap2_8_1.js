// 義務教育の対象かどうかをチェックする
let text = prompt('年齢は？');
let age = parseInt(text);
if(age >= 6 && age <= 15 ) {
    console.log('義務教育の対象');
}

// 文字列'年齢は？'を表示し、ユーザが入力した値を、変数'text'に入力しろ
// 変数'text'の値を整数化し、変数'age'に入れろ
//　もし、変数'age'の値が6以上かつ、15以下の場合ならば、
//文字列'義務教育の対象'を表示しろ