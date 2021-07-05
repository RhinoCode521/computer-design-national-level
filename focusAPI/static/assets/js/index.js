$(document).ready(function () {
    $("#send").click(function () {
        alert(123)
        var message = $("#send_content").val()
        alert("http://60.205.250.106:5000/search?key="+message)
        $.ajax({
            url: "http://60.205.250.106:5000/search?key="+message,
            type: "GET",
            data: {
                // message: message
            },
            success: function (data) {
                alert(data)
            },
            error: function () {
                alert("接收失败")
            }
        })
    });

});






// $.ajax({
//     url:"http://www.microsoft.com",    //请求的url地址
//     dataType:"json",   //返回格式为json
//     async:true,//请求是否异步，默认为异步，这也是ajax重要特性
//     data:{"id":"value"},    //参数值
//     type:"GET",   //请求方式
//     beforeSend:function(){
//         //请求前的处理
//     },
//     success:function(req){
//         //请求成功时处理
//     },
//     complete:function(){
//         //请求完成的处理
//     },
//     error:function(){
//         //请求出错处理
//     }
// });
