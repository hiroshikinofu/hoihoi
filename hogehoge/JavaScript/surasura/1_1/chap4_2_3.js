// 引数を受けとる関数を作る
let createMail = (recv) => {
    console.log(recv + '様');
    console.log('PT企画の斉藤です。');
    console.log('請求書を送ります。');
}
createMail('山本');
createMail('吉田');

// 引数'recv'を受けとる以下の関数を作って、変数'createMail'に入れろ。
// {引数'recv'と文字列'様'を結合し、表示しろ。
// 文字列'PT企画の斉藤です。'を表示しろ
// 文字列'請求書を送ります。'
// }
// 引数'recv'に文字列'山本'を指定してメールを作れ。
// 引数'recv'に文字列'吉田'を指定してメールを作れ。