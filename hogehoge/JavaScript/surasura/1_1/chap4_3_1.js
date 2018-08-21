// メール定型文の受信者名に任意の文字列を差し込む
let createMail = (recv, bill) =>{
    let msg = `${recv}様
PT企画の斉藤です。
今月の請求額は${bill}円です。`;
    console.log(msg);
};
createMail('山本', 40000);

// 引数'recv'と'bill'を受けとる以下の関数を作って変数'createMail'に入れろ。
// { 変数'msg'に、次のテンプレート文字列を入れろ
// 『${recv}様
// PT企画の斉藤です。
// 今月の請求額は${bill}円です。
// 変数'msg'を表示しろ。　}
// 文字列'山本'と、'40000'を指定してメールを作れ。