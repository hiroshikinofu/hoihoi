// データの数だけ関数を呼び出す
for (let rec of data) {
    let bill = rec['bill']
    if(rec['crg']) {
        bill = addCharge(bill);
    }
    createMail(rec['name'], bill);
}

// 変数'data'の値を順次、変数'rec'に入れる間、以下を繰り返せ。
// 変数'rec'のプロパティ'bill'を、変数'bill'に入れろ。
// もしも変数'rec'のプロパティが'bill'の場合、
// 関数'createMail'に、変数'rec'のプロパティ'name'と、変数'bili'を指定して実行しろ


// メール定型文の受信者名に任意の文字列を差し込む
let createMail = (recv, bill) =>{
    let msg = `${recv}様
PT企画の斉藤です。
今月の請求額は${bill}円です。`;
    console.log(msg);
};
// createMail('山本', 40000);

// 元の値に7%を上乗せする関数を定義する
let addCharge = (bill) => {
    return bill * 1.07;
};
// console.log(addCharge(40000));

// 複数人のデータを配列にまとめる
let data = [
    {name:'山本', bill:4000, crg:true},
    {name:'吉田', bill:25000, crg:false}
];
// console.log(data[1]['name']);
// console.log(data[1]['bill']);

// データの数だけ関数を呼び出す
for (let rec of data) {
    let bill = rec['bill']
    if(rec['crg']) {
        bill = addCharge(bill);
    }
    createMail(rec['name'], bill);
}