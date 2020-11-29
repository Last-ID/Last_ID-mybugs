function TimeDown(id, endDateStr, startDateStr) {
    //当前时间
    var nowDate = new Date();
    //结束时间
    var endDate = new Date(endDateStr);
    //[结束]相差的总秒数
    var totalEndSeconds = parseInt((endDate - nowDate) / 1000);
    //天数
    var EndDays = Math.floor(totalEndSeconds / (60 * 60 * 24));
    //取模（余数）
    var EndModulo = totalEndSeconds % (60 * 60 * 24);
    //小时数
    var EndHours = Math.floor(EndModulo / (60 * 60));
    EndModulo = EndModulo % (60 * 60);
    //分钟
    var EndMinutes = Math.floor(EndModulo / 60);
    //秒
    var EndSeconds = EndModulo % 60;
    

    //**********************************/


    //开始时间
    var startDate = new Date(startDateStr);
    //[开始]相差的总秒数
    var totalStartSeconds = parseInt((startDate - nowDate) / 1000);
    //天数
    var StartDays = Math.floor(totalStartSeconds / (60 * 60 * 24));
    //取模（余数）
    var StartModulo = totalStartSeconds % (60 * 60 * 24);
    //小时数
    var StartHours = Math.floor(StartModulo / (60 * 60));
    StartModulo = StartModulo % (60 * 60);
    //分钟
    var StartMinutes = Math.floor(StartModulo / 60);
    //秒
    var StartSeconds = StartModulo % 60;


    //输出到页面
    if(totalEndSeconds<=0)
    {
        document.getElementById(id).innerHTML ="[t][tsS:" + totalStartSeconds+"][teS:" + totalEndSeconds+"]";
    }
    else if(totalEndSeconds<=3600)
    {
        document.getElementById(id).innerHTML ="[e1][tsS:" + totalStartSeconds+"][teS:" + totalEndSeconds+"]";
    }
    
    else
    {
        document.getElementById(id).innerHTML = "[e-1][tsS:" + totalStartSeconds+"][teS:" + totalEndSeconds+"]";
    }
    //延迟一秒执行自己
    setTimeout(function () {
        TimeDown(id, endDateStr);
    }, 3000)
}