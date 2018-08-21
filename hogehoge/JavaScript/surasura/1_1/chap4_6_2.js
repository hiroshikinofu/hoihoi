// createMail関数の文面を変更する
let createMail = (recv) => {
    console.log(recv + '様');
    console.log('はじめまして。');
}
createMail('山本');

// 請求書がマイナスのときは0を返す
let addCharge = (bill) => {
    if(bill < 0){
        return 0;
    }
    return bill * 1.07;
};
console.log(addCharge(-1000));