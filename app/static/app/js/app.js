// 入力フォームでリターンキー押下時に送信させない
$('#myform').on('sumbit', function (e) {
    e.preventDefault();
})

// 連続送信防止
$('.save').on('click', function (e) {
    $('.save').addClass('disabled');
    $('#myform').submit();
})

// [検索を解除] の表示制御
conditions = $('#filter').serializeArray();
$.each(conditions, function(){
    if(this.value){
        $('.filtered').css('visibility','visible')
    }
})

// ページネーションのレスポンシブ対応
// https://auxiliary.github.io/rpage/
$(".pagination").rPage();