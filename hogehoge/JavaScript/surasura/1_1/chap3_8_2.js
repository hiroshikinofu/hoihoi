// 同じチーム同士の合わせをしない時だけ表示する
let team = ['A','B','C','D','E'];
for(let t1 of team){
    for(let t2 of team){
        if(t1 != t2){
            console.log(t1 + 'vs' + t2);
        }
    }
}
// 配列[文字列'A'、'B'、'C'、'D'、'E']を、変数'team'に入れろ。
// 変数'team'の値を、変数't1'に順次入れていく間、以下の処理を繰り返せ。
// 変数'team'の値を、変数't2'に順次入れていく間、以下の処理を繰り返せ。
// もし、変数't1'と、変数't2'の値が一致しない場合、
// 変数't1'と、文字列'VS'と、変数't2'を結合して表示しろ。